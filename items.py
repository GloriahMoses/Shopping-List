from user import User
from shoppinglist import Shoppinglist
item_dict = {}

class Items(object):

	def __init__(self, title, owner):
		self.title = title
		self.owner = owner


	def add(self, title, name, price, quantity):
			"""add items method"""
			if title != '' and name != '' and price != '' and quantity != '':
				item_dict[title] = {"name":name, 'price':price, 'quantity': quantity, 'budget':budget, 'owner':owner}
				print (item_dict)
				return 9
			else:
				return "Fill in all the details"

