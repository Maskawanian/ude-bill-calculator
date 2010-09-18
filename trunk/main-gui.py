import pygtk
pygtk.require('2.0')
import gobject
gobject.threads_init ()
import gtk,gio
import sys
from Assistant import Assistant
from AssistantPage import AssistantPage
from Calculator import Person,Calculator
# http://zetcode.com/tutorials/pygtktutorial/advancedwidgets/

class App:
	
	
	builder = None
	window = None
	bill_entry = None
	tree_view = None
	col1 = None
	col1_rend = None
	col2 = None
	col2_rend = None
	store = None
	res_tv = None
	
	asnt = None
	asnt_p1 = None
	asnt_p2 = None
	asnt_p3 = None
	people = []
	
	
	def __init__(self):
		
		self.asnt = Assistant()
		self.asnt.connect("switch-page",self.__switch_page_cb)
		self.asnt.window.connect("destroy", self.destroy)
		
		self.builder = gtk.Builder()
		self.builder.add_from_file("window.glade")
		
		self.asnt_p1 = AssistantPage()
		self.asnt_p1.title_side = "Bill"
		self.asnt_p1.title_top = "Enter Bill Information:"
		self.asnt_p1.widget = self.builder.get_object("vboxPage1")
		self.asnt.add_page(self.asnt_p1)
		
		self.asnt_p2 = AssistantPage()
		self.asnt_p2.title_side = "Finances"
		self.asnt_p2.title_top = "Enter the Party's Financial Information:"
		self.asnt_p2.widget = self.builder.get_object("vboxPage2")
		self.asnt.add_page(self.asnt_p2)
		
		self.asnt_p3 = AssistantPage()
		self.asnt_p3.title_side = "Results"
		self.asnt_p3.title_top = "Results:"
		self.asnt_p3.widget = self.builder.get_object("scrolledwindowPage3")
		self.asnt.add_page(self.asnt_p3)
		
		
		
		
		
		
		
		
		
		
		
		
		self.people.append(["Person 1","5"])
		self.people.append(["Person 2","5"])
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		# Create View
		self.bill_entry = self.builder.get_object("billEntry")
		#self.bill_entry.modify_base(gtk.STATE_NORMAL,gtk.gdk.color_parse("#FF7F7F"))
		
		
		
		self.tree_view = self.builder.get_object("peopleList")
		
		self.col1_rend = gtk.CellRendererText()
		self.col1_rend.connect("edited",self.col1_edited)
		self.col1_rend.set_property("editable",True)
		self.col1 = gtk.TreeViewColumn("Name", self.col1_rend, text=0)
		self.col1.set_sort_column_id(0)
		self.tree_view.append_column(self.col1)
		
		self.col2_rend = gtk.CellRendererText()
		self.col2_rend.connect("edited",self.col2_edited)
		self.col2_rend.set_property("editable",True)
		self.col2 = gtk.TreeViewColumn("Earnings", self.col2_rend, text=1)
		self.col2.set_sort_column_id(1)
		self.tree_view.append_column(self.col2)
		
		self.res_tv = self.builder.get_object("resultTextview")
		
		
		# Create Store
		self.store = gtk.ListStore(str, str)
		for person in self.people:
			self.store.append(person)
		
		self.tree_view.set_model(self.store)
		
		
		
		self.tree_view.set_model(self.store)
		self.asnt.show()
	
	def col1_edited(self,renderer,path,newtext):
		iter = self.store.get_iter_from_string(path)
		self.store.set(iter,0,newtext)
		self.people[int(path)][0] = newtext
	
	def col2_edited(self,renderer,path,newtext):
		iter = self.store.get_iter_from_string(path)
		self.store.set(iter,1,newtext)
		self.people[int(path)][1] = newtext
	
	def destroy(self, widget, data=None):
		"""
		Quit on window close.
		"""
		gtk.main_quit()
	
	def __switch_page_cb(self,assistant,page):
		if page == self.asnt_p1:
			pass
		elif page == self.asnt_p2:
			pass
		elif page == self.asnt_p3:
			
			calc_people = []
			for person in self.people:
				calc_people.append(Person(person[0],person[1]))
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			buf = self.res_tv.get_buffer()
			buf.set_text(repr(self.people))
		
		print "__change_page_cb",page







































if __name__ == "__main__":
	base = App()
	gtk.main()
