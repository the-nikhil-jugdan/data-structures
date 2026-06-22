from queue.queue import Queue


def test_init():
    queue = Queue()
    assert queue.length == 0


def test_enque():
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.length == 3
    assert queue.dequeue() == 3
    assert queue.dequeue() == 2
    assert queue.dequeue() == 1
