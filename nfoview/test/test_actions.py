# Copyright (C) 2005-2007 Osmo Salomaa
#
# This file is part of NFO Viewer.
#
# NFO Viewer is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# NFO Viewer is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# NFO Viewer. If not, see <http://www.gnu.org/licenses/>.

import nfoview


class TestModule(nfoview.TestCase):

    def test_attributes(self):

        for name in nfoview.actions.__all__:
            action = getattr(nfoview.actions, name)()
            assert hasattr(action, "accelerator")
            assert hasattr(action.props, "name")
            assert hasattr(action.props, "label")
            assert hasattr(action.props, "tooltip")

    def test_update_sensitivity__insensitive_view(self):

        window = nfoview.Window()
        for name in nfoview.actions.__all__:
            action = getattr(nfoview.actions, name)()
            action.update_sensitivity(window)

    def test_update_sensitivity__sensitive_view(self):

        window = nfoview.Window(self.get_nfo_file())
        for name in nfoview.actions.__all__:
            action = getattr(nfoview.actions, name)()
            action.update_sensitivity(window)
