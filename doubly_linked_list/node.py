class Node(object):
    """Node of a Doubly Linked List"""

    def __init__(self, data: object, prev_node: "Node" = None, next_node: "Node" = None):
        self.data = data
        self.previous = prev_node
        self.next = next_node
