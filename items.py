from user import User
from shoppinglist import Shoppinglist

items_dict = {'title':{'Name': 'Sugar', 'Quantity': '2kg', 'Budget': '200'}}
class Shoppingitems(object):
	"""
    Class for shoppinglist functionionality
    """

	def __init__(self, title=None, owner=None ):
		""" Initializing variables"""
		self.title = title
		self.owner = owner

	def add(self,title, item_name, quantity, budget):
			"""add items method"""
			print (title)
			if item_name != '' and quantity !='' and budget !='':
				for item_names in items_dict:
					if item_name not in items_dict.keys():
						items_dict['title'] = {'Name': item_name, 'Quantity': quantity, 'Budget': budget}
						print (items_dict)
						return 9
					else:
						return 3
			else:
				return 4

	def read_list_items(self,title,owner, ):
		if owner == owner:
			if title == items_dict[title]:
				list_items = items_dict
				return list_items

	"""def edit_item(self, owner, title, name):
		for name in range(len(self.items_dict)):
			if self.items_dict[name]['name'] == name:
				items_dict['title'] = {'Name': Nname, 'Quantity': Nquantity, 'Budget': Nbudget, 'Owner': owner} 

	def delete_item(self, owner, title, name):
		for item in range(len(self.items_dict)):
			if self.items_dict[name]['name'] == name:
				del self.item_list[item]
	"""
                