#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Main module."""

import sys
import textwrap

import backpedal
import crayons
import git
from ansiwrap import ansilen


def ansi_ljust(s, width):
    needed = width - ansilen(s)
    if needed > 0:
        return s + " " * needed
    else:
        return s


def get_repo(repo_top=None):
    # TODO: Path from config (or URL??)
    if not repo_top:
        repo_top = backpedal.find(".git", item_type="directory")
    return git.Repo(repo_top)


def get_commit_messages(repo):
    log = repo.head.log()
    commit_messages = [
        (commit.hexsha[:7], commit.message.strip()) for commit in repo.iter_commits()
    ]
    return commit_messages


def group_commits(commit_messages):
    releases = {"Unreleased": {}}
    current_release = releases["Unreleased"]
    for message in commit_messages:
        if message[1].startswith("bump:"):
            rel_head = message[1].split(" → ")[-1]
            releases[rel_head] = {}
            current_release = releases[rel_head]
        fmt_message(message, current_release)
    return releases


def fmt_message(message, current_release):
    sha, message = message
    if message.startswith("bump:"):
        return
    message = message.split(":")
    commit_type, commit_message = message[0], ":".join(message[1:])
    if "\n" in commit_message:
        commit_header = commit_message.splitlines()[0].lstrip()
        commit_body = textwrap.fill(" ".join(commit_message.splitlines()[1:]).strip())
        commit_body = "\n".join(27 * " " + l for l in commit_body.splitlines())
        commit_message = f"{commit_header}\n\n{commit_body}"
    else:
        commit_message = commit_message.strip()
    scope = None
    if "(" in commit_type and ")" in commit_type:
        commit_type, scope = commit_type.split("(")
        scope = scope.replace(")", "")
    commits = current_release.setdefault(commit_type, [])
    if scope:
        prejust = f"{crayons.yellow(sha)} [{crayons.red(scope)}]"
        fmted_message = f"{ansi_ljust(prejust, 25)}" + commit_message
    else:
        fmted_message = f"{ansi_ljust(crayons.yellow(sha), 25)}{commit_message}"
    commits.append(fmted_message)


def fmt_headings(items):
    TYPES = {
        "fix": "Bug Fix",
        "feat": "New Feature",
        "ci": "Support",
        "docs": "Support",
        "perf": "Support",
        "refactor": "Support",
    }
    SHOWN_HEADINGS = {"Bug Fix": [], "New Feature": [], "Support": [], "Unknown": []}
    for heading, commits in items:
        group = SHOWN_HEADINGS.get(TYPES.get(heading, "Unknown"))
        for commit in commits:
            group.append(commit)
    for group in SHOWN_HEADINGS:
        if group == "Bug Fix":
            if len(SHOWN_HEADINGS[group]) > 1:
                SHOWN_HEADINGS["Bug Fixes"] = SHOWN_HEADINGS[group]
                del SHOWN_HEADINGS[group]
        elif group == "New Feature":
            if len(SHOWN_HEADINGS[group]) > 1:
                SHOWN_HEADINGS["New Features"] = SHOWN_HEADINGS[group]
                del SHOWN_HEADINGS[group]
    return SHOWN_HEADINGS


if __name__ == "__main__":
    repo = get_repo()
    commit_messages = get_commit_messages(repo)
    releases = group_commits(commit_messages)

    for release in releases:
        print(crayons.cyan(release))
        print(crayons.cyan("="*len(release)))
        for heading, items in fmt_headings(releases[release].items()).items():
            if items:
                print(f"{crayons.green(heading)}")
                print(crayons.green("-"*len(heading)))
                for item in items:
                    print(f"* {item}")
        print("\n")
