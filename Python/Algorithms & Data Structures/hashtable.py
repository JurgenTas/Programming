__author__ = 'J Tas'


class HashTable():
    def __init__(self, size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def hash_func(self, key):
        s = 0
        for pos in range(len(key)):
            s += (pos + 1) * ord(key[pos])
        return s % self.size

    def rehash(self, old_hash):
        return (old_hash + 1) % self.size

    def put(self, key, data):
        idx = self.hash_func(key)
        if self.slots[idx] is None:
            self.slots[idx] = key
            self.data[idx] = data
        else:
            if self.slots[idx] == key:
                self.data[idx] = data  # replace
            else:
                next_slot = self.rehash(idx)
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot)
                    if self.slots[next_slot] is None:
                        self.slots[next_slot] = key
                        self.data[next_slot] = data
                    else:
                        if self.slots[next_slot] == key:
                            self.data[next_slot] = data  # replace

    def get(self, key):
        idx = self.hash_func(key)
        data = None
        stop = False
        found = False
        pos = idx
        while self.slots[pos] is not None and not found and not stop:
            if self.slots[pos] == key:
                stop = True
                found = True
                data = self.data[pos]
            else:
                pos = self.rehash(pos)
                if pos == idx:
                    stop = True
        return data


if __name__ == "__main__":
    ht = HashTable(5)
    ht["a"] = 5
    ht["b"] = 4
    ht["c"] = 3
    ht["d"] = 2
    ht["e"] = 1
