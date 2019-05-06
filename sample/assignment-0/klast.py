"""Function that return the k-to-last element of a LinkedList."""


def get_k_to_last(list_, k):
  """Computes the k-to-last element of the list.

  Args:
    list_: a LinkedList, the list from which to get the element
    k: a number, the index from the end of the list

  Returns:
    the k-to-last element of the list.
  """
  length = len(list_)
  if k < 0 or k >= length:
    return None
  return list_[len(list_) - k - 1]


def get_k_to_last_one_pass(list_, k):
  """Computes the k-to-last element of the list.

  Args:
    list_: a LinkedList, the list from which to get the element
    k: a number, the index from the end of the list

  Returns:
    the k-to-last element of the list.
  """
  if k < 0:
    return None
  trailing = leading = list_.head
  if not leading:
    # The list is empty.
    return None
  # Move leading k steps ahead of trailing.
  for _ in range(k):
    leading = leading.next
    if not leading:
      # The list has less than k elements.
      return None
  # Move both references forward until leading reaches the last element.
  while leading.next:
    leading, trailing = leading.next, trailing.next
  # Trailing is now k steps before it.
  return trailing
