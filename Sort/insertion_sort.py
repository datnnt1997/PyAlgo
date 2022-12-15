from typing import List


"""
Insertion Sort Algorithm
https://en.wikipedia.org/wiki/Insertion_sort

* Algorithm

* Insertion Sort Complexity
    Time Complexities
        Best case complexity: O(n)
        Average case complexity: O(n^2)
        Worst case complexity: O(n^2)
    Space Complexity
        The space complexity of the Insertion sort is O(n).
"""


def insertion_sort(array: List[int]):
    for i in range(1, len(array)):
        tmp = array[i]
        j = i - 1
        while j >= 0 and tmp < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = tmp


if __name__ == "__main__":
    data = [2, 5, 3, 6, 4, 2, 3]
    print(f"Array: {data}")
    insertion_sort(data)
    print(f"Sorted Array in Ascending Order: {data}")