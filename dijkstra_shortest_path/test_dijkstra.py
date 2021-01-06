from hamcrest import assert_that, calling, equal_to, raises
from dijkstra import find_shortest_path, Vertex

#      A
#    /  \
#   7    9
#  /      \
# B---1----C
#
def test_finds_shortest_path_from_A_to_C():
    graph = {
        'A': [Vertex('B', 7), Vertex('C', 9)],
        'B': [Vertex('A', 7), Vertex('C', 1)],
        'C': [Vertex('A', 9), Vertex('B', 1)]
    } 
    start = 'A'
    end = 'C'
    expected = {'distance': 8, 'path': ['A', 'B', 'C']}
    assert_that(find_shortest_path(graph, start, end), equal_to(expected))

#
#        F---9--E
#       /|      |
#      / |      |
#     /  |      |
#    14  2      6
#   /    |      |
#  /     |      |
# A---9--C--11--D
#
def test_finds_shortest_path_from_A_to_E():
    graph = {
        'A': [Vertex('C', 9), Vertex('F', 14)],
        'C': [Vertex('A', 9), Vertex('D', 11), Vertex('F', 2)],
        'D': [Vertex('C', 11), Vertex('E', 6)],
        'E': [Vertex('D', 6), Vertex('F', 9)],
        'F': [Vertex('A', 14), Vertex('C', 2), Vertex('E', 9)],
    } 
    start = 'A'
    end = 'E'
    expected = {'distance': 20, 'path': ['A', 'C', 'F', 'E']}
    assert_that(find_shortest_path(graph, start, end), equal_to(expected))

 #
 #        F---9--E
 #       /|      |
 #      / |      |
 #     /  |      |
 #    14  2      6
 #   /    |      |
 #  /     |      |
 # A---9--C--11--D
 #  \     |     /
 #   \    |    /
 #    7  10   15
 #     \  |  /
 #      \ | /
 #       \|/
 #        B
 #
def test_finds_final_shortest_path_from_A_to_E():
    graph = {
        'A': [Vertex('C', 9), Vertex('F', 14)],
        'B': [Vertex('A', 7), Vertex('C', 10), Vertex('D', 15)],
        'C': [Vertex('A', 9), Vertex('B', 10), Vertex('D', 11), Vertex('F', 2)],
        'D': [Vertex('B', 15), Vertex('C', 11), Vertex('E', 6)],
        'E': [Vertex('D', 6), Vertex('F', 9)],
        'F': [Vertex('A', 14), Vertex('C', 2), Vertex('E', 9)],
    } 
    start = 'A'
    end = 'E'
    expected = {'distance': 20, 'path': ['A', 'C', 'F', 'E']}
    assert_that(find_shortest_path(graph, start, end), equal_to(expected))