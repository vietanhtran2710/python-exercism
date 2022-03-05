"""
    Tree Building Exercise
"""

class Record:
    """
        Class to store node's information
    """
    def __init__(self, record_id, parent_id):
        self.record_id = record_id
        self.parent_id = parent_id


class Node:
    """
        Class to store node's id and it's children
    """
    def __init__(self, node_id):
        self.node_id = node_id
        self.children = []


def BuildTree(records):
    """
        Return a tree from a list of records
    """
    records.sort(key=lambda x: x.record_id)
    if records:
        if records[-1].record_id != len(records) - 1:
            raise ValueError('Record id is invalid or out of order.')
        if records[0].record_id != 0:
            raise ValueError('Record id is invalid or out of order.')
    nodes = {}
    for node in records:
        if node.parent_id == node.record_id and node.record_id != 0:
            raise ValueError('Only root should have equal record and parent id.')
        if node.parent_id > node.record_id:
            raise ValueError('Node record_id should be smaller than it\'s parent_id.')
        child = Node(node.record_id)
        nodes[node.record_id] = child
        if node.record_id != 0:
            nodes[node.parent_id].children.append(child)
    if records:
        return nodes[0]
    return None
