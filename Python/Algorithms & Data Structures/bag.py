__author__ = 'J Tas'
 
 
class _Item:
 
    def __init__(self, item):
        self.item = item
        self.next = None
 
 
class Bag:
 
    def __init__(self):
        self.first = None
        self.n = 0
 
    def is_empty(self):
        return self.first is None
 
    def size(self):
        return self.n
 
    def add(self, x):
        item = _Item(x)
        item.next = self.first
        self.first = item
        self.n += 1
 
    def __iter__(self):
        """Return iterator for the bag."""
        current = self.first
        while current:
            yield current.item
            current = current.next
