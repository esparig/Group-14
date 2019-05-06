import unittest

from linkedlist import LinkedList


class TestLinkedList(unittest.TestCase):

  def test_construct_iter(self):
    list_ = [1, 2, 3, 4, 5, 6, 6]
    self.assertEqual([n.value for n in LinkedList(list_)], list_)

  def test_len(self):
    """len() of a LinkedList must be equal to the len of the input list."""
    # for 2 sample lists, I test that the len of the list is the len
    # of the LinkedList that is constructed with the list.
    l1 = [1]
    self.assertEqual(len(LinkedList(l1)), len(l1))
    l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    self.assertEqual(len(LinkedList(l2)), len(l2))
    l3 = []
    self.assertEqual(len(LinkedList(l3)), len(l3))

  def test_forward(self):
    ll = LinkedList(range(10))
    for index_value in range(10):
      self.assertEqual(ll[index_value].value, index_value)

  def test_get_negative_k(self):
    ll = LinkedList(range(-10, 0))
    for v in range(-10, 0):
      self.assertEqual(ll[v].value, v)

  def test_None_is_an_acceptable_value(self):
    self.assertEqual(LinkedList([1, None, 2])[1].value, None)
