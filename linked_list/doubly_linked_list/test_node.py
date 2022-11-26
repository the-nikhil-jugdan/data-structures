import unittest

from .node import Node


class TestNode(unittest.TestCase):
    """
    Unit Tests for the Node Class
    """

    def test_single_node(self):
        """
        Test Case for single node creation
        """
        node = Node(1)
        self.assertIsNone(node.previous, "node.previous is not None for single Node initialization")
        self.assertIsNone(node.next, "node.next is not None for single Node initialization")

    def test_multiple_nodes(self):
        """
        Test Case for multiple node creation
        """
        node_0 = Node(0)
        node_1 = Node(1)
        node_2 = Node(2, prev_node=node_0, next_node=node_1)
        self.assertEqual(node_2.previous, node_0, "Incorrect previous in node initialization")
        self.assertEqual(node_2.next, node_1, "Incorrect next in node initialization")


if __name__ == '__main__':
    unittest.main()
