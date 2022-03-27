"""
    Linked list exercise
"""
class Node:
    """
    Class represent a node in a linked list
    """
    def __init__(self, value):
        self.node_value = value
        self.next_node = None

    def value(self):
        """
            Return the node value
        """
        return self.node_value

    def next(self):
        """
            Return the next node
        """
        return self.next_node


class LinkedList:
    """
        Class represent a linked list
    """
    def __init__(self, values=[]):
        node = None
        for item in values:
            new_node = Node(item)
            new_node.next_node = node
            node = new_node
        self.head_node = node
        self.current = self.head_node

    def __len__(self):
        count, node = 0, self.head_node
        while node is not None:
            count += 1
            node = node.next_node
        return count

    def __iter__(self):
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        value = self.current.node_value
        self.current = self.current.next_node
        return value

    def head(self):
        """
            Return the first node in the linked list
        """
        if self.head_node is None:
            raise EmptyListException("The list is empty.")
        return self.head_node

    def push(self, value):
        """
            Add new value to the head
        """
        new_head = Node(value)
        new_head.next_node = self.head_node
        self.head_node = new_head

    def pop(self):
        """
            Pop the value at the head
        """
        if self.head_node is None:
            raise EmptyListException("The list is empty.")
        value = self.head_node.node_value
        self.head_node = self.head_node.next_node
        return value

    def reversed(self):
        """
            Reverse all values in the linked list
        """
        lst = []
        node = self.head_node
        while node is not None:
            lst.append(node.node_value)
            node = node.next_node
        return LinkedList(lst)


class EmptyListException(Exception):
    """
        Empty List Exception
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
