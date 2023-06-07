import sys 
import gi
from rdkit import Chem
import pathlib


gi.require_version("Gtk","4.0")

from gi.repository import Gio,Gtk,GObject


class DropDown(GObject.Object):
    __gtype_name__ = "DropDown"

    def __init__(self, name):
        super().__init__()
        self._name = name

    @GObject.Property
    def name(self):
        return self._name
    

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 

        barra = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=barra)

        menu_button_model = Gio.Menu()


        menu_button_model.append("About" , 'app.about')

        boton_menu = Gtk.MenuButton.new()

        boton_menu.set_icon_name(icon_name='open-menu-symbolic')

        boton_menu.set_menu_model(menu_model=menu_button_model)

        barra.pack_end(child=boton_menu)

        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL,spacing= 10)
        self.boton = Gtk.Button(label= "Mostrar carpeta")
        self.boton.connect('clicked', self.open)     

        self.set_child(self.box)    
        self.box.append(self.boton)


        self._native2 = self.dialog_open()                                       
        self._native2.connect("response", self.on_file_open_response)            

    def _do_filter_widget_view(self, item, filter_list_model):
        return self.search_text.upper() in item.name.upper()
    


    def _on_factory_dropdown_bind(self, factory, list_item):
        box = list_item.get_child()
        label = box.get_first_child()
        method = list_item.get_item()
        label.set_text(method.name)
    
    def _on_factory_dropdown_setup(self, factory, list_item):
        box = Gtk.Box(spacing=3, orientation=Gtk.Orientation.HORIZONTAL)
        label = Gtk.Label()
        box.append(label)
        list_item.set_child(box)



    def open(self, button):
        self._native2.show()


    def _on_selected_dropdown(self, dropdown, data):
        widget = dropdown.get_selected_item()
        img = Draw.MolToImage(widget)
        self.box.append(img)

    def on_file_open_response(self, native, response):
        if response == Gtk.ResponseType.ACCEPT:
            _path = native.get_file().get_path()

    
        directorio = _path
        directorio =  pathlib.Path(directorio)

        
        archivos_mol = [fichero.name[::-4]  for fichero in directorio.iterdir() if directorio.glob("*.mol")]
        self.model_dropdown = Gio.ListStore(item_type=DropDown)


        self.sort_model_widget  = Gtk.SortListModel(model=self.model_dropdown) 

        self.search_text = ''
        self.filter_model_widget = Gtk.FilterListModel(model=self.sort_model_widget)


        self.filter_widget = Gtk.CustomFilter.new(self._do_filter_widget_view, self.filter_model_widget)


        self.filter_model_widget.set_filter(self.filter_widget)
        self.model_dropdown.append(DropDown(name="Seleccione su molécula:"))


        for i in archivos_mol:
            self.model_dropdown.append(DropDown(name=i))


        factory_dropdown = Gtk.SignalListItemFactory()
        factory_dropdown.connect("setup", self._on_factory_dropdown_setup)


        factory_dropdown.connect("bind", self._on_factory_dropdown_bind)

        self.dropdown = Gtk.DropDown(model=self.filter_model_widget, factory=factory_dropdown)
        self.dropdown.set_enable_search(True)


        self.box.append(self.dropdown)
        self.dropdown.connect("notify::selected-item", self._on_selected_dropdown)

      
    def dialog_open(self): 
        return Gtk.FileChooserNative(title="Open File",
                                    transient_for=self.get_root(),
                                    action=Gtk.FileChooserAction.SELECT_FOLDER,
                                    accept_label="_Open",
                                    cancel_label="_Cancel",
                                    )

        
    

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
        self.ayuda.set_authors(["Francisco Abdala"])
        self.ayuda.set_program_name("Lab 3")
        self.ayuda.set_comments("Este es un trabajo para programación avanzada")
        self.ayuda. set_visible(True)

    def exit_app(self, action, param):
        self.quit()

    def create_action(self, name, callback, shortcuts=None):
        action = Gio.SimpleAction.new(name, None)
        action.connect('activate', callback)
        self.add_action(action)
        if shortcuts:
            self.set_accels_for_action(f'app.{name}', shortcuts)


if __name__ == '__main__':
    import sys

    app = App()
    app.run(sys.argv)
