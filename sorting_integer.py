#!python
from sorting import insertion_sort


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: ??? Why and under what conditions?
        Time Complexity: O(n+k) where n is the number of elements in input array and k is the range of input. 
    TODO: Memory usage: ??? Why and under what conditions?
        Space Complexity:  O(n+k) where n is the number of elements in input array and k is the range of input. 
    """
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    if len(numbers) < 1:
        return
    # TODO: Find range of given numbers (minimum and maximum integer values)
    max_value = max(numbers)
    min_value = min(numbers)
    range_of_numbers = max_value - min_value + 1

    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    count_list = [0 for _ in range(range_of_numbers)]
    output = [0 for _ in range(len(numbers))]
    for i in range(0, len(numbers)):
        count_list[numbers[i]-min_value] += 1

    for i in range(1, len(count_list)):
        count_list[i] += count_list[i-1]

    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    for i in range(len(numbers)-1, -1, -1):
        output[count_list[numbers[i] - min_value] - 1] = numbers[i]
        count_list[numbers[i] - min_value] -= 1

    for i in range(0, len(numbers)):
        numbers[i] = output[i]

    return numbers


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: ??? Why and under what conditions?
        Time Complexity: O(n + k) for best case and 
            average case and O(n^2) for the worst case.
    TODO: Memory usage: ??? Why and under what conditions?
        Space Complexity: O(nk) for worst case."""

    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    if len(numbers) < 1:
        return

    max_value = max(numbers)
    min_value = min(numbers)

    range_of_buckets = (max_value - min_value) // num_buckets + 1
    buckets = [[] for _ in range(num_buckets)]

    # TODO: Loop over given numbers and place each item in appropriate bucket
    for i in numbers:
        index = (i - min_value) // range_of_buckets
        buckets[index].append(i)

    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    for i in range(len(buckets)):
        insertion_sort(buckets[i])

    # TODO: Loop over buckets and append each bucket's numbers into output list
    i = 0
    for bucket in buckets:
        for item in bucket:
            numbers[i] = item
            i += 1
