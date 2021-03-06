# A binary search or half-interval search algorithm 
# finds the position of a specified input value (the search "key") 
# within an array sorted by key value.

# In each step, the algorithm compares the search key value with the 
# key value of the middle element of the array.

# If the keys match, then a matching element has been found and its index, 
# or position, is returned.

# Otherwise, if the search key is less than the middle element's key, 
# then the algorithm repeats its action on the sub-array to the left 
# of the middle element or, if the search key is greater, on the sub-array 
# to the right.

# If the remaining array to be searched is empty, then the key cannot be found 
# in the array and a special "not found" indication is returned.

# A binary search halves the number of items to check with each iteration, 
# so locating an item (or determining its absence) takes logarithmic time. 
# A binary search is a dichotomic divide and conquer search algorithm.

from typing import Any, List

def find(item:str, collection:List[Any]) -> int:
    if not collection:
       return -1
    pivot_index = len(collection) // 2
    pivot_value = collection[pivot_index]
    if pivot_value == item:
        return pivot_index
    elif pivot_value > item:
        return find(item, collection[0:pivot_index])
    else:
        temp_index = find(item, collection[pivot_index + 1:])
        if temp_index >= 0:
            return pivot_index + 1 + temp_index
        return temp_index

