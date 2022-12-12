from typing import List


"""
Ternary Search Algorithm
https://en.wikipedia.org/wiki/Binary_search_algorithm
* Algorithm

* Counting Search Complexity
    Time Complexities
        Best case complexity: O(n+k)
        Average case complexity: O(n+k)
        Worst case complexity: O(n+k)
    Space Complexity
        The space complexity of the counting sot is O(max).
"""


def counting_sort(array: List[int]):
    size = max(array)
    output = [0] * len(array)

    count = [0] * (size + 1)

    for i in array:
        count[i] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for i in array:
        count[i] -= 1
        output[count[i]] = i

    for i in range(len(array)):
        array[i] = output[i]


if __name__ == "__main__":
    data = [2, 3, 4, 2, 3]
    print(f"Array: {data}")
    counting_sort(data)
    print(f"Sorted Array in Ascending Order: {data}")