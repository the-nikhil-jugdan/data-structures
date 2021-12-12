import unittest

from utils import ll_test_cases as utils
from .linked_list import CircularLinkedList


class TestLinkedList(unittest.TestCase):
    """
        Unit Test for the Linked List Class
    """

    def test_empty_list_initialization(self):
        """
        Empty Linked List initialization
        """
        ll = CircularLinkedList()
        utils.empty_list_initialization(
            self,
            ll
        )

    def test_non_empty_list_initialization(self):
        """
        Non-empty Linked List initialization
        """
        utils.non_empty_circular_list_initialization(
            self,
            CircularLinkedList(5),
            5
        )

    def test_length_function(self):
        """
        Length method of Linked List
        """
        utils.length_function(
            self,
            CircularLinkedList
        )

    def test_elements_function(self):
        """
        Elements property of  Linked List
        """
        utils.elements_property(
            self,
            CircularLinkedList
        )

    def test_insert_at_start(self):
        """
        Insert element at start of Linked List
        """
        utils.insert_at_start(
            self,
            CircularLinkedList
        )

    def test_insert_at_end(self):
        """
        Insert element at end of Linked List
        """
        utils.insert_at_end(
            self,
            CircularLinkedList
        )

    def test_insert_at_position(self):
        """
        Insert element at a position in Linked List (Private)
        """
        utils.insert_at_position(
            self,
            CircularLinkedList
        )

    def test_insert_at(self):
        """
        Insert element at a position in Linked List
        """
        utils.insert_at(
            self,
            CircularLinkedList
        )

    def test_remove_at_start(self):
        """
        Remove element from start of Linked List
        """
        utils.remove_at_start(
            self,
            CircularLinkedList
        )

    def test_remove_at_last(self):
        """
        Remove element from end of Linked List
        """
        utils.remove_at_last(
            self,
            CircularLinkedList
        )

    def test_remove_at_position(self):
        """
        Remove element from a position in Linked List (Private)
        """
        utils.remove_at_position(
            self,
            CircularLinkedList
        )

    def test_remove_at(self):
        """
        Remove element from a position in Linked List
        """
        utils.remove_at(
            self,
            CircularLinkedList
        )


if __name__ == '__main__':
    unittest.main()
