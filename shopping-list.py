from user import users
shopping_lists = {}

class Shoppinglist(object):
	"""
    Class for user functionionality
    """

	def __init__(self, title=None, description=None, owner=None):
		""" Initializing variables"""
		self.title = title
		self.description = description
		self.owner = users.email
		self.my_lists = {}
		self.items = {}

	def create_list(self, title, description, owner):
		"""create list method"""
		if description != ''and title != '':
			if title not in my_lists.keys():
				self.my_lists[owner] =[title, description]
				print (my_lists)
				return "Successfully created"
			else:
				return "List already exists"
		else:
			return "Fill in all the details"

	def add_items(self, title, name, price, quantity):
		"""add items method"""
		if title != '' and name != '' and price != '' and quantity != '':
			self.items[title] = {name: [price, quantity]}
		else:
			return "Fill in all the details"


"""gg = Shoppinglist()
gilo.create_list ("gg", "B2S", "going to school")"""

