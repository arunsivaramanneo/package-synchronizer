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

        package_count = len(installedPackageName)
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

list_box = Gtk.VPaned()
win.add(list_box)
win.set_border_width(20)
packageframe = Gtk.Frame()
list_box.set_position(50)
list_box.add1(packageframe)
grid = Gtk.Grid()
frame1 = Gtk.Frame()
list_box.add2(frame1)
label = Gtk.Label()
label.set_text("Available Package Syncs :")
grid.attach(label,1,1,1,1)
grid.set_border_width(5)
grid.set_column_spacing(20)
packageframe.add(grid)
sync_store = Gtk.ListStore(str)
package_combobox = Gtk.ComboBox.new_with_model(sync_store)
sync_store.append(["Currently Installed Packages"])
sync_store.append(["Insalled Packages as on : 01-Nov"])
renderer_combobox = Gtk.CellRendererText()
package_combobox.pack_start(renderer_combobox,True)
package_combobox.add_attribute(renderer_combobox,"text",0)
package_combobox.set_active(0)
grid.attach_next_to(package_combobox,label,Gtk.PositionType.RIGHT,5,1)


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


