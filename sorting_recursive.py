#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list

    merged_items = []

    i_1 = 0
    i_2 = 0

    while i_1 < len(items1) and i_2 < len(items2):
        if items1[i_1] < items2[i_2]:
            merged_items.append(items1[i_1])
            i_1 += 1
        else:
            merged_items.append(items2[i_2])
            i_2 += 1

    # TODO: Append remaining items in non-empty list to new list
    # when we have reached the end of one of the lists (unequal lengths)
    if i_1 != len(items1):
        merged_items += items1[i_1:]
    else:
        merged_items += items2[i_2:]
    return merged_items


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    if len(items) <= 1:
        return items

    # TODO: Split items list into approximately equal halves
    mid_point = len(items)//2  # split the list into two

    # TODO: Sort each half by recursively calling merge sort
    items1 = merge_sort(items[:mid_point])
    items2 = merge_sort(items[mid_point:])

    # TODO: Merge sorted halves into one list in sorted order
    sorted_items = merge(items1, items2)
    items[:] = sorted_items

    return items  # return sorted list


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    pivot = low

    # TODO: Loop through all items in range [low...high]
    for i in range(low, high):
        # TODO: Move items less than pivot into front of range [low...p-1]
        if items[pivot] >= items[i]:
            items[pivot], items[i] = items[i], items[pivot]
            i += 1

    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p
    return pivot


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    if high is None:
        high = len(items)

    if low is None:
        low = 0

    # TODO: Check if list or range is so small it's already sorted (base case)
    if len(items) == 1:
        return items

    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort
    if high > low:
        par = partition(items, low, high)

        quick_sort(items, low, par-1)
        quick_sort(items, par+1, high)

    return items
