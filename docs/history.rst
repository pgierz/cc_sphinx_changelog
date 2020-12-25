=========
Changelog
=========


Unreleased
==========


0.5.1
=====
Bug Fixes
---------
* 55dec48                  fixes heading grouping logic

                           The grouping logic in the heading formatting function was incorrect,
                           and retrieved a string ``Unknown`` rather than the list the
                           ``Unknown`` key was pointing to.  Closes #3
* 43a8501 [setup.py]       adds missing dependencies

                           Closes #4


0.5.0
=====
New Feature
-----------
* fb11339                  adds color output and formats to stdout nicely

                           Closes #2
Support
-------
* 0dc1750                  puts everything into functions
Unknown
-------
* dff4e2f


0.4.1
=====
Bug Fix
-------
* 06d4115                  better implementation of getting commit messages

                           The previous implementation was looking at ``git.head.log()``, which
                           did not register all commits as commits, some rather as pull or merge.
                           Now we directly iterate over commits and extract the log message. This
                           also preserves body parts of the message.
Support
-------
* 9ea4503                  automatically publish to pypi when automatic bump occurs


0.4.0
=====
New Feature
-----------
* c9dd3c2                  parses log and prints rST style release version summaries

                           This parses the log, gives headers based upon 'bump: ', and gathers
                           each commit in a bullet point list. Next step is to parse type of
                           change.
Support
-------
* df12a50 [changelog]      changelog fixup


0.3.0
=====
New Feature
-----------
* 75a190a                  automatic bump version on push


0.2.0
=====
Bug Fix
-------
* 72f506a [tags]           adds v prefix to tags
Support
-------
* 5724fb1                  fixs tag publishing

                           Tags in this project don't use the v prefix.
* fbd165c                  removes travis ci


0.1.1
=====
Bug Fix
-------
* 839fb8d [cz]             fixup conventional commit bumping


0.1.0
=====
New Feature
-----------
* f78d28e                  initial commit


