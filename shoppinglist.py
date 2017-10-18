from user import User
shoppinglist = {}

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
	
