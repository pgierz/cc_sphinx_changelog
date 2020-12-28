# -*- coding: utf-8 -*-

"""Top-level package for Conventional Commit Sphinx Changelog."""

__author__ = """Paul Gierz"""
__email__ = "pgierz@awi.de"
__version__ = "0.6.0"


from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.statemachine import ViewList
from sphinx.util.nodes import nested_parse_with_titles

from . import cc_sphinx_changelog


def make_section():
    section = nodes.section()
    section.attributes['ids'] = ["changelog"]
    section.attributes['names'] = ["changelog"]
    return section


class ConventionalCommitChangelog(Directive):

    def run(self):
        changelog = make_section()
        changelog += nodes.title(text="Changelog")

        repo = cc_sphinx_changelog.get_repo()
        commit_messages = cc_sphinx_changelog.get_commit_messages(repo)
        releases = cc_sphinx_changelog.group_commits(commit_messages, add_colors=False)


        for release in releases:
            release_section = make_section()
            release_section += nodes.title(text=release)
            changelog += release_section
            for heading, items in cc_sphinx_changelog.fmt_headings(releases[release].items()).items():
                if items:
                    heading_section = make_section()
                    heading_section.document = self.state.document
                    heading_section += nodes.title(text=heading)
                    release_section += heading_section
                    lst = nodes.bullet_list()
                    heading_section += lst
                    for indx, item in enumerate(items):
                        rst = ViewList()
                        cl_item = nodes.list_item()
                        lst += cl_item
                        rst.append(item, "changelog_tmp.rst", indx)
                        nested_parse_with_titles(self.state, rst, cl_item)
        return [changelog]


def setup(app):
    """Sphinx directive for making a changelog.

    Use the following to insert a formatted changelog:

    .. cc_changelog
    """
    app.add_directive("cc_changelog", ConventionalCommitChangelog)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

