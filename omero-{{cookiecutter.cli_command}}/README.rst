.. image:: {{ cookiecutter.github_repository_url }}/workflows/OMERO/badge.svg
    :target: {{ cookiecutter.github_repository_url }}

.. image:: https://badge.fury.io/py/omero-{{cookiecutter.cli_command}}.svg
    :target: https://badge.fury.io/py/omero-{{cookiecutter.cli_command}}

omero-{{cookiecutter.cli_command}}
==================================

{{cookiecutter.short_description}}


Requirements
============

* OMERO 5.6.0 or newer
* Python 3.6 or newer


Installing from PyPI
====================

This section assumes that an OMERO.py is already installed.

Install the command-line tool using `pip <https://pip.pypa.io/en/stable/>`_:

::

    $ pip install -U omero-{{cookiecutter.cli_command}}

Release process
---------------

This repository uses `bump2version <https://pypi.org/project/bump2version/>`_ to manage version numbers.
To tag a release run::

    $ bumpversion release

This will remove the ``.dev0`` suffix from the current version, commit, and tag the release.

To switch back to a development version run::

    $ bumpversion --no-tag [major|minor|patch]

specifying ``major``, ``minor`` or ``patch`` depending on whether the development branch will be a `major, minor or patch release <https://semver.org/>`_. This will also add the ``.dev0`` suffix.

Remember to ``git push`` all commits and tags.

License
-------

This project, similar to many Open Microscopy Environment (OME) projects, is
licensed under the terms of the GNU General Public License (GPL) v2 or later.

Copyright
---------

2017-2020, The Open Microscopy Environment
