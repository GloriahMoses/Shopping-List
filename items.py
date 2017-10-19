from user import User
from shoppinglist import Shoppinglist

item_lists = {}
class Shoppingitems(object):

	def __init__(self, title=None, owner=None ):
		""" Initializing variables"""
		self.title = title
		self.owner = owner

	def add(self,title, name, quantity, budget, owner):
			"""add items method"""
			if name != '' and quantity !='' and budget !='':
				if name not in item_lists:
					self.title = title
					item_lists[title] = {'name': name, 'quantity': quantity, 'budget': budget}
					print (item_lists)
					print(title)
					return 9