import unittest
from adt_stack import Stack

def test_creating_stack():
    new_stack = Stack(8)
    assert new_stack.size == 8
    assert new_stack.top_of_stack == -1


def test_stack_push():
    new_stack = Stack(4)
    new_stack.push("Foo")
    new_stack.push("Bar")
    new_stack.push("Baz")

    assert new_stack.top_of_stack == 2


def test_stack_pop():
    new_stack = Stack(4)
    new_stack.push("Foo")
    new_stack.push("Bar")
    new_stack.push("Baz")
    popped_data = new_stack.pop()

    assert popped_data == "Baz"
    assert new_stack.top_of_stack == 1


def test_stack_peek():
    new_stack = Stack(4)
    new_stack.push("Foo")
    new_stack.push("Bar")
    new_stack.push("Baz")

    assert new_stack.peek() == "Baz"
    assert new_stack.top_of_stack == 2
