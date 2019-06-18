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
            parent = i[1]
            child = i[0]

            if parent not in self.vertices:
                self.vertices[parent] = set()
            if child not in self.vertices:
                self.vertices[child] = set()

            self.vertices[parent].add(child)

    def find_ancestor(self, node):

        ancestor_distance = []
        earliest_ancestor = None

        q = Queue()
        q.enqueue([node, ancestor_distance])
        visited = set()

        print(f'node: {node}, que: {q.queue}, size: {q.size()}')

        while q.size() > 0:
            # get next item from queue
            current_node = q.queue[0]
            cn_val = current_node[0]
            cn_path = current_node[1]

            print(f'\nNext in queue = {current_node}')

            # check if we did not visit this node yet
            if cn_val not in visited:
                visited.add(cn_val)

                print(f'parents: {self.vertices[cn_val]}')

                for parent in self.vertices[cn_val]:
                    parent_path = cn_path.copy()
                    parent_path.append(cn_val)

                    if len(parent_path) > len(ancestor_distance):
                        ancestor_distance = parent_path
                        if earliest_ancestor == None or parent <= earliest_ancestor:
                            earliest_ancestor = parent

                    q.enqueue([parent, parent_path])

            print(f'cn path vs anc_dist: {cn_path} - {ancestor_distance}')
            if len(cn_path) >= len(ancestor_distance):
                cn_path.append(cn_val)
                ancestor_distance = cn_path
                earliest_ancestor = cn_val

            q.dequeue()
            print(f'anc: {earliest_ancestor}, dist: {ancestor_distance}')
            print(f'QUE: {q.queue}\n')

        return earliest_ancestor


g = Graph()
g.add_nodes_and_edges(input_list)

print(g.vertices)
print(g.find_ancestor(input_ID))
