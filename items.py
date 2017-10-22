from user import User
from shoppinglist import Shoppinglist

items_dict = {}
class Shoppingitems(object):

	def __init__(self, title=None, owner=None ):
		""" Initializing variables"""
		self.title = title
		self.owner = owner

	def add(self,title, name, quantity, budget, owner):
			"""add items method"""
			if name != '' and quantity !='' and budget !='':
				if name not in items_dict:
					items_dict[title] = {'Name': name, 'Quantity': quantity, 'Budget': budget}
					print (items_dict)
					return 9
				print ("anything")
