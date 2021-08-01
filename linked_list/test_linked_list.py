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

    def test_insert_at(self):
        """Tests the insert_at Linked List method"""
        ll = LinkedList()
        for i in range(1, 6):
            ll.insert_at_last(i)
        ll.insert_at(2, 6)
        self.assertEqual(ll.elements, [1, 2, 6, 3, 4, 5], "insert_at method is not working properly")
        ll.insert_at(0, 7)
        self.assertEqual(ll.elements, [7, 1, 2, 6, 3, 4, 5], "insert_at method is not working properly")
        ll.insert_at(7, 8)  # Inserting at last position
        self.assertEqual(ll.elements, [7, 1, 2, 6, 3, 4, 5, 8], "insert_at method is not working properly")
        ll.insert_at(1, 9)
        self.assertEqual(ll.elements, [7, 9, 1, 2, 6, 3, 4, 5, 8], "insert_at method is not working properly")
        ll.insert_at(8, 10)  # Inserting at last position
        self.assertEqual(ll.elements, [7, 9, 1, 2, 6, 3, 4, 5, 10, 8], "insert_at method is not working properly")
        try:
            # Inserting beyond last position
            self.assertRaises(Exception, ll.insert_at(11, 10))
        except Exception:
            pass

    def test_remove_at_start(self):
        """Tests the remove_at_start Linked List method"""
        ll = LinkedList()
        for i in range(1, 6):
            ll.insert_at_last(i)
        ll.remove_at_start()
        self.assertEqual(ll.elements, [2, 3, 4, 5], "remove_at_start method is not working properly")
        ll.remove_at_start()
        self.assertEqual(ll.elements, [3, 4, 5], "remove_at_start method is not working properly")
        ll.remove_at_start()
        self.assertEqual(ll.elements, [4, 5], "remove_at_start method is not working properly")

    def test_remove_at_last(self):
        """Tests the remove_at_last Linked List method"""
        ll = LinkedList()
        for i in range(1, 6):
            ll.insert_at_last(i)
        ll.remove_at_last()
        self.assertEqual(ll.elements, [1, 2, 3, 4], "remove_at_last method is not working properly")
        ll.remove_at_last()
        self.assertEqual(ll.elements, [1, 2, 3], "remove_at_last method is not working properly")
        ll.remove_at_last()
        self.assertEqual(ll.elements, [1, 2], "remove_at_last method is not working properly")

    def test_remove_at_position(self):
        """Tests the remove_at_position method of Linked List"""
        ll = LinkedList()
        for i in range(1, 6):
            ll.insert_at_last(i)
        ll.remove_at_position(1)
        self.assertEqual(ll.elements, [1, 3, 4, 5], "remove_at_position method is not working properly")
        ll.remove_at_position(2)
        self.assertEqual(ll.elements, [1, 3, 5], "remove_at_position method is not working properly")
        ll.remove_at_position(2)
        self.assertEqual(ll.elements, [1, 3], "remove_at_position method is not working properly")

    def test_remove_at(self):
        """Tests the remove_at Linked List method"""
        ll = LinkedList()
        for i in range(1, 11):
            ll.insert_at_last(i)
        ll.remove_at(8)
        self.assertEqual(ll.elements, [1, 2, 3, 4, 5, 6, 7, 8, 10], "remove_at method is not working properly")
        ll.remove_at(0)
        self.assertEqual(ll.elements, [2, 3, 4, 5, 6, 7, 8, 10], "remove_at method is not working properly")
        ll.remove_at(7)  # Inserting at last position
        self.assertEqual(ll.elements, [2, 3, 4, 5, 6, 7, 8], "remove_at method is not working properly")
        ll.remove_at(1)
        self.assertEqual(ll.elements, [2, 4, 5, 6, 7, 8], "remove_at method is not working properly")
        ll.remove_at(2)  # Inserting at last position
        self.assertEqual(ll.elements, [2, 4, 6, 7, 8], "insert_at method is not working properly")
        try:
            # Inserting beyond last position
            self.assertRaises(Exception, ll.remove_at(11))
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
