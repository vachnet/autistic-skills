#!/usr/bin/env python3
"""Build deterministic, local skill archives. Never uploads or authenticates."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "easy-communication"
VERSION = "0.1.0"


def archive(path, entries):
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as out:
        for name, data in sorted(entries.items()):
            if name.startswith("/") or ".." in Path(name).parts:
                raise ValueError(f"Unsafe archive path: {name}")
            info = zipfile.ZipInfo(name, date_time=(2026, 10, 24, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            out.writestr(info, data)
    with zipfile.ZipFile(path) as check:
        assert check.testzip() is None
        assert set(check.namelist()) == set(entries)
        for name, data in entries.items():
            assert check.read(name) == data


def check_skill(folder):
    text = (folder / "SKILL.md").read_text()
    match = re.match(r"\A---\nname: ([a-z0-9-]+)\ndescription: ([^\n]+)\n---\n", text)
    assert match and match[1] == folder.name, f"Invalid skill frontmatter: {folder}"
    assert len(match[1]) < 64 and len(match[2]) <= 1024
    assert "TODO" not in text and "[INSERT" not in text
    for target in re.findall(r"\]\((references/[^)]+)\)", text):
        assert (folder / target).is_file(), f"Missing reference: {target}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publisher", help="Actual public publisher name; omitted until supplied")
    args = parser.parse_args()
    if args.publisher is not None and not 1 <= len(args.publisher.strip()) <= 80:
        parser.error("Publisher must contain 1–80 nonblank characters")
    publisher = args.publisher.strip() if args.publisher else None

    notes = (ROOT / "docs" / "PLATFORM-NOTES.md").read_bytes()
    skill_folders = sorted((PLUGIN / "skills").iterdir())
    for folder in skill_folders:
        (folder / "references" / "platform-notes.md").write_bytes(notes)
        check_skill(folder)

    manifest = json.loads((PLUGIN / "plugin.json").read_text())
    assert manifest["version"] == VERSION
    ui = manifest["extensions"]["com.openai"]["interface"]
    assert len(ui["displayName"]) <= 30 and len(ui["shortDescription"]) <= 30
    assert len(ui["longDescription"]) <= 4000
    assert len(ui["defaultPrompt"]) <= 3
    assert all(len(p) <= 128 for p in ui["defaultPrompt"])
    if publisher:
        manifest["author"] = {"name": publisher}
        ui["developerName"] = publisher
    for field in ("logo", "composerIcon"):
        target = PLUGIN / ui[field]
        assert target.is_file() and target.stat().st_size <= 5 * 1024 * 1024
        svg = ET.fromstring(target.read_text())
        assert int(svg.attrib["width"]) == int(svg.attrib["height"]) >= 48

    entries = {p.relative_to(PLUGIN).as_posix(): p.read_bytes()
               for p in PLUGIN.rglob("*") if p.is_file()}
    entries["plugin.json"] = (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode()
    dist = ROOT / "dist"
    dist.mkdir(exist_ok=True)
    built = []
    target = dist / f"openai-easy-communication-{VERSION}.zip"
    archive(target, entries)
    built.append(target)

    for folder in skill_folders:
        skill_entries = {f"{folder.name}/{p.relative_to(folder).as_posix()}": p.read_bytes()
                         for p in folder.rglob("*") if p.is_file() and "agents" not in p.relative_to(folder).parts}
        target = dist / f"claude-{folder.name}-{VERSION}.zip"
        archive(target, skill_entries)
        built.append(target)

    source = {}
    for p in ROOT.rglob("*"):
        rel = p.relative_to(ROOT)
        if not p.is_file() or any(part in {"dist", ".git", "__pycache__", ".venv"} for part in rel.parts):
            continue
        if rel.parts[0] not in {"docs", "scripts", "plugins", "evals"} and rel.as_posix() != "README.md":
            continue
        source[f"easy-communication/{rel.as_posix()}"] = p.read_bytes()
    target = dist / f"easy-communication-source-{VERSION}.zip"
    archive(target, source)
    built.append(target)

    checksums = "".join(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.name}\n" for p in built)
    (dist / "SHA256SUMS.txt").write_text(checksums)
    report = {
        "version": VERSION,
        "structural_checks": "passed: paths, references, frontmatter, metadata lengths, assets, archive integrity and readback",
        "publisher": publisher,
        "public_submission_ready": False,
        "publication_status": "not published",
        "remaining": ["verified developer identity and authenticated publishing access", "owner-selected reuse license", "live host installation and behavioral evaluation", "participatory user evaluation before claims of child readiness"] + ([] if publisher else ["actual public publisher name"]),
        "limits": "Local structural validation only; no marketplace review, clinical validation, or child trial.",
        "files": [p.name for p in built]
    }
    (dist / "BUILD-REPORT.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
