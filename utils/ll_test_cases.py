from unittest import TestCase


def empty_list_initialization(instance: TestCase, ll):
    """
    Test cases for empty linked list initialization
    """
    instance.assertIsNone(ll.head, "Empty list initialization fails. head is not None")


def non_empty_list_initialization(instance: TestCase, ll, initial=0):
    """
    Test Cases for non empty linked list initialization
    """
    instance.assertIsNotNone(ll.head, "head is None for non-empty list")
    instance.assertEqual(ll.head.data, initial, "head initialized with wrong data")
    instance.assertIsNone(ll.head.next, "head.next is not null for singleton list")


def length_function(instance: TestCase, ll_class):
    """
    Test cases for length function
    """
    ll = ll_class()
    instance.assertEqual(ll.elements, [], "elements works incorrectly for empty list")
    ll = ll_class(5)
    instance.assertEqual(ll.elements, [5], "elements works incorrectly")


def elements_property(instance: TestCase, ll_class):
    """
    Test Cases for the elements property
    """
    ll = ll_class()
    instance.assertEqual(ll.elements, [], "elements works incorrectly for empty list")
    ll = ll_class(5)
    instance.assertEqual(ll.elements, [5], "elements works incorrectly")


def insert_at_start(instance: TestCase, ll_class):
    """
    Test cases for insert at start
    """
    ll = ll_class()
    ll.insert_at_start(5)
    instance.assertEqual(ll.elements, [5], "Insert at start not working properly")
    ll.insert_at_start(1)
    instance.assertEqual(ll.elements, [1, 5], "Insert at start not working properly")


def insert_at_end(instance: TestCase, ll_class):
    """
    Test cases for insert at end
    """
    ll = ll_class()
    ll.insert_at_last(3)
    # Test for empty list
    instance.assertEqual(ll.elements, [3], "Insert at last not working properly")
    ll.insert_at_start(2)
    ll.insert_at_start(1)
    ll.insert_at_last(4)
    instance.assertEqual(ll.elements, [1, 2, 3, 4], "Insert at last not working properly")
    ll.insert_at_last(5)
    instance.assertEqual(ll.elements, [1, 2, 3, 4, 5], "Insert at last not working properly")


def insert_at_position(instance: TestCase, ll_class):
    """
    Test Cases for insert at position
    """
    ll = ll_class()
    ll.insert_at_last(1)
    ll.insert_at_last(4)
    ll.insert_at_position(1, 2)
    instance.assertEqual(ll.elements, [1, 2, 4], "insert_at_position method is not working properly")
    ll.insert_at_position(2, 3)
    instance.assertEqual(ll.elements, [1, 2, 3, 4], "insert_at_position method is not working properly")
    ll.insert_at_position(2, 10)
    instance.assertEqual(ll.elements, [1, 2, 10, 3, 4], "insert_at_position method is not working properly")


def insert_at(instance: TestCase, ll_class):
    """
    Test Cases for insert_at method of Linked List
    """
    ll = ll_class()
    for i in range(1, 6):
        ll.insert_at_last(i)
    ll.insert_at(2, 6)
    instance.assertEqual(ll.elements, [1, 2, 6, 3, 4, 5], "insert_at method is not working properly")
    ll.insert_at(0, 7)
    instance.assertEqual(ll.elements, [7, 1, 2, 6, 3, 4, 5], "insert_at method is not working properly")
    ll.insert_at(7, 8)  # Inserting at last position
    instance.assertEqual(ll.elements, [7, 1, 2, 6, 3, 4, 5, 8], "insert_at method is not working properly")
    ll.insert_at(1, 9)
    instance.assertEqual(ll.elements, [7, 9, 1, 2, 6, 3, 4, 5, 8], "insert_at method is not working properly")
    ll.insert_at(8, 10)  # Inserting at last position
    instance.assertEqual(ll.elements, [7, 9, 1, 2, 6, 3, 4, 5, 10, 8], "insert_at method is not working properly")
    try:
        # Inserting beyond last position
        instance.assertRaises(Exception, ll.insert_at(11, 10))
    except Exception:
        pass


def remove_at_start(instance: TestCase, ll_class):
    """
    Test Cases for  remove_at_start Linked List method
    """
    ll = ll_class()
    for i in range(1, 6):
        ll.insert_at_last(i)
    ll.remove_at_start()
    instance.assertEqual(ll.elements, [2, 3, 4, 5], "remove_at_start method is not working properly")
    ll.remove_at_start()
    instance.assertEqual(ll.elements, [3, 4, 5], "remove_at_start method is not working properly")
    ll.remove_at_start()
    instance.assertEqual(ll.elements, [4, 5], "remove_at_start method is not working properly")


def remove_at_last(instance: TestCase, ll_class):
    """
    Test Cases for the remove_at_last method of Liked List
    """
    ll = ll_class()
    for i in range(1, 6):
        ll.insert_at_last(i)
    ll.remove_at_last()
    instance.assertEqual(ll.elements, [1, 2, 3, 4], "remove_at_last method is not working properly")
    ll.remove_at_last()
    instance.assertEqual(ll.elements, [1, 2, 3], "remove_at_last method is not working properly")
    ll.remove_at_last()
    instance.assertEqual(ll.elements, [1, 2], "remove_at_last method is not working properly")


def remove_at_position(instance: TestCase, ll_class):
    """
    Test Cases for the remove_at_method method of Linked List
    """
    ll = ll_class()
    for i in range(1, 6):
        ll.insert_at_last(i)
    ll.remove_at_position(1)
    instance.assertEqual(ll.elements, [1, 3, 4, 5], "remove_at_position method is not working properly")
    ll.remove_at_position(2)
    instance.assertEqual(ll.elements, [1, 3, 5], "remove_at_position method is not working properly")
    ll.remove_at_position(2)
    instance.assertEqual(ll.elements, [1, 3], "remove_at_position method is not working properly")


def remove_at(instance: TestCase, ll_class):
    """
    Test Cases for the remove_at method of Linked List
    """
    ll = ll_class()
    for i in range(1, 11):
        ll.insert_at_last(i)
    ll.remove_at(8)
    instance.assertEqual(ll.elements, [1, 2, 3, 4, 5, 6, 7, 8, 10], "remove_at method is not working properly")
    ll.remove_at(0)
    instance.assertEqual(ll.elements, [2, 3, 4, 5, 6, 7, 8, 10], "remove_at method is not working properly")
    ll.remove_at(7)  # Removing at last position
    instance.assertEqual(ll.elements, [2, 3, 4, 5, 6, 7, 8], "remove_at method is not working properly")
    ll.remove_at(1)
    instance.assertEqual(ll.elements, [2, 4, 5, 6, 7, 8], "remove_at method is not working properly")
    ll.remove_at(2)
    instance.assertEqual(ll.elements, [2, 4, 6, 7, 8], "insert_at method is not working properly")
    try:
        # Inserting beyond last position
        instance.assertRaises(Exception, ll.remove_at(11))
    except Exception:
        pass
