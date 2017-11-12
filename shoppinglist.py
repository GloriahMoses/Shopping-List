from user import User

shoppinglists = {}
items_dict = {}

class Shoppinglist(object):

	"""
    Class for shoppinglist functionionality
    """
	def __init__(self, title=None, description=None, owner=None ):
		""" Initializing variables"""
		self.title = title
		self.description = description
		self.owner = owner
		
	def create(self, title, description, owner):
		"""create list method"""
		if description != ''and title != '':
			if title not in shoppinglists.keys():
				shoppinglists[title] = {'owner':owner, 'Description':description}
				return 8 #"Successfully created"
			else:
				return 10 #"List already exists"
		else:
			return "Fill in all the details"

	def add(self,title, item_name, quantity, budget):
			"""add items method and edit"""
			if item_name != '' and quantity !='' and budget !='':
				if title not in items_dict.keys():
					items_dict[title] = {item_name: [quantity, budget]}
					print(items_dict)
					return 9
				else:
					items_dict[title][item_name] = [quantity, budget]
					print(items_dict)
					return 9
			else:
				return 4

	def delete_item(self, item):
		pass

	def view(self, items_dict, lists):
		#self.items_dict[title] = {item_name: [quantity, budget]}
		items_dict = items_dict
		lists = shoppinglists

