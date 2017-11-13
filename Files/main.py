#!/usr/bin/python

import gi
import Const
import os
gi.require_version("Gtk","3.0")

from Common import setScreenSize,createScrollbar,copyContentsFromFile,setBackgroundColor,on_cell_toggled
from gi.repository import Gtk

class main(Gtk.Window):
    def __init__(self):
        super(main, self).__init__(title=Const.TITLE)

        setScreenSize(self,Const.WIDTH_RATIO,Const.HEIGHT_RATIO1)

    def _getinstalledapplications(self):

        os.system("eopkg list-installed > installedPackages.txt")
        os.system("cat installedPackages.txt | grep -o ' -.*' > installedPackageDescription.txt")
        os.system("cat installedPackages.txt | awk '{gsub(/ -.*/,'True');print}' > installedPackageNames.txt ")

        installedPackageDescription = copyContentsFromFile("installedPackageDescription.txt")
        installedPackageName = copyContentsFromFile("installedPackageNames.txt")

        installationCheck = []
        background_color = []
        for i in range(len(installedPackageName)):
            installationCheck.append(True)
            background_color = setBackgroundColor(i)
            installedStore.append([installationCheck[i],installedPackageName[i].strip('\n'),installedPackageDescription[i].strip('\n'),background_color])


win = main()
installedStore = Gtk.ListStore(bool,str,str,str)
TreeListApplication = Gtk.TreeView(model=installedStore)
TreeScrollbar = createScrollbar(TreeListApplication)

win._getinstalledapplications()

win.connect("delete-event",Gtk.main_quit)

win.set_border_width(20)
vbox = Gtk.VBox(spacing=10)
win.add(vbox)
frame1 = Gtk.Frame()
vbox.add(frame1)

for i,column_title in enumerate(Const.COLUMN_HEADER):
    if i == 0:
        renderer_toggle = Gtk.CellRendererToggle()
        renderer_toggle.connect("toggled",on_cell_toggled)
        column = Gtk.TreeViewColumn(column_title,renderer_toggle,active=0)
    elif i > 0:
        renderertext = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn(column_title,renderertext,text=i)
        column.add_attribute(renderertext,"background",3)
    TreeListApplication.append_column(column)

frame1.add(TreeScrollbar)

win.show_all()
Gtk.main()


