from user import User

class Shoppinglist(object):

	"""
    Class for shoppinglist functionionality
    """
	def __init__(self, title=None, description=None, owner=None ):
		""" Initializing variables"""
		self.title = title
		self.description = description
		self.owner = owner
		self.shoppinglists = {}
		self.items_dict = {}
		
	def create(self, title, description, owner):
		"""create list method"""
		if description != ''and title != '':
			if title not in self.shoppinglists.keys():
				self.shoppinglists[title] = {'owner':owner, 'Description':description}
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
					print(items_dict)
					return 9
			else:
				return 4
	def view(self):
		self.items_dict = items_dict
		self.shoppinglists = lists
			
	def delete_item(self, item):
		for title in items_dict.keys():
			for item in items_dict[title].keys():
				self.item = items_dict[title].keys()
	
	def delete_list(self):
		pass
