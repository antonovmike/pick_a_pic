import gi
import os
import random

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf


photos_names = []


class PhotoWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Pick a pic")
        self.set_border_width(10)
        self.set_default_size(906, 540)
        self.set_resizable(False)

        vbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.add(vbox)

        self.button = Gtk.Button(label="Random")
        self.button.set_property("width-request", 100)
        self.button.connect("clicked", self.on_button_clicked)
        vbox.pack_start(self.button, True, True, 0)

        self.answer = Gtk.Button(label="Answer")
        self.answer.set_property("width-request", 100)
        self.answer.connect("clicked", self.on_answer_clicked)
        vbox.pack_start(self.answer, True, True, 0)

        vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox.pack_start(vbox1, True, True, 0)

        self.image1 = Gtk.Image()
        vbox1.pack_start(self.image1, True, True, 0)

        self.label1 = Gtk.Label()
        vbox1.pack_start(self.label1, True, True, 0)

        vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        vbox.pack_start(vbox2, True, True, 0)

        self.image2 = Gtk.Image()
        vbox2.pack_start(self.image2, True, True, 0)

        self.label2 = Gtk.Label()
        vbox2.pack_start(self.label2, True, True, 0)

        self.label1.set_size_request(450, 50)
        self.label2.set_size_request(450, 50)

    def on_button_clicked(self, widget):
        global photos_names
        photos_names.clear()
        photos = os.listdir('photos')
        photo1 = random.choice(photos)
        photo2 = random.choice(list(set(photos) - set([photo1])))

        photos_names.append(os.path.splitext(photo1)[0])
        photos_names.append(os.path.splitext(photo2)[0])

        pixbuf1 = GdkPixbuf.Pixbuf.new_from_file(f'photos/{photo1}')
        scaled_pixbuf1 = pixbuf1.scale_simple(450, 450, GdkPixbuf.InterpType.BILINEAR)
        pixbuf2 = GdkPixbuf.Pixbuf.new_from_file(f'photos/{photo2}')
        scaled_pixbuf2 = pixbuf2.scale_simple(450, 450, GdkPixbuf.InterpType.BILINEAR)

        self.image1.set_from_pixbuf(scaled_pixbuf1)
        self.image2.set_from_pixbuf(scaled_pixbuf2)
        self.label1.set_text('')
        self.label2.set_text('')

    def on_answer_clicked(self, widget):
        global photos_names
        if photos_names:
            photo1 = photos_names[0]
            photo2 = photos_names[1]
            self.label1.set_text(photo1)
            self.label2.set_text(photo2)


win = PhotoWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
