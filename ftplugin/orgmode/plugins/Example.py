from orgmode import echo, ORGMODE
from orgmode.menu import Submenu, HorizontalLine, ActionEntry
from orgmode.keybinding import Keybinding
from orgmode.heading import Heading, DIRECTION_FORWARD, DIRECTION_BACKWARD

import vim

class Example(object):
	""" Example plugin """

	def __init__(self):
		""" Initialize plugin """
		object.__init__(self)
		# menu entries this plugin should create
		self.menu = ORGMODE.menu + Submenu('Example')

		# key bindings for this plugin
		# key bindings are also registered through the menu so only additional
		# bindings should be put in this variable
		self.keybindings = []
	
	def register(self):
		"""
		Registration of plugin. Key bindings and other initialization should be done.
		"""
		# an Action menu entry which binds "keybinding" to action ":action"
		self.menu + ActionEntry('Action', Keybinding('keybinding', ':action'))
