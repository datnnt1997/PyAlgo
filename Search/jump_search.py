from typing import Optional, List

import math

"""
Jump Search Algorithm
https://en.wikipedia.org/wiki/Jump_search
* Algorithm
    Jump search technique also works for ordered lists. It creates a block and tries to find the element in that block. 
    If the item is not in the block, it shifts the entire block. The block size is based on the size of the list. If 
    the size of the list is n then block size will be √n. After finding a correct block it finds the item using a linear 
    search technique. The jump search lies between linear search and binary search according to its performance.
* Jump Search Complexity
    Time Complexities
        The time Complexity: O(√n)
    Space Complexity
        The space complexity: O(1).
"""


def jump_search(in_list: List[int], target: int) -> Optional[int or None]:
    block_size = int(math.sqrt(len(in_list)))
    l_index = 0
    r_index = block_size
    while in_list[min(r_index, len(in_list))-1] < target:
        l_index = r_index
        r_index = r_index + block_size
        if l_index >= len(in_list):
            return None
    while in_list[l_index] < target:
        l_index += 1
        if l_index == min(r_index, len(in_list)):
            return None
    if in_list[l_index] == target:
        return l_index
    return None


if __name__ == "__main__":
    arr = [10, 13, 15, 26, 28, 50, 56, 88, 94, 127, 159, 356, 480, 567, 689, 699, 780, 850, 956, 995]
    target = 356
    print(f"Sorted array: {arr}")
    print(f"Iterative Implementation - Value {target} is at index {jump_search(arr, target)}")
