from .binary_node import Node


class BinarySearchTree(object):
    def __init__(self, data=None):
        self._root: Node | None = Node(data) if data is not None else None

    def root(self) -> Node | None:
        return self._root

    def find(self, data) -> Node | None:
        return BinarySearchTree.find_in_node(self._root, data)

    @staticmethod
    def find_in_node(node: Node | None, data: object) -> Node | None:
        if node is None:
            return None
        if node.data == data:
            return node
        left_res = BinarySearchTree.find_in_node(node.left, data)
        if left_res is not None:
            return left_res
        return BinarySearchTree.find_in_node(node.right, data)

    def insert(self, data: object):
        if self._root is None:
            self._root = Node(data)
        else:
            BinarySearchTree.insert_in_node(self._root, data)

    @staticmethod
    def insert_in_node(node: Node, data: object):
        """"""
        if node.data > data:
            if node.left is None:
                node.left = Node(data)
            else:
                BinarySearchTree.insert_in_node(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                BinarySearchTree.insert_in_node(node.right, data)

    def __str__(self) -> str:
        if self._root is not None:
            return "\n".join(BinarySearchTree.to_node_str_list(self._root))
        return ""

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def to_node_str_list(node: Node) -> list[str]:
        left_rep = (
            [] if node.left is None else BinarySearchTree.to_node_str_list(node.left)
        )
        right_rep = (
            [] if node.right is None else BinarySearchTree.to_node_str_list(node.right)
        )
        left_len = len(left_rep)
        right_len = len(right_rep)
        str_rep_internal = []
        str_rep = []
        for i in range(0, max(left_len, right_len)):
            if i >= left_len:
                str_rep_internal.append((" " * len(right_rep[i]), right_rep[i]))
            elif i >= right_len:
                str_rep_internal.append((left_rep[i], (" " * len(left_rep[i]))))
            else:
                str_rep_internal.append((left_rep[i], right_rep[i]))
        print(str_rep_internal)
        if len(str_rep_internal) == 0:
            str_rep.insert(0, str(node.data))
        else:
            str_rep = [a + b for (a, b) in str_rep_internal]
            max_len = max(len(str_rep_internal[-1][0]), len(str_rep_internal[-1][1]))
            previous_elems = str_rep_internal[0]
            left = previous_elems[0].strip()
            right = previous_elems[1].strip()
            str_rep[0] = (
                " " * (max_len // 2 - 1)
                + left
                + "-" * max(max_len // 2, 3)
                + "\u2575"
                + "-" * max(max_len // 2, 3)
                + right
                + " " * (max_len // 2)
            )
            max_len = len(str_rep[0])
            str_rep.insert(
                0,
                " " * (max_len // 2)
                + str(node.data)
                + " " * (max_len // 2 - len(str(node.data))),
            )
        return str_rep
