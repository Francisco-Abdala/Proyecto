import sys
import gi

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk


class ExampleDialog(Gtk.MessageDialog):
    def __init__(self, parent):
        super().__init__(title="Estariamos listos", transient_for=parent)

        self.add_buttons(
            "_OK",
            Gtk.ResponseType.OK
        )

        self.set_markup("Se guardó con éxito")
