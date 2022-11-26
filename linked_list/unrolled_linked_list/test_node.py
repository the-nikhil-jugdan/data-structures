import unittest

from .node import Node


class TestNode(unittest.TestCase):
    """
        Unit Tests for the Node Class for Unrolled Linked List
    """

    def test_single_node(self):
        """Test Case for single Node"""
        node = Node([1, 2, 3])
        self.assertIsNone(node.next, "node.next is not None for single Node initialization")

    def test_multiple_nodes(self):
        """Test case for multiple Node"""
        node_1 = Node([1, 2, 3])
        node_2 = Node([4, 5, 6], next_node=node_1)
        self.assertEqual(node_2.next, node_1, "Incorrect next in node initialization")

    def test_initial_data(self):
        """Test case for initial data"""
        node = Node()
        self.assertEqual(node.data, [], "Node initialisation fails for no data")
        initial_data = [1, 2, 3, 4, 5]
        node = Node(initial_data)
        self.assertEqual(node.data, initial_data, "Node initialisation fails with initial data")
