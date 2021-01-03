# Hoare's quicksort algorithm:
# Quicksort is a divide-and-conquer algorithm. It works by selecting a 'pivot' element 
# from the array and partitioning the other elements into two sub-arrays, 
# according to whether they are less than or greater than the pivot. 
# The pivot value will then be placed between the higher and the lower range
# and never be touched again.
# The sub-arrays are then sorted recursively.
# 
# Time Complexity: 
# Best and Average Case: O(nlog(n))
# Worst Case: O(n^2)

from typing import List, Dict, Any
from pprint import pprint

def quicksort(input:List[int], lower_index:int, higher_index:int) -> List[int]:
    if lower_index >= higher_index:
        return input

    new_pivot = partition(input, lower_index, higher_index)
    
    quicksort(input, lower_index, new_pivot - 1)
    quicksort(input, new_pivot + 1, higher_index)
    
    return input

# apply partition to the part of the array between l and r indices
def partition(input:List[int], lower_index:int, higher_index:int) -> int:
    pivot = higher_index
    i = lower_index - 1

    for j in range(lower_index, higher_index):
        if input[j] <= input[pivot]:
            # increment the lower range
            i = i + 1
            # swap bigger and smaller number to have everything up to i being smaller than pivot
            # and everything from j to higher_index being greater than pivot
            input[i], input[j] = input[j], input[i]
    
    # place pivot between low and high number range at i + 1
    input[i + 1], input[pivot] = input[pivot], input[i + 1]

    return i + 1
