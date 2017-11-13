import gi
import Const
gi.require_version("Gtk","3.0")

from gi.repository import Gtk, Gdk

def setScreenSize(self, widthRatio, heightRatio):
    Screen = Gdk.Screen.get_default()
    self.set_size_request(Screen.get_width() * widthRatio, Screen.get_height() * heightRatio)

# Copy the Contents of the file from a File to a List
def copyContentsFromFile(fileName):
    with open(fileName, "r") as file1:
        value = []
        for line in file1:
            value.append(line)
    return value

def setBackgroundColor(i):
    if i % 2 == 0:
        background_color = Const.BGCOLOR1
    else:
        background_color = Const.BGCOLOR2
    return background_color

def createScrollbar(Treeview):
    Scrollbar = Gtk.ScrolledWindow()
    Scrollbar.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
    Scrollbar.set_vexpand(True)
    Scrollbar.add(Treeview)
    return Scrollbar

def on_cell_toggled(widget,path):
    pass