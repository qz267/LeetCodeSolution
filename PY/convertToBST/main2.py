__author__ = 'zheng'


class EmptyTree(object):
    def isEmpty(self):
        return True

    def __str__(self):
        return ""


class BinaryTree(object):

    THE_EMPTY_TREE = EmptyTree()

    def __init__(self, item):
        self._root = item
        self._left = BinaryTree.THE_EMPTY_TREE
        self._right = BinaryTree.THE_EMPTY_TREE

    def isEmpty(self):
        return False

    def getRoot(self):
        return self._root

    def getLeft(self):
        return self._left

    def getRight(self):
        return self._right

    def setRoot(self, item):
        self._root = item

    def setLeft(self, tree):
        self._left = tree

    def setRight(self, tree):
        self._right = tree

    def removeLeft(self):
        left = self._left
        self._left = BinaryTree.THE_EMPTY_TREE
        return left

    def removeRight(self):
        right = self._right
        self._right = BinaryTree.THE_EMPTY_TREE
        return right

    def __str__(self):
        """Returns a string representation of the tree
        rotated 90 degrees to the left."""
        def strHelper(tree, level):
            result = ""
            if not tree.isEmpty():
                result += strHelper(tree.getRight(), level + 1)
                result += "| " * level
                result += str(tree.getRoot()) + "\n"
                result += strHelper(tree.getLeft(), level + 1)
            return result
        return strHelper(self, 0)