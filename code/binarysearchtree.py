class BinarySearchTree:
    class Node:
        def __init__(self, item):
            self.item = item
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
    
    def add(self, item):
        self.root = self._addRecursive(self.root, item)

    def _addRecursive(self, root, item):
        if root is None:
            return self.Node(item)
        if item <= root.item:
            root.left = self._addRecursive(root.left, item)
        else:
            root.right = self._addRecursive(root.right, item)
        return root

    def contains(self, item):
        return self._containsRecursive(self.root, item)

    def _containsRecursive(self, root, item):
        if root is None :
            return False
        if root.item == item:
            return True
        if item < root.item:
            return self._containsRecursive(root.left, item)
        return self._containsRecursive(root.right, item)


    def delete(self, item):
        self.root = self._deleteRecursive(self.root, item)
        
    def _deleteRecursive(self, root, item):
        if root is None:
            return root
        if item < root.item:
            root.left = self._deleteRecursive(root.left, item)
            return root
        elif item > root.item:
            root.right = self._deleteRecursive(root.right, item)
            return root
        else:
            # found the node to delete
            if root.left is None and root.right is None:
                return None
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left
            # node has two children
            # find the next in-order predecessor of root
            # replace the root's data with the predecessor's data
            # and delete the predecessor node
            rootOfLeftSubtree = root.left
            if rootOfLeftSubtree.right is None:
                root.item = rootOfLeftSubtree.item
                root.left = rootOfLeftSubtree.left
                return root
            
            # find the next in-order predecessor of root
            parentOfPredecessor = rootOfLeftSubtree
            current = rootOfLeftSubtree.right
            while current.right is not None:
                parentOfPredecessor = current
                current = current.right
            predecessor = current # found next in-order predecessor of root
            root.item = predecessor.item
            parentOfPredecessor.right = predecessor.left #adopt any grandchildren
            return root