from queue import Queue

# PROBLEM:
"""
Suppose we have some input data describing a graph of relationships between parents and children over multiple generations.
The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.

Write a function that, given the dataset and the ID of an individual in the dataset,
returns their earliest known ancestor – the one at the farthest distance from the input individual.

If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID.
If the input individual has no parents, the function should return -1.
"""
input_ID = 6
input_list = [
    [1, 3],
    [2, 3],
    [3, 6],
    [5, 6],
    [5, 7],
    [4, 5],
    [4, 8],
    [8, 9],
    [11, 8],
    [10, 1]
]


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_nodes_and_edges(self, node_list):
        for i in node_list:
            parent = i[0]
            child = i[1]

            if parent not in self.vertices:
                self.vertices[parent] = set()
            if child not in self.vertices:
                self.vertices[child] = set()

            self.vertices[parent].add(child)


g = Graph()
g.add_nodes_and_edges(input_list)

print(g.vertices)
