import unittest

from shopping_list import ShoppingList

class ShoppingListTestCase(unittest.TestCase):
    def setUp(self):
        self.myList = ShoppingList()

    def test_items(self):
        self.assertEqual(self.myList.myList, [], msg='item not in list')

    def test_add_items(self):
        self.myList.add_items('lotion')
        self.assertEqual(self.myList.myList, ['lotion'], msg='item not added to list')

    def test_add_more_items(self):
        self.myList.add_more_items('perfume')
        self.assertEqual(self.myList.myList, ['perfume'], msg='item not not on list')

    def test_remove_item(self):
        self.myList.remove_item("perfume")
        self.assertEqual(self.myList.myList, ['perfume'], msg="Item not deleted")
    
  
    