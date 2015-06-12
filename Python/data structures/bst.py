class Node:

    def __init__(self, key, val):
        self.left = None
        self.right = None
        self.key = key
        self.value = val

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, node):
        self.root = self._insert(self.root, node)

    def _insert(self, root, node):
        if root is None:
            return node
        if root.key > node.key:
            root.left = self._insert(root.left, node)
        else:
            root.right = self._insert(root.right, node)
        return root

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return None  # key not found
        if key < node.key:
            return self._search(node.left, key)
        elif key > node.key:
            return self._search(node.right, key)
        else:
            return node.value  # found key

if __name__ == '__main__':

    tree = BinarySearchTree()
    tree.insert(Node(3, "a"))
    tree.insert(Node(7, "d"))
    tree.insert(Node(1, "e"))
    tree.insert(Node(5, "f"))
    tree.insert(Node(6, "f"))
    tree.insert(Node(9, "f"))
    x = tree.search(9)



