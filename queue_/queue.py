class Queue(object):
    def __init__(self):
        self.arr = []
        self._length = 0
        self._front = 0
        self._rear = 0

    def enqueue(self, elem: object):
        self._length += 1
        self._rear += 1
        self.arr.append(elem)

    def dequeue(self) -> object:
        self._length -= 1
        ret = self.arr[self._front]
        self._front += 1
        return ret

    def length(self) -> int:
        return self._length
