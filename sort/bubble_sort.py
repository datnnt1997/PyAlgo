from typing import List


"""
Bubble Sort Algorithm
https://en.wikipedia.org/wiki/Bubble_sort

* Algorithm

* Bubble Sort Complexity
    Time Complexities
        Best case complexity: O(n)
        Average case complexity: O(n^2)
        Worst case complexity: O(n^2)
    Space Complexity
        The space complexity of the Bubble sort is O(max).
"""


def bubble_sort(array: List[int]):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                tmp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = tmp


if __name__ == "__main__":
    data = [2, 3, 4, 2, 3]
    print(f"Array: {data}")
    bubble_sort(data)
    print(f"Sorted Array in Ascending Order: {data}")

