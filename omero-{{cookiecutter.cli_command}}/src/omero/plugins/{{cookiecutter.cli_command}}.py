#!/usr/bin/env python

#
# Copyright (c) {% now 'utc', '%Y' %} {{ cookiecutter.copyright_holder }}.
# All rights reserved.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

{% set class_name = cookiecutter.cli_command[0].upper() + cookiecutter.cli_command[1:] %}

import sys

from omero.cli import CLI
from omero_{{cookiecutter.cli_command}} import HELP, {{class_name}}Control

try:
    register("{{cookiecutter.cli_command}}", {{class_name}}Control, HELP)
except NameError:
    if __name__ == "__main__":
        cli = CLI()
        cli.register("{{cookiecutter.cli_command}}", {{class_name}}Control, HELP)
        cli.invoke(sys.argv[1:])
