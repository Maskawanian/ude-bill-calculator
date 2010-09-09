import pygtk
pygtk.require('2.0')
import gobject
gobject.threads_init ()
import gtk,gio

class Assistant(gobject.GObject):
	
	__gsignals__ = {
		"new-page" : (gobject.SIGNAL_RUN_LAST, gobject.TYPE_NONE, (gobject.TYPE_PYOBJECT,)),
	}
	
	builder = None
	__window = None
	__vbox_side_title = None
	__label_top_title = None
	__button_back = None
	__button_continue = None
	__nb = None
	__pages = []
	
	def __init__(self):
		gobject.GObject.__init__(self)
		
		self.builder = gtk.Builder()
		
		self.builder.add_from_file("assistant.glade")
		self.window = self.builder.get_object("mainWindow")
		self.__vbox_side_title = self.builder.get_object("vboxSideTitle")
		self.__label_top_title = self.builder.get_object("labelTopTitle")
		self.__nb = self.builder.get_object("notebook")
		self.__button_back = self.builder.get_object("buttonBack")
		self.__button_continue = self.builder.get_object("buttonContinue")
		
		self.__button_back.connect("clicked", self.__click_back)
		self.__button_continue.connect("clicked", self.__click_continue)
		self.__nb.connect("switch-page",self.__nb_change_current_page_cb)
		
	def show(self):
		# Build
		self.__pages[0].is_selected = True
		for page in self.__pages:
			
			# Side Label
			page.side_label = gtk.Label()
			page.side_label.set_alignment(0,0.5)
			page.side_label.set_markup(page.title_side)
			
			self.__vbox_side_title.pack_start(page.side_label, expand=False, fill=True, padding=0)
			
			# Notebook Page
			self.__nb.append_page(page.widget,gtk.Label("Page"))
		
		self.__rejigger()
		
		# Show
		self.window.show_all()
		
		
		
	def add_page(self,page):
		self.__pages.append(page)
		
		
		
	def __rejigger(self):
		for page in self.__pages:
			if page.is_selected:
				page.side_label.set_markup("<b>"+page.title_side+"</b>")
			else:
				page.side_label.set_markup(page.title_side)
	
	def __nb_change_current_page_cb(self, widget, data, pagenum):
		self.__button_back.set_sensitive(pagenum!=0)
		print "__nb_change_current_page_cb"
	
	def __click_back(self, widget, data=None):
		self.__nb.prev_page()
	
	def __click_continue(self, widget, data=None):
		self.__nb.next_page()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
