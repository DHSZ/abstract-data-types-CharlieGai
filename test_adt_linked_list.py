from adt_linked_list import *

def test_create_a_list():
    llist = LinkedList(["a", "b", "c", "d", "e"])
    assert str(llist) == "a -> b -> c -> d -> e -> None"

def test_add_to_start():
    llist = LinkedList()

    llist.add_to_start(Node("b"))
    assert str(llist) == "b -> None"

    llist.add_to_start(Node("a"))
    assert str(llist) == "a -> b -> None"


def test_add_to_end():
    llist = LinkedList()

    llist.add_to_end(Node("b"))
    assert str(llist) == "b -> None"

    llist.add_to_end(Node("a"))
    assert str(llist) == "b -> a -> None"


def test_add_after():
    llist = LinkedList()

    llist.add_to_start(Node("b"))
    llist.add_to_start(Node("a"))
    llist.add_to_end(Node("d"))
    llist.add_after("b", Node("c"))
    assert str(llist) == "a -> b -> c -> d -> None"

def test_remove_node():
    llist = LinkedList()

    llist.add_to_start(Node("b"))
    llist.add_to_start(Node("a"))
    llist.add_to_end(Node("d"))
    llist.add_after("b", Node("c"))
    llist.remove_node("b")
    assert str(llist) == "a -> c -> d -> None"