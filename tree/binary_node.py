class Node(object):
    def __init__(self, object):
        self.data = object
        self.left: "Node | None" = None
        self.right: "Node | None" = None
