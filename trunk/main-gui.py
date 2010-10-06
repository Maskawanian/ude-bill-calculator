import pygtk
pygtk.require('2.0')
import gobject
gobject.threads_init ()
import gtk,gio
import sys
import re

from Assistant import Assistant
from AssistantPage import AssistantPage
from Calculator import Person,Calculator
# http://zetcode.com/tutorials/pygtktutorial/advancedwidgets/

class App:
	
	
	builder = None
	window = None
	bill_entry = None
	bill_validation_tip_hbox = None
	tree_view = None
	add_button = None
	remove_button = None
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
		self.asnt.connect("validate-page",self.__validate_page_cb)
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
		self.bill_validation_tip_hbox = self.builder.get_object("billValidationTipHBox")
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
		
		self.add_button = self.builder.get_object("addButton")
		self.add_button.connect("clicked",self.p2_add_row)
		self.remove_button = self.builder.get_object("removeButton")
		self.remove_button.connect("clicked",self.p2_remove_row)
		
		self.res_tv = self.builder.get_object("resultTextview")
		
		
		# Create Store
		self.store = gtk.ListStore(str, str)
		for person in self.people:
			self.store.append(person)
		
		self.tree_view.set_model(self.store)
		
		
		
		self.tree_view.set_model(self.store)
		self.asnt.show()
	
	
	
	
	
	
	
	
	
	def p2_add_row(self,widget,data=None):
		self.store.append(["New Party","0"])
		self.people.append(["New Party","0"])
		
		iter = self.store.get_iter_from_string(str(len(self.people)-1))
		path = self.store.get_path(iter)
		self.tree_view.set_cursor(path,self.col1,True)
	
	def p2_remove_row(self,widget,data=None):
		
		selection = self.tree_view.get_selection()
		model, iter = selection.get_selected()
		if None != iter:
			path = model.get_path(iter)
			row = path[0] # We can only select 1 so just access the first index
			del self.people[row]
			self.store.remove(iter)
	
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
			charge = float(self.bill_entry.get_text())
			
			calc_people = []
			for person in self.people:
				calc_people.append(Person(person[0],person[1]))
			
			calc = Calculator()
			calc.people = calc_people
			calc.charge = charge
			calc.calculate()
			
			str = ""
			
			
			str+= "Total income including all parties: ${0:03.2f}\n\n".format(calc.total_income)
			
			for p in calc.people:
				str+= "Amount due by {0} whose income is ${1:03.2f} is ${2:03.2f}.\n".format(p.name,p.income,p.due)
			
			str+= "\nEach party is paying {0:03.2f}% of their income.".format(calc.due_percent)
			
			
			
			
			
			
			
			
			buf = self.res_tv.get_buffer()
			buf.set_text(str)
		
		print "__change_page_cb",page
	def __validate_page_cb(self,assistant,page):
		if page == self.asnt_p1:
			return self.__validate_page1()
		
		
		return self.asnt.VALIDATE_SUCCESS
	
	def __validate_page1(self):
		str = self.bill_entry.get_text()
		if str == "":
			self.bill_entry.modify_base(gtk.STATE_NORMAL,gtk.gdk.color_parse("#FF7F7F"))
			self.bill_validation_tip_hbox.show()
			return self.asnt.VALIDATE_FAIL
		
		notnum = re.compile(r"[^0-9\.]")
		if notnum.search(str):
			self.bill_entry.modify_base(gtk.STATE_NORMAL,gtk.gdk.color_parse("#FF7F7F"))
			self.bill_validation_tip_hbox.show()
			return self.asnt.VALIDATE_FAIL
		
		self.bill_entry.modify_base(gtk.STATE_NORMAL,None)
		self.bill_validation_tip_hbox.hide()
		return self.asnt.VALIDATE_SUCCESS
	
	
	
	
	
	
	
	
	
	
	
	
	
	






































if __name__ == "__main__":
	base = App()
	gtk.main()
