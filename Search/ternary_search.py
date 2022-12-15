from typing import Optional, List

"""
Ternary Search Algorithm

* Algorithm

* Ternary Search Complexity
    Time Complexities
        Best case complexity: O(1)
        Average case complexity: O(log n)
        Worst case complexity: O(log n)
    Space Complexity
        The space complexity of the ternary search is O(1).
"""


def tenary_search(in_list: List[int], target: int) -> Optional[int or None]:
    return None

if __name__ == "__main__":
    arr = [10, 13, 15, 26, 28, 50, 56, 88, 94, 127, 159, 356, 480, 567, 689, 699, 780, 850, 956, 995]
    target = 356
    print(f"Sorted array: {arr}")
    print(f"Iterative Implementation - Value {target} is at index {tenary_search(arr, target)}")
