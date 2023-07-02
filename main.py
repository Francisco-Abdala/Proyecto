import sys
import gi
import matplotlib

gi.require_version('Gtk', '4.0')

from gi.repository import Gio, Gtk
from simulacion import Simulacion
from enfermedad import Enfermedad
from comunidad import Comunidad

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app = self.get_application()
        self.set_default_size(100, 200)
        header_bar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=header_bar)
        self.set_title("Simulación")

        menu_button_model = Gio.Menu()
        menu_button_model.append("About", "app.about")
        menu_button = Gtk.MenuButton.new()


        menu_button.set_icon_name(icon_name='open-menu-symbolic')
        menu_button.set_menu_model(menu_model=menu_button_model)
        header_bar.pack_end(child=menu_button)

        self.principal_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing= 10)
        self.info_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing= 10)

        self.principal_box.append(self.principal_box)

        # Botón para empezar la simualción
        self.start_button = Gtk.Button.new_with_label("Empezar simulación")
        self.start_button.connect("clicked",self.on_start_button_clicked)
        self.principal_box.append(self.start_button)

    def on_start_button_clicked(self, button):
        self.iniciar_simulacion()
        self.progreso.close()
    def iniciar_simulacion(self):

        infeccion_probable = 20
        promedio_pasos = 5
        mortalidad = 3
        enfermedad = Enfermedad(infeccion_probable,
                                promedio_pasos, mortalidad)
        

        num_ciudadanos = 100
        infectados = 2
        media_conexion_fisica = 30
        probabilidad_conexion_fisica = 50
        comunidad = Comunidad(num_ciudadanos, enfermedad, infectados,
                            media_conexion_fisica, probabilidad_conexion_fisica)
        

        dias_simulacion = 50
        simulacion = Simulacion(dias_simulacion, comunidad, enfermedad)
        simulacion.simular()

class MyApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id='cl.com.Example',
                        flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.create_action("about", self.on_about_action)


    def on_about_action(self, action, param):
        about = Gtk.AboutDialog.new()
        about.set_authors(["Francisco Abdala", "Amanda Pérez"])
        about.set_program_name("Simulación")
        about.set_copyright("Ingeniería Civil en Bioinformática")
        about.set_visible(True)


    def do_activate(self):
        active_window = self.props.active_window
        if active_window:
            active_window.present()
        else:
            self.win = MainWindow(application=self)
            self.win.present()


    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f'app.{name}', shortcuts)


if __name__ == '__main__':
    app = MyApp()
    app.run(sys.argv)