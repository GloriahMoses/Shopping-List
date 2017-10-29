from user import User
from shoppinglist import Shoppinglist

#items_dict = {'title':{'Name': 'Sugar', 'Quantity': '2kg', 'Budget': '200'}}
class Shoppingitems(object):
	"""
    Class for shoppinglist functionionality
    """

	def __init__(self, title=None, owner=None ):
		""" Initializing variables"""
		self.title = title
		self.owner = owner
		self.items_dict = {'backtosch':{'Name': 'Sugar', 'Quantity': '2kg', 'Budget': '200'}}

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