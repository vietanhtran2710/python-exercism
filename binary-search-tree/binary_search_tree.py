"""
    Binary search tree exercise
"""
class TreeNode:
    """
        Class representing a single node in a tree
    """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    """
        Class representing the whole binary tree create by multiple TreeNode
    """
    def __init__(self, tree_data):
        self.root = TreeNode(tree_data[0])
        for item in tree_data[1:]:
            compare_node = self.root
            while True:
                if item <= compare_node.data:
                    if compare_node.left is None:
                        compare_node.left = TreeNode(item)
                        break
                    compare_node = compare_node.left
                else:
                    if compare_node.right is None:
                        compare_node.right = TreeNode(item)
                        break
                    compare_node = compare_node.right

    def data(self):
        """
            Return the tree data
        """
        return self.root

    def sorted_data(self):
        """
            Return the sorted data in the tree
        """
        def get_sorted(node):
            result = []
            if node.left is not None:
                result += get_sorted(node.left)
            result += [node.data]
            if node.right is not None:
                result += get_sorted(node.right)
            return result

        return get_sorted(self.root)
