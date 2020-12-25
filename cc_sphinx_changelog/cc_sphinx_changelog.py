#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main module."""

import backpedal
import git

def get_repo(repo_top=None):
    # TODO: Path from config (or URL??)
    if not repo_top:
        repo_top = backpedal.find(".git", item_type="directory")
    return git.Repo(repo_top)


def get_commit_messages(repo):
    log = repo.head.log()
    commit_messages = [commit.message.strip() for commit in repo.iter_commits()]
    return commit_messages


def group_commits(commit_messages):
    releases = {"Unreleased": {}}
    current_release = releases["Unreleased"]
    for message in commit_messages:
        if message.startswith("bump:"):
            rel_head = message.split(" → ")[-1]
            releases[rel_head] = {}
            current_release = releases[rel_head]
        fmt_message(message, current_release)
    return releases


def fmt_message(message, current_release):
    if message.startswith("bump:"):
        return
    message = message.split(":")
    commit_type, commit_message =  message[0], ":".join(message[1:])
    if "\n" in commit_message:
        commit_message = "\n".join([commit_message.splitlines()[0]]+["  "+msg for msg in commit_message.splitlines()][1:])
    scope = None
    if "(" in commit_type and ")" in commit_type:
        commit_type, scope = commit_type.split("(")
        scope = scope.replace(")", "")
    commits = current_release.setdefault(commit_type, [])
    fmted_message = f"**{scope}**: {commit_message}" if scope else f"{commit_message}"
    commits.append(fmted_message)


if __name__ == "__main__":
    repo = get_repo()
    commit_messages = get_commit_messages(repo)
    releases = group_commits(commit_messages)

    for release in releases:
        print(release)
        print("="*len(release))
        for heading, items in releases[release].items():
            print(f"{heading}")
            print("-"*len(heading))
            for item in items:
                print(f"* {item}")
