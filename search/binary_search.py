from typing import Optional, List

"""
Binary Search Algorithm
https://en.wikipedia.org/wiki/Binary_search_algorithm
* Algorithm
    Binary search works on sorted arrays. Binary search begins by comparing an element in the middle of the array with 
    the target value. If the target value matches the element, its position in the array is returned. If the target 
    value is less than the element, the search continues in the lower half of the array. If the target value is greater 
    than the element, the search continues in the upper half of the array. By doing this, the algorithm eliminates the 
    half in which the target value cannot lie in each iteration.

* Binary Search Complexity
    Time Complexities
        Best case complexity: O(1)
        Average case complexity: O(log n)
        Worst case complexity: O(log n)
    Space Complexity
        The space complexity of the binary search is O(1).
"""


def binary_search(in_list: List[int], target: int) -> Optional[int or None]:
    l_index = 0
    r_index = len(in_list) - 1
    while l_index <= r_index:
        m_index = (l_index + r_index) // 2
        if in_list[m_index] > target:
            r_index = m_index - 1
        elif in_list[m_index] < target:
            l_index = m_index + 1
        else:
            return m_index
    return None


def run_resursive_binary_search(in_list: List[int], target: int, left_index: int = 0, righ_index: int = 0):
    if left_index > righ_index:
        return None
    m_index = (left_index + righ_index) // 2
    if in_list[m_index] > target:
        return run_resursive_binary_search(in_list, target, left_index=left_index, righ_index=righ_index - 1)
    elif in_list[m_index] < target:
        return run_resursive_binary_search(in_list, target, left_index=left_index + 1, righ_index=righ_index)
    else:
        return m_index


def recursive_binary_search(in_list: List[int], target: int) -> Optional[int or None]:
    l_index = 0
    r_index = len(in_list) - 1
    return run_resursive_binary_search(in_list, target, left_index=l_index, righ_index=r_index)


if __name__ == "__main__":
    arr = [10, 13, 15, 26, 28, 50, 56, 88, 94, 127, 159, 356, 480, 567, 689, 699, 780, 850, 956, 995]
    target = 356
    print(f"Sorted array: {arr}")
    print(f"Iterative Implementation - Value {target} is at index {binary_search(arr, target)}")
    print(f"Recursive Implementation - Value {target} is at index {recursive_binary_search(arr, target)}")
