import pygtk
pygtk.require('2.0')
import gobject
gobject.threads_init ()
import gtk,gio
import sys

# http://zetcode.com/tutorials/pygtktutorial/advancedwidgets/

actresses = [('jessica alba', 'pomona', '1981'), ('sigourney weaver', 'new york', '1949'),
	('angelina jolie', 'los angeles', '1975'), ('natalie portman', 'jerusalem', '1981'),
	('rachel weiss', 'london', '1971'), ('scarlett johansson', 'new york', '1984' )]

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
		#self.tree_view.insert_column_with_attributes(-1, "Name", gtk.CellRendererText())
		#self.tree_view.insert_column_with_attributes(-1, "Earnings", gtk.CellRendererText())
		#self.tree_view.insert_column_with_attributes(-1, "Due", gtk.CellRendererText())
		
		# Create Store
		#self.store = gtk.ListStore(str, str, str)
		#iterator = self.store.append(["Person 1","5","5"])
		#self.store.append(["Person 2","5","5"])
		#self.tree_view.set_model(self.store)
		
		
		
		
		self.store = self.create_model()
		self.tree_view.set_model(self.store)
		
		self.tree_view.set_rules_hint(True)
		
		self.create_columns(self.tree_view)
		
		
		
		self.window.show_all()
	
	
	def create_columns(self, treeView):
	
		rendererText = gtk.CellRendererText()
		column = gtk.TreeViewColumn("Name", rendererText, text=0)
		column.set_sort_column_id(0)	
		treeView.append_column(column)
		
		rendererText = gtk.CellRendererText()
		column = gtk.TreeViewColumn("Place", rendererText, text=1)
		column.set_sort_column_id(1)
		treeView.append_column(column)

		rendererText = gtk.CellRendererText()
		column = gtk.TreeViewColumn("Year", rendererText, text=2)
		column.set_sort_column_id(2)
		treeView.append_column(column)
	
	def create_model(self):
		store = gtk.ListStore(str, str, str)

		for act in actresses:
			store.append([act[0], act[1], act[2]])

		return store
	
	
	def destroy(self, widget, data=None):
		"""
		Quit on window close.
		"""
		gtk.main_quit()

if __name__ == "__main__":
	base = App()
	gtk.main()
