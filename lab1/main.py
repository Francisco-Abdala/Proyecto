import sys

import gi

gi.require_version("Gtk", "4.0")

from gi.repository import Gtk
from dialog import ExampleDialog


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        self.set_default_size(800, 250)
        self.set_title("Ejemplo")

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing= 10)
        self.set_child(self.box)    

        self.grid1 = Gtk.GridView()
        self.box.append(self.grid1)

        self.label1 = Gtk.Label()
        self.label1.set_text("Escriba lo que desee guardar")
        self.box.append(self.label1)

        self.entrada = Gtk.Entry()
        self.box.append(self.entrada)
        self.entrada.set_placeholder_text("Ingrese algo")

        self.button_save = Gtk.Button(label="Guardar")
        self.button_save.connect("clicked", self.save)                          
        self.box.append(self.button_save)

        self._native1 = self.dialog_save()                                                         
        self._native1.connect("response", self.on_file_save_response)   


    def on_dialog_response(self, dialog, response):
        if response == Gtk.ResponseType.OK:           
            dialog.close()   


    def save(self, button):
        self._native1.show()  


    def dialog_save(self): 
        return Gtk.FileChooserNative(title="Save File",
                                    # "self.main_window" is defined elsewhere as a Gtk.Window
                                    transient_for=self.get_root(),
                                    action=Gtk.FileChooserAction.SAVE,
                                    accept_label="_Save",
                                    cancel_label="_Cancel",
                                    )
    

    def on_file_save_response(self, native, response):

        if response == Gtk.ResponseType.ACCEPT:
            self.open_dialog()
            _path = native.get_file().get_path()
            print(_path)
            with open(_path, "w") as _file:
                _file.write(f'{self.entrada.get_text()}\n')


    def open_dialog(self):

        dialog = ExampleDialog(parent=self.get_root())                          
        dialog.connect("response", self.on_dialog_response)
        dialog.set_visible(True)  


class MyApp(Gtk.Application):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)

        self.connect('activate', self.on_activate)


    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


app = MyApp(application_id="com.example.GtkApplication")
app.run(sys.argv)
