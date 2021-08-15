from .node import Node


class LinkedList(object):
    """Doubly Linked List Class"""

    def __init__(self, data: object = None):
        """
        Creates a doubly linked list
        If data is given, creates a single node
        If data is not given, head is None
        """
        if data:
            self.head: Node = Node(data)
        else:
            self.head: Node = None

    def traverse(self, action=None, position: int = None) -> Node:
        """
        Traverses th list, returns the last or specified element and at each node performs the given action
        """

        # Return if empty list
        if self.head is None:
            return None

        current_node: Node = self.head
        current_position = 0

        while True:
            # If action is specified, execute
            if action:
                action(current_node)

            # If we hit the required position, return current node
            if current_position == position:
                return current_node

            # If we hit the last node, return
            if current_node.next is None:
                return current_node

            # Next iteration
            current_node = current_node.next
            current_position += 1

    @property
    def length(self) -> int:
        """Returns the length of the linked list"""
        elements = 0

        def inc_len(node):
            nonlocal elements
            elements += 1

        self.traverse(inc_len)

        return elements

    @property
    def elements(self) -> list:
        """Return list of Linked List data"""
        elements = []

        # Add data to list
        def add(node):
            nonlocal elements
            elements.append(node.data)

        self.traverse(add)

        return elements

    def insert_at_start(self, data: object) -> Node:
        """Insert a new Node at the start of the list and return the node"""
        # Empty List
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data, next_node=self.head)
            self.head.previous = node
            self.head = node
        return self.head

    def insert_at_last(self, data: object) -> Node:
        """Insert a Node at the end of Linked List"""
        # Empty List
        if self.head is None:
            self.head = Node(data)
            return self.head
        else:
            last_node = self.traverse()
            node = Node(data, prev_node=last_node)
            last_node.next = node
            return node

    def insert_at_position(self, position: int, data: object) -> Node:
        """
        Insert a node at the given position (Private)
        """
        next_node = self.traverse(position=position)
        prev = next_node.previous
        node = Node(data, prev_node=prev, next_node=next_node)
        prev.next = node
        next_node.previous = node
        return node

    def insert_at(self, position: int, data: object) -> Node:
        """
        Insert a node at the given position
        """
        length = self.length
        if position > length:
            raise Exception("Element Position out of bound")
        if position == 0:
            return self.insert_at_start(data)
        if position == length:
            return self.insert_at_last(data)
        return self.insert_at_position(position, data)

    def remove_at_start(self) -> Node:
        """
        Remove element from start of Linked List
        """
        # If list is not empty
        if self.head:
            ret = self.head
            self.head = self.head.next
            self.head.previous = None
            ret.next = None
            return ret

    def remove_at_last(self) -> Node:
        """
        Remove element from the end of the Linked List
        """
        # If list is not empty
        if self.head:
            last = self.traverse()
            prev = last.previous
            last.previous = None
            prev.next = None
            return last

    def remove_at_position(self, position: int) -> Node:
        """
        Removes the Node at the given position
        """
        # Check if List isn't empty
        if self.head:
            node = self.traverse(position=position)
            # If node has a next
            if node.next:
                node.next.previous = node.previous
            # If node has a previous
            if node.previous:
                node.previous.next = node.next
            node.previous = None
            node.next = None
            return node

    def remove_at(self, position: int) -> Node:
        """
        Remove the Node at the given position
        """
        length = self.length
        if position > length:
            raise Exception("Element Position out of bound")
        if position == 0:
            return self.remove_at_start()
        if position == length - 1:
            return self.remove_at_last()
        return self.remove_at_position(position)
