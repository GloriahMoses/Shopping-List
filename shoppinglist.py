from user import User
shoppinglist = {}

class Shoppinglist(object):
	"""
    Class for shoppinglist functionionality
    """
	def __init__(self, title=None, description=None, owner=None ):
		""" Initializing variables"""
		self.title = title
		self.description = description
		self.owner = owner
		self.items_dict = {}
		
	def create(self, title, description, owner):
		"""create list method"""
		if description != ''and title != '':
			if title not in shoppinglist.keys():
				shoppinglist[title] = {'owner':owner, 'Description':description}
				return 8 #"Successfully created"
			else:
				return 10 #"List already exists"
		else:
			return "Fill in all the details"

	def add(self,title, item_name, quantity, budget):
			"""add items method and edit"""
			if item_name != '' and quantity !='' and budget !='':
				if title not in self.items_dict.keys():
					self.items_dict[title] = {item_name: [quantity, budget]}
					return 9
				else:
					self.items_dict[title][item_name] = [quantity, budget]
					return 9
			else:
				return 4
