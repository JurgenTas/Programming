__author__ = 'J Tas'

import random


class Randomizedqueue:
    """
    A randomized queue is similar to a stack or queue, except that the item
    removed is chosen uniformly at random from items in the data structure. This
    implementation supports each randomized queue operation (besides creating an
    iterator) in constant amortized time and use space proportional to the number
    of items currently in the queue.
    """

    def __init__(self):
        self.s = [None] * 1
        self.size = 0

    # resize s
    def resize(self, capacity):
        copy = [None] * capacity
        for i in xrange(self.size):
            copy[i] = self.s[i]
        self.s = copy

    # return true if the list is empty
    def empty(self):
        return self.size == 0;

    # return the number of items on the list
    def size(self):
        return self.size

    # add the item
    def enqueue(self, item):
        if item is None:
            raise Exception("trying to add None!")
        if self.size == len(self.s):
            self.resize(2 * len(self.s))
        self.s[self.size] = item
        self.size += 1

    # delete and return a random item
    def dequeue(self):
        if self.size < 1:
            raise Exception("Empty!")
        index = random.randint(0, self.size - 1)
        old_val = self.s[index]
        self.s[index] = self.s[self.size - 1]
        self.s[self.size - 1] = None
        self.size -= 1
        if 0 < self.size <= len(self.s) / 4:
            self.resize(len(self.s) / 2)
        return old_val

    # return (but do not delete) a random item
    def sample(self):
        if self.size < 1:
            raise Exception("Empty!")
        index = random.randint(0, self.size - 1)
        item = self.s[index]
        return item

    def __iter__(self):
        return self.RandomizedqueueItr(self)

    class RandomizedqueueItr:

        def __init__(self, obj):
            self.i = 0
            self.arr = [None] * obj.size
            for i in xrange(obj.size):
                self.arr[i] = obj.s[i]
            random.shuffle(self.arr)

        def __iter__(self):
            return self

        def has_next(self):
            return self.i < len(self.arr)

        def next(self):
            if not self.has_next():
                raise StopIteration()
            item = self.arr[self.i]
            self.i += 1
            return item;


if __name__ == "__main__":

    queue = Randomizedqueue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue("c")
    queue.enqueue("d")
    queue.enqueue("e")

    for q in queue:
        print(q)
