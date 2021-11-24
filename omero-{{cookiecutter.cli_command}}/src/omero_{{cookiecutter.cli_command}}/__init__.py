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

from omero.cli import BaseControl, Parser

HELP = ("""{{cookiecutter.short_description}}

Add your documentation here.

Examples:

    # Do something
    omero {{cookiecutter.cli_command}} ...

""")


class {{class_name}}Control(BaseControl):

    def _configure(self, parser: Parser) -> None:
        parser.add_login_arguments()
        parser.add_argument(
            "--force",
            "-f",
            default=False,
            action="store_true",
            help="Actually do something. Default: false.",
        )
        parser.set_defaults(func=self.action)

    def action(self, args):
        conn = self.ctx.conn(args)
        self.ctx.out("done.")
