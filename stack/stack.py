class Stack(object):
    def __init__(self):
        self.arr = []
        self._length = 0

    @property
    def length(self) -> int:
        return self._length

    def push(self, elem: object):
        self.arr.append(elem)
        self._length += 1

    def pop(self) -> object:
        if self.length == 0:
            raise IndexError("Stack is empty")
        ret = self.arr.pop()
        self._length -= 1
        return ret
