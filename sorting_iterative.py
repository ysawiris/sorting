#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if so
    n = len(items)

    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will repeat one time more than needed.

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # if the element found is greater
            # than the next element the items are not sorted
            if items[j] > items[j+1]:
                return False

    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order

    n = len(items)

    # Traverse through all array elements
    for i in range(n-1):

        # loop though the remaining elements
        for j in range(0, n-i-1):

            # Swap if the element found is greater
            # than the next element
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
    # Traverse through all array elements
    for i in range(len(items)):
        # Traverse through the other element
        # and find highest elemnt and put in the back
        max_idx = i
        for j in range(i+1, len(items)):
            if items[max_idx] > items[j]:
                max_idx = j

        # Swap the found minimum element with
        # the first element
        items[i], items[max_idx] = items[max_idx], items[i]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
    # Traverse through 1 to len(arr)
    for i in range(1, len(items)):

        key = items[i]

        # check if the element is smaller than the
        # previous element untill you are at index 0
        j = i-1
        while j >= 0 and key < items[j]:
            items[j+1] = items[j]
            j -= 1
        items[j+1] = key
