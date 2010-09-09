import pygtk
pygtk.require('2.0')
import gobject
gobject.threads_init ()
import gtk,gio

class AssistantPage(gobject.GObject):
	
	title_side = "A page."
	title_top = "A top description."
	is_selected = False
	widget = gtk.DrawingArea()
	side_label = None
	
	def __init__(self):
		gobject.GObject.__init__(self)
	
	
