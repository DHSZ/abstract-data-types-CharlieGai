from adt_queue import *


def test_creating_queue():
    test_queue = Queue(10)

    assert test_queue.size == 10


def test_enqueuing_data():
    test_queue = Queue(5)
    test_queue.enqueue("Jared")
    test_queue.enqueue("Manisha")
    test_queue.enqueue("Diane")

    assert test_queue.front_index == 0
    assert test_queue.end_index == 2


def test_dequeuing_data():
    test_queue = Queue(5)
    test_queue.enqueue("Jared")
    test_queue.enqueue("Manisha")
    test_queue.enqueue("Diane")

    assert test_queue.dequeue() == "Jared"
    assert test_queue.dequeue() == "Manisha"
    assert test_queue.dequeue() == "Diane"


def test_cyclical_dequeue():
    test_queue = Queue(5)
    test_queue.enqueue("Jordan")
    test_queue.enqueue("Virgil")
    test_queue.enqueue("Sadio")
    test_queue.enqueue("Mo")
    test_queue.dequeue()
    test_queue.dequeue()
    test_queue.enqueue("Roberto")
    test_queue.enqueue("Takumi")
    test_queue.enqueue("James")

    assert test_queue.dequeue() == "Sadio"
    assert test_queue.storage == ["Takumi", "James", None, "Mo", "Roberto"]