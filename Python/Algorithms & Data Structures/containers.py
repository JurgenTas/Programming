__author__ = 'J Tas'

# =====================================================================


class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# =====================================================================


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, node):
        self.next = node


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.get_next()
        return count

    def search(self, item):
        curr = self.head
        found = False
        while curr is not None and not found:
            if curr.get_data() == item:
                found = True
            else:
                curr = curr.get_next()
        return found

    def remove(self, item):
        curr = self.head
        prev = None
        found = False
        while not found:
            if curr.get_data() == item:
                found = True
            else:
                prev = curr
                curr = curr.get_next()
        if prev is None:
            self.head = curr.get_next()
        else:
            prev.set_next(curr.get_Next())


# =====================================================================

if __name__ == "__main__":

    l1 = LinkedList()
    l1.add("a")
    l1.add("b")
    l1.add("c")
    l1.add("d")
    l1.add("e")




