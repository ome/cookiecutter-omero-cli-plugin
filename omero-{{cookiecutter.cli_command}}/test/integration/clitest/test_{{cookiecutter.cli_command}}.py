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

import omero
import pytest
from omero.testlib.cli import CLITest
from omero.plugins.{{cookiecutter.cli_command }}import {{class_name}}Control


class Test{{class_name}}(CLITest):

    def setup_method(self, method):
        super(Test{{class_name}}, self).setup_method(method)
        self.cli.register("{{cookiecutter.cli_command}}", {{class_name}}Control, "TEST")
        self.args += ["{{cookiecutter.cli_command}}"]

    def {{cookiecutter.cli_command}}(self, capfd):
        self.cli.invoke(self.args, strict=True)
        return capfd.readouterr()[0]

    def test_{{cookiecutter.cli_command}}(self):
        name = self.uuid()
        oid = self.create_object("Project", name="my test")
        obj_arg = '%s%s:%s' % (object_type, model, oid)
        self.args += [obj_arg]
        out = self.{{cookiecutter.cli_command}}(capfd)
