# -*- coding: utf-8 -*-

"""Main module."""

import backpedal
import git

# TODO: Path from config (or URL??)
repo_top = backpedal.find(".git", item_type="directory")
repo = git.Repo(repo_top)

log = repo.head.log()
commit_messages = [commit.message.strip() for commit in repo.iter_commits()]
releases = {"Unreleased": []}
current_release = releases["Unreleased"]
for message in commit_messages:
    if message.startswith("bump:"):
        rel_head = message.split(" → ")[-1]
        releases[rel_head] = []
        current_release = releases[rel_head]
    current_release.append(message)

for release in releases:
    print(release)
    print("="*len(release))
    for item in releases[release]:
        print(f"* {item}")
    print("\n")
