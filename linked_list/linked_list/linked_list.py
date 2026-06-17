from .node import Node


class LinkedList(object):
    """Linked List Class"""

    def __init__(self, data: object = None):
        """
        Creates a Linked List with given data for head.
        Creates an empty list if no data given
        """
        if data:
            self.head: Node | None = Node(data)
        else:
            self.head = None

    def __iter__(self):
        """Yields one node at a time, making LL an iterable"""
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = current_node.next

    @property
    def length(self) -> int:
        """Returns length of the Linked List"""
        return sum(1 for _ in self)

    @property
    def elements(self) -> list:
        """Returns list of data of the Linked list"""
        return [elem.data for elem in self]

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
            last_node = None
            for current_node in self:
                last_node = current_node
            if last_node is not None:
                last_node.next = new_node
        return new_node

    def insert_at_position(self, position, data) -> Node:
        curr_node = None
        for curr_pos, curr_node in enumerate(self):
            if curr_pos == position - 1:
                break
        if curr_node is None:
            raise IndexError("Element position out of bound")
        node = Node(data, curr_node.next)
        curr_node.next = node
        return node

    def remove_at(self, position: int) -> Node | None:
        """Remove the Node at the given position"""
        length = self.length
        if position > length:
            raise Exception("Element Position out of bound")
        if position == 0:
            return self.remove_at_start()
        if position == length - 1:
            return self.remove_at_last()
        return self.remove_at_position(position)

    def remove_at_start(self) -> Node | None:
        if self.head:
            ret = self.head
            self.head = self.head.next
            ret.next = None
            return ret

    def remove_at_last(self) -> Node | None:
        """Remove the Node at the last of the Linked List"""
        # If list is not empty
        if self.head:
            pre_last = self.head
            if self.head.next is None:
                self.head = None
                return pre_last

            length = self.length
            for pos, node in enumerate(self):
                if pos == length - 2:
                    pre_last = node
                    break

            ret = pre_last.next
            pre_last.next = None
            return ret

    def remove_at_position(self, position: int) -> Node | None:
        """Removes the Node at the given position"""
        if self.head:
            prev_node = None
            for pos, node in enumerate(self):
                if pos == position - 1:
                    prev_node = node
                    break
            if prev_node is None or prev_node.next is None:
                raise IndexError("Element position out of bound")
            ret = prev_node.next
            prev_node.next = ret.next
            ret.next = None
            return ret

    def delete(self):
        self.head = None
