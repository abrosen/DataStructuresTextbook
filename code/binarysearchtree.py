class BinarySearchTree:
    class Node:
        def __init__(self, item):
            self.item = item
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, item):
        self.root = self._addRecursive(self.root, item)

    def _addRecursive(self, node, item):
        if node is None:
            return self.Node(item)
        if item <= node.item:
            node.left = self._addRecursive(node.left, item)
        else:
            node.right = self._addRecursive(node.right, item)
        return node

    def contains(self, item):
        return self._containsRecursive(self.root, item)

    def _containsRecursive(self, node, item):
        if node is None :
            return False
        if node.item == item:
            return True
        if item < node.item:
            return self._containsRecursive(node.left, item)
        return self._containsRecursive(node.right, item)
