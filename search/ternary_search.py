from typing import Optional, List

"""
Ternary Search Algorithm
https://en.wikipedia.org/wiki/Binary_search_algorithm
* Algorithm

* Binary Search Complexity
    Time Complexities
        Best case complexity: O(1)
        Average case complexity: O(log n)
        Worst case complexity: O(log n)
    Space Complexity
        The space complexity of the binary search is O(1).
"""


def tenary_search(in_list: List[int], target: int) -> Optional[int or None]:
    l_index = 0
    r_index = len(in_list) - 1
    while l_index <= r_index:
        m1_index = l_index + (l_index + r_index) // 3
        m2_index = r_index - (l_index + r_index) // 3
        if in_list[m1_index] == target:
            return m1_index
        elif in_list[m2_index] == target:
            return m2_index
        elif in_list[m1_index] >  target:
    return None


if __name__ == "__main__":
    arr = [10, 13, 15, 26, 28, 50, 56, 88, 94, 127, 159, 356, 480, 567, 689, 699, 780, 850, 956, 995]
    target = 356
    print(f"Sorted array: {arr}")
    print(f"Iterative Implementation - Value {target} is at index {tenary_search(arr, target)}")
