from linked_list.circular_linked_list.linked_list import CircularLinkedList


class Node:
    """Node of an unrolled linked list"""

    def __init__(self, data: list = [], next_node: "Node" = None):
        self.next = next_node
        linked_list = CircularLinkedList()
        for elem in data:
            linked_list.insert_at_last(elem)
        self.linked_list = linked_list

    @property
    def data(self):
        return self.linked_list.elements
