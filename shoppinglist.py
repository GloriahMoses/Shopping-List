my_lists = {}
from user import User

class Shoppinglist(object):
	"""
    Class for user functionionality
    """

	def __init__(self, title=None, description=None, owner=None):
		""" Initializing variables"""
		self.title = title
		self.description = description
		self.owner = owner

	def create_list(self, title, description, owner):
		"""create list method"""
		if description != ''and title != '':
			if title not in my_lists.keys():
				my_lists[owner] ={'title': title,'description': description}
				print (my_lists)
				return 8 #"Successfully created"
			else:
				return "List already exists"
		else:
			return "Fill in all the details"

	


"""gg = Shoppinglist()
gilo.create_list ("gg", "B2S", "going to school")

def add_items(self, title, name, price, quantity):
		add items method
		if title != '' and name != '' and price != '' and quantity != '':
			self.items[title] = {name: [price, quantity]}
		else:
			return "Fill in all the details"
			"""