import pygtk
pygtk.require('2.0')
import gobject
gobject.threads_init ()
import gtk,gio
import sys
from Assistant import Assistant
from AssistantPage import AssistantPage
# http://zetcode.com/tutorials/pygtktutorial/advancedwidgets/

class App:
	assistant = None
	
	builder = None
	window = None
	tree_view = None
	store = None
	
	def __init__(self):
		
		assistant = Assistant()
		
		self.builder = gtk.Builder()
		self.builder.add_from_file("window.glade")
		
		page1 = AssistantPage()
		page1.title_side = "Bill"
		page1.title_top = "Enter Bill Information:"
		page1.widget = self.builder.get_object("vboxPage1")
		assistant.add_page(page1)
		
		page2 = AssistantPage()
		page2.title_side = "Finances"
		page2.title_top = "Enter the Party's Financial Information:"
		page2.widget = self.builder.get_object("vboxPage2")
		assistant.add_page(page2)
		
		page3 = AssistantPage()
		page3.title_side = "Results"
		page3.title_top = "Results:"
		page3.widget = self.builder.get_object("scrolledwindowPage3")
		assistant.add_page(page3)
		
		
		
		
		assistant.window.connect("destroy", self.destroy)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
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
		assistant.show()
	
	
	
	
	def destroy(self, widget, data=None):
		"""
		Quit on window close.
		"""
		gtk.main_quit()

if __name__ == "__main__":
	base = App()
	gtk.main()
