import unittest

import klast
import linkedlist


class KLastBase(object):
  """Base class for all tests for k-to-last functions.

  The function being tested is defined in the setUp() method, so that tests
  only need to be written once and can be applied to both implementations.
  """

  def get_k_to_last_of_list(self, source_list, k):
    return self.get_k_to_last(linkedlist.LinkedList(source_list), k)

  def testEmpty(self):
    self.assertIsNone(self.get_k_to_last_of_list([], 0))
    self.assertIsNone(self.get_k_to_last_of_list([], 1))

  def testLast(self):
    self.assertEqual(2, self.get_k_to_last_of_list([1, 5, 3, 2], 0).value)

  def testFirst(self):
    self.assertEqual(1, self.get_k_to_last_of_list([1, 5, 3, 2], 3).value)

  def testMiddle(self):
    self.assertEqual(5, self.get_k_to_last_of_list([1, 5, 3, 2], 2).value)

  def testOutOfBounds(self):
    self.assertIsNone(self.get_k_to_last_of_list([1, 5, 3, 2], 5))

  def testNegativeOnEmpty(self):
    self.assertIsNone(self.get_k_to_last_of_list([], -1))

  def testNegative(self):
    self.assertIsNone(self.get_k_to_last_of_list([1, 2, 3], -1))


class TestKLast(KLastBase, unittest.TestCase):

  get_k_to_last = staticmethod(klast.get_k_to_last)


class TestKLastOnePass(KLastBase, unittest.TestCase):

  get_k_to_last = staticmethod(klast.get_k_to_last_one_pass)
