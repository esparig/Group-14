"""This module defines a singly-linked list implementation."""


class Node:
  """An element of the list.

  Contains a value (of any type) and a reference to the next element in the
  list.
  """

  def __init__(self, value=None):
    """Creates a new node.

    Args:
      value: the value to be stored in the node.
    """
    self.value, self.next = value, None


# This implementation uses the iterator a lot, it is not better in
# terms of complexity:
# pros: shorter methods, more consistent with other Python containers list, dicts...
# cons: confusing to the reader unfamiliar with iterators
#
# resource on Python's iterators:
# https://www.programiz.com/python-programming/iterator
# http://www.diveintopython3.net/iterators.html


class LinkedList:
  """A singly-linked list.

  The first element of the list (of type Node) is accessible via the head field.
  Further elements can be accessed via the next field of the node returned.
  """

  def __init__(self, source_list):
    """Creates a LinkedList from a Python list.

    Args:
      source_list: a list, the values to put in the newly created list.
    """
    # __init__ loops over the input list: O(n)

    if not source_list:
      self.head = None
      return

    current = self.head = Node(source_list[0])
    for value in source_list[1:]:
      current.next = Node(value)
      current = current.next

  def __iter__(self):
    """An iterator object over the list's elements.

    This function returns an iterator object in constant time.

    Then the caller of the iterator can call 'next()' and next will returns each
    Node, and once exhausted the iterator will raise a StopIteration exception.

    When using the for loop over an iterable, __iter__ then __next__ are called
    automatically (these steps are called the iterator protocol).

    Yields:
      the Node in the list.
    """
    current = self.head
    while current:
      # Return the current element as the next element of the iterator, but keep
      # the state so that the next call to it will return the next element.
      yield current
      current = current.next
    # When there are no more elements, the function returns None.

  def __len__(self):
    """Returns the length of the list.

    Enumerate returns an iterator immediately, and the for loop will call next()
    on the enumerate iterator until exhausted. You can call next on an
    enumerate iterator as many times as there are elements in the iterator
    provided to enumerate. __iter__ will yields the n elements, so enumerate
    will also return n elements. __len__ is in O(n).

    Returns:
      a number, the length of the list.
    """
    if not self.head:
      return 0
    for index, _ in enumerate(self):
      pass
    return index + 1

  def __getitem__(self, k):
    """Returns the k-th element of the list.

    Args:
      k: a number, the index within the list.

    Returns:
      a Node, corresponding to the given position in the list

    Raises:
      IndexError: if the requested element does not exist.
    """
    if k < 0:
      return self[len(self) + k]  # O(n) due to len()
    else:
      for index, node in enumerate(self):  # O(n) due to __iter__
        if index == k:
          return node
      else:
        raise IndexError('LinkedList only has %s elements, no %sth element' %
                         (index + 1, k))
