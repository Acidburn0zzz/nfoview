# -*- coding: utf-8 -*-

# Copyright (C) 2008 Osmo Salomaa
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Dialog for selecting NFO files to open."""

from gi.repository import GObject
from gi.repository import Gtk
from nfoview.i18n  import _

__all__ = ("OpenDialog",)


class OpenDialog(Gtk.FileChooserDialog):

    """Dialog for selecting NFO files to open."""

    def __init__(self, parent):
        """Initialize an :class:`OpenDialog` instance."""
        GObject.GObject.__init__(self)
        self.set_title(_("Open"))
        self.set_transient_for(parent)
        self.set_action(Gtk.FileChooserAction.OPEN)
        self.add_button(_("_Cancel"), Gtk.ResponseType.CANCEL)
        self.add_button(_("_Open"), Gtk.ResponseType.OK)
        self.set_select_multiple(True)
        self.set_default_response(Gtk.ResponseType.OK)
        file_filter = Gtk.FileFilter()
        file_filter.set_name(_("All files"))
        file_filter.add_pattern("*")
        self.add_filter(file_filter)
        file_filter = Gtk.FileFilter()
        file_filter.set_name(_("NFO files (*.nfo)"))
        file_filter.add_pattern("*.[Nn][Ff][Oo]")
        self.add_filter(file_filter)
        self.set_filter(file_filter)
