import sys
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gio, GObject, Gtk

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

        self.set_default_size(200, 100)
        self.set_title("Ejercicio Dropdown")
        self.app_ = self.get_application()

        self.box = Gtk.Box.new( Gtk.Orientation.VERTICAL,5)
        self.set_child(self.box)

        self.search_text = ''

        datos = ["Ricardiño","Mohammed","Ci","Alejandroide"]


        self.model_dropdown = Gio.ListStore(item_type=DropDown)
        self.sort_model_widget  = Gtk.SortListModel(model=self.model_dropdown) 
        self.filter_model_widget = Gtk.FilterListModel(model=self.sort_model_widget)
        self.filter_widget = Gtk.CustomFilter.new(self._do_filter_widget_view, self.filter_model_widget)
        self.filter_model_widget.set_filter(self.filter_widget)

        for i in datos:
            self.model_dropdown.append(DropDown(name=i))

        factory_dropdown = Gtk.SignalListItemFactory()
        factory_dropdown.connect("setup", self._on_factory_dropdown_setup)
        factory_dropdown.connect("bind", self._on_factory_dropdown_bind)


        self.dropdown = Gtk.DropDown(model=self.filter_model_widget, factory=factory_dropdown)
        self.dropdown.set_enable_search(True)
        self.box.append(self.dropdown)
        self.dropdown.connect("notify::selected-item", self._on_selected_dropdown)
        

        self.button = Gtk.Button.new_with_label(label="imprimir")
        self.button.connect("clicked",self.on_print_button_clicked,self.dropdown)
        self.box.append(self.button)

        search_entry_widget = self._get_search_entry_widget(self.dropdown)
        search_entry_widget.connect("search-changed", self._on_search_widget_changed)

    def _get_search_entry_widget(self, dropdown1):
        ayuda = dropdown1.get_last_child()
        box = ayuda.get_child()
        box1 = box.get_first_child()
        search_entry = box1.get_first_child() # Gtk.SearchEntry
        return search_entry


    def _on_search_widget_changed(self, search_entry):
        self.search_text = search_entry.get_text()
        self.filter_widget.changed(Gtk.FilterChange.DIFFERENT)

    def _do_filter_widget_view(self, item, filter_list_model):
        return self.search_text.upper() in item.name.upper()

    def _on_factory_dropdown_setup(self, factory, list_item):
        box = Gtk.Box(spacing=3, orientation=Gtk.Orientation.HORIZONTAL)
        label = Gtk.Label()
        box.append(label)
        list_item.set_child(box)

    def _on_factory_dropdown_bind(self, factory, list_item):
        box = list_item.get_child()
        label = box.get_first_child()
        method = list_item.get_item()
        label.set_text(method.name)

    def on_print_button_clicked(self,p_button, dropdown):
        print(dropdown.get_selected_item().name)

    def _on_selected_dropdown(self, dropdown, data):
        widget = dropdown.get_selected_item()
        print("Ha selecionado a", widget.name)

class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def do_activate(self):
        active_window = self.props.active_window
        if active_window:
            active_window.present()
        else:
            self.win = MainWindow(application=self)
            self.win.present()

app = MyApp(application_id="com.myapplicationexample",flags= Gio.ApplicationFlags.FLAGS_NONE)
app.run(sys.argv)