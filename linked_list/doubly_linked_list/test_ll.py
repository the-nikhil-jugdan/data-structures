import unittest

from linked_list.utils import ll_test_cases as utils
from .linked_list import LinkedList


class TestDoublyLinkedList(unittest.TestCase):
    """
    Unit test for the Doubly Linked List class
    """

    def test_empty_list_initialization(self):
        """
        Empty Doubly Linked List initialization
        """
        ll = LinkedList()
        utils.empty_list_initialization(
            self,
            ll
        )

    def test_non_empty_list_initialization(self):
        """
        Non-empty Doubly Linked List initialization
        """
        utils.non_empty_list_initialization(
            self,
            LinkedList(5),
            5
        )

    def test_length_function(self):
        """
        Length method of Doubly Linked List
        """
        utils.length_function(
            self,
            LinkedList
        )

    def test_elements_prop(self):
        """
        Elements property of Linked List
        """
        utils.elements_property(
            self,
            LinkedList
        )

    def test_insert_at_start(self):
        """
        Insert element at start of the Linked List
        """
        utils.insert_at_start(
            self,
            LinkedList
        )

    def test_insert_at_end(self):
        """
        Insert element at the end of Linked List
        """
        utils.insert_at_end(
            self,
            LinkedList
        )

    def test_insert_at_position(self):
        """
        Insert an element at a position in Linked List (Private)
        """
        utils.insert_at_position(
            self,
            LinkedList
        )

    def test_insert_at(self):
        """
        Insert element at a position in Linked List
        """
        utils.insert_at(
            self,
            LinkedList
        )

    def test_remove_at_start(self):
        """
        Remove element from start of Linked List
        """
        utils.remove_at_start(
            self,
            LinkedList
        )

    def test_remove_at_end(self):
        """
        Remove element from enf of Linked List
        """
        utils.remove_at_last(
            self,
            LinkedList
        )

    def test_remove_at_position(self):
        """
        Remove element from a position in Linked List(Private)
        """
        utils.remove_at_position(
            self,
            LinkedList
        )

    def test_remove_at(self):
        """
        Remove element from a position in Linked List
        """
        utils.remove_at(
            self,
            LinkedList
        )


if __name__ == '__main__':
    unittest.main()
