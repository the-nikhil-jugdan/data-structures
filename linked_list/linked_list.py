from .node import Node


class LinkedList(object):
    """Linked List Class"""

    def __init__(self, data: object = None):
        """
            Creates a Linked List with given data for head.
            Creates an empty list if no data given
        """
        if data:
            self.head: Node = Node(data)
        else:
            self.head = None

    @property
    def length(self) -> int:
        """Returns length of the Linked List"""
        elements = 0

        def inc_len(node):
            nonlocal elements
            elements += 1

        self.traverse(inc_len)
        return elements

    @property
    def elements(self) -> list:
        """Returns list of data of the Linked list"""
        elements = []

        def add(node):
            nonlocal elements
            elements.append(node.data)

        self.traverse(add)
        return elements

    def traverse(self, action=None, position: int = None) -> Node:
        """
            Traverses the list, returns the last element and at each node performs the given action
        """
        current_node: Node = self.head
        current_position = 0
        last_node: Node = None

        while current_node is not None:
            if action:
                action(current_node)
            if current_position == position:
                last_node = current_node
                break
            if not current_node.next:
                last_node = current_node
            current_node = current_node.next
            current_position += 1

        return last_node

    def insert_at(self, position, data) -> Node:
        """Insert a Node at the given position"""
        length = self.length
        if position > length:
            raise Exception("Element Position out of bound")
        if position == 0:
            return self.insert_at_start(data)
        if position == length:
            return self.insert_at_last(data)
        return self.insert_at_position(position, data)

    def insert_at_start(self, data) -> Node:
        """Insert a Node at the start of the Linked List"""
        node = Node(data, self.head)
        self.head = node
        return node

    def insert_at_last(self, data) -> Node:
        """Insert a Node at the end of the Linked List"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last_node = self.traverse()
            last_node.next = new_node
        return new_node

    def insert_at_position(self, position, data):
        node_at_prev_pos = self.traverse(position=position - 1)
        node = Node(data, node_at_prev_pos.next)
        node_at_prev_pos.next = node
        return node
