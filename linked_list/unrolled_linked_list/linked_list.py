from linked_list.linked_list.linked_list import LinkedList
from .node import Node


class UnrolledLinkedList(LinkedList):
    """Unrolled linked list class"""

    def __init__(self, data: list = None):
        super(UnrolledLinkedList, self).__init__()
        if data:
            self.head: Node = Node(data)
