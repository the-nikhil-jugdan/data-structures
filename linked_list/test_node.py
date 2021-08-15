import unittest

from .node import Node


class TestNode(unittest.TestCase):
    """
        Unit Tests for the Node Class
    """

    def test_single_node(self):
        """Test Case for single Node"""
        node = Node(1)
        self.assertIsNone(node.next, "node.next is not None for single Node initialization")

    def test_multiple_nodes(self):
        """Test case for multiple Node"""
        node_1 = Node(1)
        node_2 = Node(2, next_node=node_1)
        self.assertEqual(node_2.next, node_1, "Incorrect next in node initialization")
