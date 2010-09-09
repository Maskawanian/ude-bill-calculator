import pygtk
pygtk.require('2.0')
import gobject
gobject.threads_init ()
import gtk,gio
import sys

# http://zetcode.com/tutorials/pygtktutorial/advancedwidgets/

class App:
	builder = None
	window = None
	tree_view = None
	store = None
	
	def __init__(self):
		self.builder = gtk.Builder()
		self.builder.add_from_file("window.glade")
		self.window = self.builder.get_object("mainWindow")
		self.window.connect("destroy", self.destroy)
		
		# Create View
		self.tree_view = self.builder.get_object("peopleList")
		
		renderer = gtk.CellRendererText()
		renderer.set_property("editable",True)
		column = gtk.TreeViewColumn("Name", renderer, text=0)
		column.set_sort_column_id(0)	
		self.tree_view.append_column(column)
		
		renderer = gtk.CellRendererText()
		renderer.set_property("editable",True)
		column = gtk.TreeViewColumn("Earnings", renderer, text=1)
		column.set_sort_column_id(1)
		self.tree_view.append_column(column)
		
		# Create Store
		self.store = gtk.ListStore(str, str)
		self.store.append(["Person 1","5"])
		self.store.append(["Person 2","5"])
		self.tree_view.set_model(self.store)
		
		
		
		self.tree_view.set_model(self.store)
		
		self.window.show_all()
	
	
	
	
	def destroy(self, widget, data=None):
		"""
		Quit on window close.
		"""
		gtk.main_quit()

if __name__ == "__main__":
	base = App()
	gtk.main()
