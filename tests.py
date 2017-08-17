import unittest

from shopping_list import ShoppingList

class ShoppingListTestCase(unittest.TestCase):
    def setUp(self):
        self.myList = ShoppingList()

    def test_items(self):
        self.myList.items.append('perfume')
        self.assertEqual(self.myList.items, ['perfume'], msg='item not in list')

    def test_add_items(self):
        self.myList.add_item('honey')
        self.assertEqual(self.myList.items, ['pefume', 'honey'], msg='item not added to list')

      

    