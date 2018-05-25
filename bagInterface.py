"""
Interface for a collection of items stored in a type of
object like a bag.   
"""
class BagInterface():

    #constructor
    def __init__(self, sourceCollection = None):
        pass

    #accessor methods
    def isEmpty(self):
        return True

    def __len__(self):
        return 0

    def __str__(self):
        return ""

    def __iter__(self):
        return None

    def __add__(self, other):
        return None
    
    def __eq__(self, other):
        return False

    #mutator methods
    def clear(self):
        pass
    
    def add(self, item):
        pass

    def remove(self, item):
        pass