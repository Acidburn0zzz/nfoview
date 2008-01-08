# Copyright (C) 2007 Osmo Salomaa
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

"""Dialog for displaying credits and information."""

import gtk
import nfoview
_ = nfoview.i18n._

__all__ = ("AboutDialog",)

_LICENSE = """\
NFO Viewer is free software: you can redistribute it and/or modify it under \
the terms of the GNU General Public License as published by the Free Software \
Foundation, either version 3 of the License, or (at your option) any later \
version.

NFO Viewer is distributed in the hope that it will be useful, but WITHOUT ANY \
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR \
A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with \
NFO Viewer. If not, see <http://www.gnu.org/licenses/>."""


class AboutDialog(gtk.AboutDialog):

    """Dialog for displaying credits and information."""

    def __init__(self, parent):

        gtk.AboutDialog.__init__(self)
        gtk.about_dialog_set_url_hook(self._on_url_clicked)
        self.set_transient_for(parent)
        self.set_title(_("About NFO Viewer"))
        self.set_name(_("NFO Viewer"))
        self.set_version(nfoview.__version__)
        self.set_copyright(u"Copyright \xa9 2005-2007 Osmo Salomaa")
        self.set_comments(_("Viewer for NFO files"))
        self.set_license(_LICENSE)
        self.set_wrap_license(True)
        self.set_website("http://home.gna.org/nfoview/")
        self.set_website_label(_("NFO Viewer Website"))
        self.set_authors(("Osmo Salomaa <otsaloma@cc.hut.fi>",))
        self.set_logo_icon_name("gtk-dialog-info")

        # Translators: This is a special message that shouldn't be translated
        # literally. It is used in the about dialog to give credits to the
        # translators. Thus, you should translate it to your name and email
        # address. You can also include other translators who have contributed
        # to this translation; in that case, please write them on separate
        # lines seperated by newlines (\n).
        self.set_translator_credits(_("translator-credits"))

    def _on_url_clicked(self, dialog, url):
        """Open website in a web browser."""

        nfoview.util.browse_url(url)
