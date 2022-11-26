class Node(object):
    """Node of a Linked List"""

    def __init__(self, data: object, next_node: "Node" = None):
        self.data = data
        self.next = next_node
