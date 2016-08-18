#!/usr/bin/env python
# example base.py

import pygtk
pygtk.require('2.0')
import gtk

from wmctrl import Window


class Base:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.show()
        print Window.list()
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)


    def hello(self, widget, data=None):
        print "Hello World"


    def delete_event(self, widget, data=None):
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()
    def main(self):
        gtk.main()

print __name__
if __name__ == "__main__":
   base = Base()
   base.main()