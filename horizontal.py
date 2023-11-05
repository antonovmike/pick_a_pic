import gi
import os
import random

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf

photos_names = []


class PhotoWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Pick a pic")
        self.set_border_width(0)
        self.set_default_size(800, 570)
        self.set_resizable(False)

        fixed = Gtk.Fixed()
        self.add(fixed)

        self.button = Gtk.Button(label="Random")
        self.button.set_size_request(450, 50)
        self.button.connect("clicked", self.on_button_clicked)
        fixed.put(self.button, 0, 0)

        self.answer = Gtk.Button(label="Answer")
        self.answer.set_size_request(450, 50)
        self.answer.connect("clicked", self.on_answer_clicked)
        fixed.put(self.answer, 400, 0)

        self.image1 = Gtk.Image()
        fixed.put(self.image1, 0, 50)

        self.label1 = Gtk.Label()
        fixed.put(self.label1, 0, 500)

        self.image2 = Gtk.Image()
        fixed.put(self.image2, 400, 50)

        self.label2 = Gtk.Label()
        fixed.put(self.label2, 400, 500)

        self.label1.set_xalign(0.5)
        self.label1.set_yalign(0.5)

        self.label2.set_xalign(0.5)
        self.label2.set_yalign(0.5)
        self.label1.set_size_request(450, 50)
        self.label2.set_size_request(450, 50)
        self.label1.set_max_width_chars(50)
        self.label2.set_max_width_chars(50)
        self.label1.set_valign(Gtk.Align.CENTER)
        self.label2.set_valign(Gtk.Align.CENTER)
        self.label1.set_justify(Gtk.Justification.CENTER)
        self.label2.set_justify(Gtk.Justification.CENTER)
        self.label1.set_line_wrap(True)
        self.label2.set_line_wrap(True)

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

    def file_names(self, file_name):
        file_name = file_name.replace(" - ", "\n")
        parts = file_name.split("\n")
        if len(parts) > 1:
            parts[1] = f'"{parts[1]}"'
        return "\n".join(parts)

    def on_answer_clicked(self, widget):
        global photos_names
        if photos_names:
            photo1 = self.file_names(photos_names[0])
            photo2 = self.file_names(photos_names[1])
            self.label1.set_markup("<span font='18'>{}</span>".format(photo1))
            self.label2.set_markup("<span font='18'>{}</span>".format(photo2))


win = PhotoWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
