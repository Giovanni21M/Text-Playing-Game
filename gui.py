import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Text Playing Game")
        self.set_border_width(10)
        self.set_size_request(400, 350)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        box.set_homogeneous(False)

        vboxUp = Gtk.Box(spacing=20)
        vboxUp.set_homogeneous(False)
        vboxBot = Gtk.Box(spacing=20)
        vboxBot.set_homogeneous(False)

        hboxLeft = Gtk.Box(spacing=20)
        hboxLeft.set_homogeneous(False)
        hboxRight = Gtk.Box(spacing=20)
        hboxRight.set_homogeneous(False)

        box.pack_start(vboxUp, True, True, 0)
        box.pack_start(vboxBot, True, True, 0)

        vboxBot.pack_start(hboxLeft, True, True, 0)
        vboxBot.pack_start(hboxRight, True, True, 0)

        label = Gtk.Label()
        label.set_text("What is your name brave soul?")
        label.set_justify(Gtk.Justification.FILL)
        vboxUp.pack_start(label, True, True, 0)

        self.entry = Gtk.Entry()
        hboxLeft.pack_start(self.entry, True, True, 0)

        self.button = Gtk.Button(label="Next")
        self.button.connect("clicked", self.button_clicked)
        hboxRight.pack_start(self.button, True, True, 0)

        self.add(box)

    def button_clicked(self, widget):
        print("Hello")
 

win = MainWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
