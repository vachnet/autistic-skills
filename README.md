# Easy Communication / สื่อสารง่าย

Two instruction-based skills for accessible communication and optional practice, in Thai and English. Built for autistic communicators with different language, reading, sensory, and motor preferences. Autism does not imply inability to communicate or a particular reading level.

**Status: local prototype, not publicly published, not clinically validated.** No child usability trials or live ChatGPT/Claude installation tests have been completed. These skills support communication; they do not diagnose, treat autism, or replace a person's AAC system or communication partners.

## Start here / เริ่มที่นี่

- [คู่มือภาษาไทย](docs/START-TH.md)
- [English installation and use](docs/START-EN.md)
- [Sample conversations](docs/EXAMPLES.md)
- [Platform eligibility and evidence](docs/SOURCES.md)
- [Publication status and next steps](docs/PUBLISHING.md)

| Skill | Purpose | Starter |
|---|---|---|
| `easy-communication` | Express a real message, need, feeling, refusal, or question | ช่วยฉันสื่อสาร / Help me communicate |
| `communication-practice` | Opt-in short role-play, chosen by the learner | ฝึกสื่อสาร / Let's practice communication |

Thai is the default if the language is unclear. The user's language takes priority. `ไทย`, `English`, or `สองภาษา / both` switches language; bilingual output is opt-in. Text choices are numbered lines, not clickable app buttons. A person may type a number, a word, an emoji, or their own message. Speech depends on the host app's existing accessibility features.

## Age and platform limits

| Age | ChatGPT | Claude consumer app |
|---|---|---|
| Under 13 | An adult must conduct the interaction; provide offline practice materials for adult use | No independent child use; adults can prepare materials for use offline |
| 13–17 | Parental consent required; practice may be learner-led within platform rules and an agreed support plan | No independent minor use; adults can prepare offline materials |
| 18+ | Direct use subject to account rules and availability | Direct use subject to account rules and availability |

These are the official rules checked on 2026-10-24; recheck before release. Do not bypass restrictions through account sharing. A separate app using an API would require a separate design and policy review; this project is not that app.

## Build

Run `python3 scripts/build_release.py`. It creates two Claude ZIPs, one OpenAI skills-only plugin ZIP, a complete source ZIP, checksums, and a packaging report in `dist/`. Each Claude ZIP contains exactly one self-contained skill folder. The OpenAI ZIP has `plugin.json` at its root.

`python3 scripts/build_release.py --publisher 'Your chosen public name'` adds publisher metadata once a real name is supplied. It does not verify identity or publish anything. Without that option, publisher metadata stays absent and the report explicitly marks public submission as incomplete.

## Design decisions

The supplied Thai project account inspired optional sentence expansion, preview/confirmation, short messages, familiar vocabulary, and clear ending/replay. This is an original adaptation, not a reproduction of that article or a claim of affiliation with the named association, foundation, university, or company. Missing screenshots and code in the pasted account were not available for inspection.

We intentionally allow refusals and questions from the start; do not require subject–verb–object order, hide unusual word combinations, reorder choices by popularity, require speech, or use timed double taps. Existing personal AAC vocabulary remains available. The 100 most frequent internet words are not treated as a validated vocabulary for every autistic user.

No tracking code, external tools, connectors, network calls, camera access, or executable scripts are included inside the skills. The host service still processes the conversation under its own terms. Durable memory, microphone access, and true picture-board interactions are not provided by these instruction files.

Publication requires a verified publisher and an authenticated publishing channel. No license has been selected yet; public reuse terms must be decided by the project owner before release.
