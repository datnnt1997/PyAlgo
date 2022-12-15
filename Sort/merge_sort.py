from typing import List


"""
Merge Sort Algorithm
https://en.wikipedia.org/wiki/Merge_sort

* Algorithm

* Merge Sort Complexity
    Time Complexities
        Best case complexity: O(nlogn)
        Average case complexity: O(nlogn)
        Worst case complexity: O(nlogn)
    Space Complexity
        The space complexity of the Merge sort is O(n).
"""


def merge_sort(array: List[int]):
    if len(array) > 1:
        mid = len(array) // 2

        left = array[:mid]

        right = array[mid:]

        merge_sort(left)

        merge_sort(right)

        l_idx = r_idx = k = 0

        while l_idx < len(left) and r_idx < len(right):
            if left[l_idx] > right[r_idx]:
                array[k] = right[r_idx]
                r_idx += 1
            else:
                array[k] = left[l_idx]
                l_idx += 1
            k += 1

        while l_idx < len(left):
            array[k] = left[l_idx]
            l_idx += 1
            k += 1

        while r_idx < len(right):
            array[k] = right[r_idx]
            r_idx += 1
            k += 1


if __name__ == "__main__":
    data = [2, 3, 4, 2, 3]
    print(f"Array: {data}")
    merge_sort(data)
    print(f"Sorted Array in Ascending Order: {data}")