from abc import ABC, abstractmethod


# TODO: Create enhanced API for Linked List
class LinkedListBase(object):
    """
    Linked List Base class
    """

    node_class = None

    def __init__(self, data: object = None):
        """
        Create a new linked list instance
        """
        if not self.node_class:
            raise Exception("Node class not configured")
        if data:
            self._head = self.node_class(data)
            self._length = 1
        else:
            self._head = None
            self._length = 0
        self._last = self._head

    @property
    def length(self):
        return self._length

    @property
    def last(self):
        return self._last

    def traverse(self, action=None):
        """
        Traverse the list and perform some actions
        """
