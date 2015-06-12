'''
A double-ended queue is a generalization of a stack and a queue that supports
inserting and removing items from either the front or the back of the data
structure. This implementation supports each deque operation in constant
worst-case time and uses space proportional to the number of items currently
in the deque
'''

__author__="jurgentas"
__date__ ="$Jun 27, 2014 10:39:38 AM$"

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    # return true if the list is empty
    def empty(self): 
        return self.size == 0;
    
    # return the number of items on the list
    def size(self):
        return self.size
    
    # insert the item at the front
    def add_first(self, item):
        if(item is None):
            raise Exception("trying to add None!")
        new_node = self.Node(item, next = self.head)
        if (self.empty()):
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
            
    # insert the item at the end
    def add_last(self, item):
        if(item is None):
            raise Exception("trying to add None!")
        new_node = self.Node(item, prev=self.tail)
        if (self.empty()):
            self.head = self.last = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    # delete and return the item at the front      
    def remove_first(self):
        if(self.empty()):
            raise Exception("empty deque!")
        self.size -= 1
        item = self.head.item
        if(self.empty()):
            self.head = self.last = None
        else:
            self.head.next.prev = None
            self.head = self.head.next;
        return item
    
    # delete and return the item at the end
    def remove_last(self):
        if(self.empty()):
            raise Exception("empty deque!")
        self.size -= 1
        item = self.tail.item
        if(self.empty()):
            self.head = self.tail = None
        else:
            self.tail.prev.next = None;
            self.tail = self.tail.prev;
        return item
    
    def __iter__(self):
        return self.DequeItr(self)
    
    class Node:
        
        def __init__(self, item = None, next = None, prev = None):
            self.item = item
            self.next = next
            self.prev = prev
            
    class DequeItr:
        
        def __init__(self, obj):
            self.current = obj.head
            
        def __iter__(self):
            return self
        
        def next(self):
            
            if self.current is None:
                raise StopIteration()  
            item = self.current.item
            self.current = self.current.next
            return item;

if __name__ == "__main__":
    
    d = Deque()
    d.add_first("a")
    d.add_first("b")
    d.add_first("c")
    d.add_first("d")
    d.add_first("e")
    d.add_first("f")
    d.remove_last()
    
    for x in d:
        print x
