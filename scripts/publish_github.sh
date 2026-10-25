#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."
repository='vachnet/autistic-skills'

command -v gh >/dev/null || { echo 'Install GitHub CLI first: https://cli.github.com'; exit 1; }
command -v git >/dev/null || { echo 'Install Git first.'; exit 1; }
if ! gh api user --jq .login >/dev/null 2>&1; then
  gh auth login --hostname github.com --web --git-protocol https
fi
account="$(gh api user --jq .login)"
if [ "$account" != 'vachnet' ]; then
  gh auth switch --hostname github.com --user vachnet
fi
gh auth setup-git --hostname github.com

if [ ! -d .git ]; then
  git init -b main
fi
if git remote get-url origin >/dev/null 2>&1; then
  remote="$(git remote get-url origin)"
  case "$remote" in
    https://github.com/vachnet/autistic-skills|https://github.com/vachnet/autistic-skills.git|git@github.com:vachnet/autistic-skills.git) ;;
    *) echo "Stopped: origin points to another repository: $remote"; exit 1 ;;
  esac
fi

git add -- .gitignore README.md docs evals plugins scripts
if ! git diff --cached --quiet; then
  git commit -m 'Add accessible communication skills and documentation'
fi

if gh repo view "$repository" >/dev/null 2>&1; then
  visibility="$(gh repo view "$repository" --json visibility --jq .visibility)"
  if [ "$visibility" != 'PUBLIC' ]; then
    echo 'Stopped: the existing repository is private; its visibility was not changed.'
    exit 1
  fi
  if ! git remote get-url origin >/dev/null 2>&1; then
    git remote add origin "https://github.com/$repository.git"
  fi
  git push --set-upstream origin HEAD:main
else
  gh repo create "$repository" --public --source=. --remote=origin --push
fi

local_commit="$(git rev-parse HEAD)"
remote_commit="$(git ls-remote origin refs/heads/main | awk '{print $1}')"
if [ "$local_commit" != "$remote_commit" ]; then
  echo 'Remote commit verification failed.'
  exit 1
fi
gh repo view "$repository" --json url,visibility --jq '"Verified: " + .url + " (" + .visibility + ")"'
