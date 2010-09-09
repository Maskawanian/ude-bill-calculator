import pygtk
pygtk.require('2.0')
import gobject
gobject.threads_init ()
import gtk,gio

class Assistant(gobject.GObject):
	
	builder = None
	__window = None
	__vbox_side_title = None
	__pages = []
	
	def __init__(self):
		gobject.GObject.__init__(self)
		
		self.builder = gtk.Builder()
		
		self.builder.add_from_file("assistant.glade")
		self.__window = self.builder.get_object("mainWindow")
		self.__vbox_side_title = self.builder.get_object("vboxSideTitle")
		
		
		
	def show(self):
		# Build
		for page in self.__pages:
			side_label = gtk.Label()
			side_label.set_alignment(0,0.5)
			if page.is_selected:
				side_label.set_markup("<b>"+page.title_side+"</b>")
			else:
				side_label.set_markup(page.title_side)
			
			page.side_label = side_label
			self.__vbox_side_title.pack_start(side_label, expand=False, fill=True, padding=0)
			
			
		
		
		# Show
		self.__window.show_all()
		
		
		
	def add_page(self,page):
		self.__pages.append(page)
		
		
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
