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

        self.set_default_size(800,250)
        self.set_title("Simulación")
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing= 10)
        self.set_child(self.box)    

        self.grid1 = Gtk.GridView()
        self.box.append(self.grid1)
        self.button_save = Gtk.Button(label="Empezar simulación")
        self.button_save.connect("clicked", self.on_start_button_clicked)                          
        self.box.append(self.button_save)


        
    def on_start_button_clicked(self, button):
        self.iniciar_simulacion()
        self.progreso.close()
        self.show_mensaje_inicio()

    def iniciar_simulacion(self):
        infeccion_probable = 20
        promedio_pasos = 5
        muerte = 3
        virus = Enfermedad(infeccion_probable,
                                promedio_pasos, muerte)
        
        poblacion = 100000
        infectados = 2
        media_conexion_fisica = 30
        probabilidad_conexion_fisica = 50
        ciudad = Comunidad(poblacion, virus, infectados,
                            media_conexion_fisica, probabilidad_conexion_fisica)
        

        dias = 50
        simulacion = Simulacion(ciudad, virus,dias)
        simulacion.comienzo()

class MyApp(Gtk.Application):

    def __init__(self):
        super().__init__(application_id='cl.com.Example',
                         flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.create_action('quit', self.exit_app, ['<primary>q'])
        self.create_action('about', self.on_about_action)


    def do_activate(self):
        win = self.props.active_window
        if not win:
            win = MainWindow(application=self)
        win.present()

    def do_startup(self):
        Gtk.Application.do_startup(self)

    def do_shutdown(self):
        Gtk.Application.do_shutdown(self)

    def exit_app(self, action, param):
        self.quit()

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f'app.{name}', shortcuts)


    def on_about_action(self, action, param):
        about = Gtk.AboutDialog.new()
        about.set_authors(["Francisco Abdala", "Amanda Pérez"])
        about.set_program_name("Simulación")
        about.set_copyright("Ingeniería Civil en Bioinformática")
        about.set_visible(True)

if __name__ == '__main__':
    app = MyApp()
    app.run(sys.argv)
