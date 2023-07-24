#Importa lo que se usará en el código

#Francisco Abdala,Amanda Perez
import sys
import gi
import matplotlib

gi.require_version('Gtk', '4.0')

from gi.repository import Gio, Gtk
from time import sleep
from simulacion import Simulacion
from enfermedad import Enfermedad
from comunidad import Comunidad
from vacuna_a import Vacuna_A
from vacuna_b import Vacuna_B
from vacuna_c import Vacuna_C

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Determina el tamaño y titulo de la ventana creada
        self.set_title("Simulación")

        #Crea un header bar
        barra = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=barra)
        self.set_title("Simulación")


        #Crea el botón para el about que se encuentra en el header bar
        menu_button_model = Gio.Menu()
        menu_button_model.append("About" , 'app.about')
        boton_menu = Gtk.MenuButton.new()
        boton_menu.set_icon_name(icon_name='open-menu-symbolic')
        boton_menu.set_menu_model(menu_model=menu_button_model)
        barra.pack_end(child=boton_menu)

        #Creación de una caja
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing= 10)
        self.set_child(self.box)    

        #Creación de un grid
        self.grid1 = Gtk.GridView()
        self.box.append(self.grid1)

        #Creación del botón que se utilizará para el comienzo de la simulación
        self.button = Gtk.Button(label="Empezar simulación")
        self.button.connect("clicked", self.on_start_button_clicked)                          
        self.box.append(self.button)

    #Acción del botón
    def on_start_button_clicked(self, button):
        self.iniciar_simulacion()

    #Función que esta sujeta al botón de comienzo
    def iniciar_simulacion(self):
        #Se les pasa los parámetros para la clase Enfermedad
        infeccion_probable = 0.02   
        promedio_pasos = 10
        muerte = 2
        virus = Enfermedad(infeccion_probable,
                                promedio_pasos,muerte)
        #Se les pasa los parámetros para la clase Comunidad
        poblacion = 1000
        infectados = 7
        media_conexion_fisica = 7
        probabilidad_conexion_fisica = 40
        ayuda = int(poblacion * 0.4)
        vacuna1 = Vacuna_A(ayuda)
        vacuna2 = Vacuna_B(ayuda)
        vacuna3 = Vacuna_C(ayuda)
        ciudad = Comunidad(poblacion, virus, infectados,
                            media_conexion_fisica, probabilidad_conexion_fisica)
        ciudad.set_vacuna(vacuna1)
        ciudad.set_vacuna(vacuna2)
        ciudad.set_vacuna(vacuna3)
        #Se les pasa los parámetros para la clase Simulación
        dias = 40
        simulacion = Simulacion(ciudad, virus,dias)
        simulacion.comienzo()

#Clase aplicación
class App(Gtk.Application):

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

    def on_about_action(self, action, param):
        self.ayuda = Gtk.AboutDialog.new()
        self.ayuda.set_authors(["Francisco Abdala", "Amanda Pérez"])
        self.ayuda.set_program_name("Proyecto")
        self.ayuda.set_comments("Este es el proyecto para programación avanzada")
        self.ayuda.set_visible(True)

    def exit_app(self, action, param):
        self.quit()

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f'app.{name}', shortcuts)

#Da inicio a la ventana
if __name__ == '__main__':
    app = App()
    app.run(sys.argv)
