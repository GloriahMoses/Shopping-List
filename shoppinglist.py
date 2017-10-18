from user import User
shoppinglist = {}
item_list = {}
class Shoppinglist(object):
	"""
    Class for user functionionality
    """

	def __init__(self, title=None, description=None, owner=None):
		""" Initializing variables"""
		self.title = title
		self.description = description
		self.owner = owner

	def create(self, title, description, owner):
		"""create list method"""
		if description != ''and title != '':
			if title not in shoppinglist.keys():
				shoppinglist[owner] = {'description':description,'title':title}
				print (shoppinglist)
				return 8 #"Successfully created"
			else:
				return "List already exists"
		else:
			return "Fill in all the details"

	def owner_items(self, user, list_name):
        user_items = [item for item in self.item_list if item['owner']
                      == user and item['list'] == list_name]
        return user_items

	def add(self, title, name, price, quantity):
			"""add items method"""
			if title != '' and name != '' and price != '' and quantity != '':
				items[title] = {"name": {'price':price, 'quantity': quantity, 'budget':budget, 'owner':owner}}
				print (items)
				return 1
			else:
				return "Fill in all the details"

	
