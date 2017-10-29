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
		self.shoppinglist = {'glo@gmail.com':{'Title': 'BB', 'Description': 'Default'}}
		
	def create(self, title, description, owner):
		"""create list method"""
		if description != ''and title != '':
			if title not in self.shoppinglist.keys():
				self.shoppinglist[owner] = {'Title':title, 'Description':description}
				print (self.shoppinglist)
				return 8 #"Successfully created"
			else:
				return "List already exists"
		else:
			return "Fill in all the details"

	def read_list(self,title, owner):
		if owner == owner:
			lists = self.shoppinglist
			return lists

"""
	def edit_list(self, title, decription, owner):
		if title != '':
			if title in shoppinglist:
				shoppinglist[owner]['title'] == shoppinglist[owner]['ntitle']
				shoppinglist[owner]['description'] == shoppinglist[owner]['ndescription']
"""