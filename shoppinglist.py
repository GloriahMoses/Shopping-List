from user import User
import collections

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
				print(shoppinglists)
				return 8 #"Successfully created"
			else:
				return 10 #"List already exists"
		else:
			return "Fill in all the details"

	def add(self,title, item_name, quantity, budget):
			"""add items method and edit"""
			if item_name != '' and quantity !='' and budget !='':
				if title not in shoppinglists.keys():
					return "Error"
				else:
					items_dict[title] = {item_name: [quantity, budget]}
					print(items_dict)
					print(shoppinglists)
					return 9
			else:
				return 4
	def view(self):
		print(items_dict)
		print(shoppinglists)
		return shoppinglists
		return items_dict
	
			
	def delete_item(self, item):
		for title in items_dict.keys():
			for item in items_dict[title].keys():
				self.item = items_dict[title].keys()
	
	def delete_list(self):
		pass
