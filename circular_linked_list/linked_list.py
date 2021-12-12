from linked_list.linked_list import LinkedList
from linked_list.node import Node


class CircularLinkedList(LinkedList):
    """Circular Linked List"""

    def __init__(self, data: object = None):
        super(CircularLinkedList, self).__init__(data=data)
        if self.head:
            self.head.next = self.head

    def traverse(self, action=None, position: int = None) -> Node:
        """
            Traverses the list, returns the last or specified element and at each node performs the given action
        """
        current_node: Node = self.head
        current_position = 0
        last_node: Node = None

        if current_node is not None:
            while True:
                if action:
                    action(current_node)
                if current_position == position:
                    last_node = current_node
                    break
                if current_node.next == self.head:
                    last_node = current_node
                    break
                current_node = current_node.next
                current_position += 1
        return last_node

    def insert_at_start(self, data) -> Node:
        """Insert a Node at the start of the Linked List"""
        node = Node(data)
        if self.head is not None:
            node.next = self.head
            last_node = self.traverse()
            last_node.next = node
            self.head = node
        else:
            self.head = node
            self.head.next = node
        return node

    def insert_at_last(self, data) -> Node:
        """Insert a Node at the end of the Linked List"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            last_node = self.traverse()
            last_node.next = new_node
            new_node.next = self.head
        return new_node

    def remove_at_start(self) -> Node:
        if self.head:
            ret = self.head
            if self.head.next == self.head:
                self.head = None
                return ret
            last_node = self.traverse()
            last_node.next = self.head.next
            self.head = self.head.next
            ret.next = None
            return ret

    def remove_at_last(self) -> Node:
        """Remove the Node at the last of the Linked List"""
        # If list is not empty
        if self.head:
            length = self.length
            if length - 2 < 0:
                ret = self.head
                self.head = None
                return ret
            pre_last = self.traverse(position=length - 2)
            ret = pre_last.next
            pre_last.next = self.head
            return ret
