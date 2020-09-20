from adt_binary_tree import *

def test_creating_tree():
    tree = Tree()
    assert tree.get_root() is None

def test_get_tree_root():
    tree = Tree()
    tree.add_node(7)

    assert tree.get_root().value == Node(7).value


def test_build_tree():
    tree = Tree()
    tree.add_node(7)
    tree.add_node(4)
    tree.add_node(5)
    tree.add_node(8)

    assert tree.find_node(7).left.value == Node(4).value
    assert tree.find_node(7).right.value == Node(8).value

def test_find_existing_node():
    tree = Tree()
    tree.add_node(7)
    tree.add_node(4)
    tree.add_node(5)
    tree.add_node(8)
    tree.add_node(9)
    tree.add_node(2)
    tree.add_node(11)

    assert tree.find_node(9).value == Node(9).value


def test_find_missing_node():
    tree = Tree()
    tree.add_node(7)
    tree.add_node(4)
    tree.add_node(5)
    tree.add_node(8)
    tree.add_node(9)
    tree.add_node(2)
    tree.add_node(11)

    assert tree.find_node(10) is None