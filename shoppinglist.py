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
		shoppinglists = {}
		items_dict = {}
		
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
	def view(self):
		for title in items_dict.keys():
			title = lists 
		for item in items_dict[title].keys():
			items = items_dict
			
	def delete_item(self, item):
		for title in items_dict.keys():
			for item in items_dict[title].keys():
				self.item = items_dict[title].keys()
	
	def delete_list(self):
		pass
