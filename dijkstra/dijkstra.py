# Dijkstra's shortest path algorithm:
# In an undirected, weighted graph find the cheapest path 
# from a given start node to a given end node.
#
# For each vertex find the distance to its neighbors and add it to the already taken path.
# Store the smaller distance as new distance. 
# Add the visited vertex to the list of visited nodes. 
# Stop when the end vertex is contained in the list of visited nodes.
#
# Time Complexity: O(|V|^2)

from typing import List, Dict, Any
from collections import namedtuple
import math
from pprint import pprint

Vertex = namedtuple('Vertex', ['name', 'weight'])
        
def find_shortest_path(graph:Dict[str, List[Vertex]], start:str, end:str) -> Dict[str, Any]:
    visited = ['']   
    unvisited = list(graph.keys())
    
    shortestDistancesInit = dict() 
    for vertex in unvisited:
        if vertex == start:
            shortestDistancesInit[vertex] = 0. 
            shortestDistancesInit['path'] = [] # type: ignore
        else:
            shortestDistancesInit[vertex] = math.inf
    
    for node_name, neighbors in graph.items():
        neighbors.sort(key=lambda vertex: vertex.weight)

    shortestDistances = traverse(start, graph, visited, end, shortestDistancesInit)
    
    return {'distance': shortestDistances[end], 'path': shortestDistances['path']}

def traverse(current_node: str, graph:Dict[str, List[Vertex]], visited:List[str], end:str, shortestDistances:Dict) -> Dict:

    if end in visited:
        shortestDistances['path'] = list(filter(None, visited))
        return shortestDistances

    visited.append(current_node)
    
    for neighbor in graph[current_node]:
        if neighbor.name not in visited:
            shortestDistances[neighbor.name] = min(
                shortestDistances[neighbor.name], 
                shortestDistances[current_node] + neighbor.weight
            )
            return traverse(neighbor.name, graph, visited, end, shortestDistances)
    
    shortestDistances['path'] = list(filter(None, visited))
    return shortestDistances