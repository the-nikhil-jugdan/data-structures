import unittest

from .linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    """
        Unit Test for the Linked List Class
    """

    def test_empty_list_initialization(self):
        ll = LinkedList()
        self.assertIsNone(ll.head, "Empty list initialization fails. head is not None")

    def test_non_empty_list_initialization(self):
        ll = LinkedList(5)
        self.assertIsNotNone(ll.head, "head is None for non-empty list")
        self.assertEqual(ll.head.data, 5, "head initialized with wrong data")
        self.assertIsNone(ll.head.next, "head.next is not null for singleton list")

    def test_length_function(self):
        ll = LinkedList()
        self.assertEqual(ll.length, 0, "Length function returns incorrect length for 0 elements")
        ll = LinkedList(5)
        self.assertEqual(ll.length, 1, "Length function returns incorrect length")

    def test_elements_function(self):
        ll = LinkedList()
        self.assertEqual(ll.elements, [], "elements works incorrectly for empty list")
        ll = LinkedList(5)
        self.assertEqual(ll.elements, [5], "elements works incorrectly")

    def test_insert_at_start(self):
        ll = LinkedList()
        ll.insert_at_start(5)
        self.assertEqual(ll.elements, [5], "Insert at start not working properly")
        ll.insert_at_start(1)
        self.assertEqual(ll.elements, [1, 5], "Insert at start not working properly")

    def test_insert_at_end(self):
        ll = LinkedList()
        ll.insert_at_last(3)
        # Test for empty list
        self.assertEqual(ll.elements, [3], "Insert at last not working properly")
        ll.insert_at_start(2)
        ll.insert_at_start(1)
        ll.insert_at_last(4)
        self.assertEqual(ll.elements, [1, 2, 3, 4], "Insert at last not working properly")
        ll.insert_at_last(5)
        self.assertEqual(ll.elements, [1, 2, 3, 4, 5], "Insert at last not working properly")

    def test_insert_at_position(self):
        """Tests the insert_at_position method of Linked List"""
        ll = LinkedList()
        ll.insert_at_last(1)
        ll.insert_at_last(4)
        ll.insert_at_position(1, 2)
        self.assertEqual(ll.elements, [1, 2, 4], "insert_at_position method is not working properly")
        ll.insert_at_position(2, 3)
        self.assertEqual(ll.elements, [1, 2, 3, 4], "insert_at_position method is not working properly")
        ll.insert_at_position(2, 10)
        self.assertEqual(ll.elements, [1, 2, 10, 3, 4], "insert_at_position method is not working properly")


if __name__ == '__main__':
    unittest.main()
