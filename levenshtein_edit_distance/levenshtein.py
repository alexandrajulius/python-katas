# Levenshtein's edit distance algorithm
#
# This algorithm takes two strings:
#  - string1 of length n, and 
#  - string2 of length m, 
# and returns the distance between them.
#
# Example:
# The Levenshtein distance between "kitten" and "sitting" is 3, since the following 
# three edits change one into the other, and there is no way to do it with fewer than three edits:
#
# kitten → sitten (substitution of "s" for "k")
# sitten → sittin (substitution of "i" for "e")
# sittin → sitting (insertion of "g" at the end).
#
# This algorithm is used for string autocorrection in the following way:
# We can create a Levenshtein automaton for a given word and a given distance d.
# We can then convert it to a DFA (Deterministic Finite Automaton).
# 
# Supposed we have a dictionary of words stored as Trie we can then
# quickly find all words in that Trie that have distance d to the input string
# and return those as an autocorrection suggestion.
#
# Moreover, Levenshtein's algorithm is a common example for dynamic programming, 
# since we do not re-calculate all distances between the letters file finding the minimal
# distance, but store them in a matrix.

import numpy as np
from pprint import pprint
        
def edit_distance(string1:str, string2:str) -> int:
    distance_matrix = np.arange(0)
    n = len(string1)
    m = len(string2)
    
    distance_matrix.resize(n + 1, m + 1)

    for i in range(1, n + 1):
        distance_matrix[i, 0] = i   
    
    for j in range(1, m + 1):
        distance_matrix[0, j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if string1[i-1] == string2[j-1]:
                substitutionCost = 0
            else:
                substitutionCost = 1

            distance_matrix[i, j] = min(
                distance_matrix[i - 1, j] + 1,                # deletion
                distance_matrix[i, j-1] + 1,                  # insertion
                distance_matrix[i-1, j-1] + substitutionCost  # substitution
                )

    return distance_matrix[n, m]