====================================
Conventional Commit Sphinx Changelog
====================================


.. image:: https://img.shields.io/pypi/v/cc_sphinx_changelog.svg
        :target: https://pypi.python.org/pypi/cc_sphinx_changelog

.. image:: https://github.com/pgierz/cc_sphinx_changelog/workflows/Python%20package/badge.svg
        :target: https://github.com/pgierz/cc_sphinx_changelog/actions?query=workflow%3A%22Python+package%22

.. image:: https://readthedocs.org/projects/convention-commits-sphinx/badge/?version=latest
        :target: https://convention-commits-sphinx.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Automatically generates a releases-style changelog based on conventional commit messages.


* Free software: GNU General Public License v3
* Documentation: https://convention-commits-sphinx.readthedocs.io.


Features
--------

Add the following to your Sphinx ReST files to get an automatically generated changelog based upon conventional commit messages::

    .. cc_changelog::


For more info on conventional commits, please see:

* https://www.conventionalcommits.org/en/v1.0.0/
* https://commitizen-tools.github.io/commitizen/

Here is an example of a changelog in ``git log --graph --oneline`` form::

    * 37b88f7 - (HEAD -> master, origin/master) docs(README): uses rtd link from project home (copy/paste) (64 seconds ago) <Paul Gierz>
    * 2106914 - docs(readme): fixes double dot in badge link (oops) (5 minutes ago) <Paul Gierz>
    * dba6788 - docs(README): fixes readme links (6 minutes ago) <Paul Gierz>
    * 87e04fc - (tag: v0.6.1) bump: version 0.6.0 → 0.6.1 (19 minutes ago) <GitHub Action>
    * afc76c2 - fix(setup.py): adds missing dependencies (20 minutes ago) <Paul Gierz>
    * 3a5de72 - test(tox): removes tox test suite (20 minutes ago) <Paul Gierz>
    * fa9923e - (tag: v0.6.0) bump: version 0.5.2 → 0.6.0 (26 minutes ago) <GitHub Action>
    * 17137dc - feat: adds sphinx directive (27 minutes ago) <Paul Gierz>
    * 1253061 - feat: adds optional printing of colors (default on) (28 minutes ago) <Paul Gierz>
    * 60d2aa6 - (tag: v0.5.2) bump: version 0.5.1 → 0.5.2 (2 days ago) <GitHub Action>
    * f025602 - refactor: moves main program into a simple function (2 days ago) <Paul Gierz>
    * acf0e3f - style: applies black and isort (2 days ago) <Paul Gierz>
    * 944e0b7 - docs: changes to rtd theme, adds heading to changelog (3 days ago) <Paul Gierz>
    * 89ad1e5 - docs: adds formatted changelog to docs (3 days ago) <Paul Gierz>
    * a09c9b0 - (tag: v0.5.1) bump: version 0.5.0 → 0.5.1 (3 days ago) <GitHub Action>
    * 55dec48 - fix: fixes heading grouping logic (3 days ago) <Paul Gierz>
    * 43a8501 - fix(setup.py): adds missing dependencies (3 days ago) <Paul Gierz>
    * 8997fa7 - (tag: v0.5.0) bump: version 0.4.1 → 0.5.0 (3 days ago) <Paul Gierz>
    *   dff4e2f - Merge remote-tracking branch 'origin/master' (3 days ago) <Paul Gierz>
    |\
    | * d25017d - (tag: v0.4.1) bump: version 0.4.0 → 0.4.1 (4 days ago) <GitHub Action>
    * | fb11339 - feat: adds color output and formats to stdout nicely (3 days ago) <Paul Gierz>
    * | 0dc1750 - (origin/feature/funcs) refactor: puts everything into functions (3 days ago) <Paul Gierz>
    |/
    * 9ea4503 - ci: automatically publish to pypi when automatic bump occurs (4 days ago) <Paul Gierz>
    * 06d4115 - fix: better implementation of getting commit messages (4 days ago) <Paul Gierz>
    * 0d9a1e5 - (tag: v0.4.0) bump: version 0.3.0 → 0.4.0 (4 days ago) <GitHub Action>
    * c9dd3c2 - feat: parses log and prints rST style release version summaries (4 days ago) <Paul Gierz>
    * df12a50 - docs(changelog): changelog fixup (4 days ago) <Paul Gierz>
    * 04209f6 - (tag: v0.3.0) bump: version 0.2.0 → 0.3.0 (4 days ago) <Paul Gierz>
    * 75a190a - feat: automatic bump version on push (4 days ago) <Paul Gierz>
    * c39e0fb - (tag: v0.2.0) bump: version 0.1.1 → 0.2.0 (4 days ago) <Paul Gierz>
    * 72f506a - fix(tags): adds v prefix to tags (4 days ago) <Paul Gierz>
    * 5724fb1 - ci: fixs tag publishing (4 days ago) <Paul Gierz>
    * fbd165c - ci: removes travis ci (4 days ago) <Paul Gierz>
    * 8b73303 - (tag: 0.1.1) bump: version 0.1.0 → 0.1.1 (4 days ago) <Paul Gierz>
    * 839fb8d - fix(cz): fixup conventional commit bumping (4 days ago) <Paul Gierz>
    * 2fc0466 - (tag: 0.1.0) bump: version 0.0.1 → 0.1.0 (4 days ago) <Paul Gierz>
    * f78d28e - feat: initial commit (4 days ago) <Paul Gierz>

Roadmap
-------

In the future, I'd like to include better formatting in Sphinx (preserve
paragraphs), as well as automatically create links to issue numbers and
releases.
