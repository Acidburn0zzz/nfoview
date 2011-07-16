# Copyright (C) 2006-2009 Osmo Salomaa
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

"""Baseclass and wrapper for :class:`Gtk.Builder` constructed dialogs."""

from gi.repository import Gtk

__all__ = ("BuilderDialog",)


class BuilderDialog(object):

    """Baseclass and wrapper for `Gtk.Builder` constructed dialogs.

    :cvar widgets: List of names of widgets to be assigned as attributes

    All widgets defined in :attr:`widgets` are assigned as instance variables
    with names preceded by a single underscore. All signals defined in the UI
    definition file are connected to ``self``. All :func:`getattr` calls not
    found in ``self`` are delegated to :attr:`self._dialog` allowing ``self``
    to look and act like a :class:`Gtk.Dialog`.
    """

    widgets = (NotImplementedError,)

    def __getattr__(self, name):
        """Return attribute from either ``self`` or :attr:`self._dialog`."""
        return getattr(self._dialog, name)

    def __init__(self, ui_file_path):
        """Initialize a :class:`BuilderDialog` object from `ui_file_path`."""
        self._builder = Gtk.Builder()
        self._builder.set_translation_domain("nfoview")
        self._builder.add_from_file(ui_file_path)
        self._builder.connect_signals(self)
        self._dialog = self._builder.get_object("dialog")

        for name in self.widgets:
            widget = self._builder.get_object(name)
            setattr(self, "_%s" % name, widget)

    def run(self):
        """Show the dialog, run it and return response."""
        self._dialog.show()
        return self._dialog.run()
