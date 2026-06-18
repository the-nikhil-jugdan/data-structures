from stack.stack import Stack


def test_init():
    stack = Stack()
    assert stack.length == 0


def test_ops():
    stack = Stack()
    stack.push(1)
    assert stack.length == 1
    assert stack.pop() == 1
