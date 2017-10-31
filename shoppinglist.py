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
		self.shoppinglist = {'BB':{'owner': 'glo@gmail.com', 'Description': 'Default'}}
		self.items_dict = {'BB':{'Name': 'Sugar', 'Quantity': '2kg', 'Budget': '200'}}
		
	def create(self, title, description, owner):
		"""create list method"""
		if description != ''and title != '':
			if title not in self.shoppinglist.keys():
				self.shoppinglist[title] = {'owner':owner, 'Description':description}
				print (self.shoppinglist)
				return 8 #"Successfully created"
			else:
				return "List already exists"
		else:
			return "Fill in all the details"

	def add(self,title, item_name, quantity, budget):
			"""add items method"""
			if item_name != '' and quantity !='' and budget !='':
				if title not in self.items_dict.keys():
					self.items_dict[title] = {'Name': item_name, 'Quantity': quantity, 'Budget': budget}
					print (self.items_dict)
					return 9
				else:
					return 3
			else:
				return 4



"""
	def edit_list(self, title, decription, owner):
		if title != '':
			if title in shoppinglist:
				shoppinglist[owner]['title'] == shoppinglist[owner]['ntitle']
				shoppinglist[owner]['description'] == shoppinglist[owner]['ndescription']
"""

	
