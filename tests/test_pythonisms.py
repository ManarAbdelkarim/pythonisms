from pythonisms import __version__
from pythonisms.pythonisms import *
import pytest

def test_eq(test):
    list1 , list2 = test
    actual = linked == linked2
    expected = True
    assert actual == expected

def test_iter(test):
    list1 , list2 = test
    actual = [x for x in list1]
    expected = [4,3,2,1]
    assert actual == expected



@pytest.fixture()
def test():
    linked = LinkedList()
    linked.insert(1)
    linked.insert(2)
    linked.insert(3)
    linked.insert(4)

    linked2 = LinkedList()
    linked2.insert(1)
    linked2.insert(2)
    linked2.insert(3)
    linked2.insert(4)
    return linked ,linked2