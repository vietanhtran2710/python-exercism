"""
    Double linked list exercise
"""
class Node:
    """
        Class represent a node in the linked list
    """
    def __init__(self, value, succeeding=None, previous=None):
        self.value = value
        self.before = previous
        self.after = succeeding


class LinkedList:
    """
        Class represent a double linked list
    """
    def __init__(self):
        self.head = None

    def push(self, value):
        """
            Add value to the back
        """
        if self.head is None:
            self.head = Node(value)
        else:
            node = self.head
            while node.after is not None:
                node = node.after
            node.after = Node(value, None, node)

    def pop(self):
        """
            Remove value at the back
        """
        if self.head.after is None:
            value = self.head.value
            self.head = None
        else:
            node = self.head
            while node.after.after is not None:
                node = node.after
            value = node.after.value
            node.after = None
        return value

    def shift(self):
        """
            Remove value at the front
        """
        value = self.head.value
        self.head = self.head.after
        return value

    def unshift(self, value):
        """
            Add value to the front
        """
        new_node = Node(value, self.head, None)
        self.head = new_node
