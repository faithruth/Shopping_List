class ShoppingList(object):
    def __init__(self, myList=None):
        self.myList=myList or []

    def add_items(self, item):
        self.myList.append(item)
        return self.myList

    def add_more_items(self, item):
        self.myList.append(item)
        return self.myList
    
    def remove_item(self, item):
        self.myList.remove(item)
        return self.myList


   
    



    
        
