"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.
        """
        # add the vertex into vertices Set.
        # give it value of empty set
        self.vertices[vertex] = set()
        # later on we'll add neighbouring vertices into this set

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if both vertices exist in our graph
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            # if they don't exist, rais an error
            raise IndexError("The vertex does not exist in the graph")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create an empty queue
        q = Queue()
        # enqueue the staring vertex
        q.enqueue(starting_vertex)
        # Create a Set to store the visited nodes
        visited = set()
        # While the queue is not empty
        while q.size() > 0:
            # take the last node from the queue (First added)
            current_node = q.queue[0]
            print(f'bft: {current_node}')
            # if the first node has not been visited
            if current_node not in visited:
                # add all of it's neighbours to the back of the queue
                for neighbour in self.vertices[current_node]:
                    q.enqueue(neighbour)

                # mark it as visited
                visited.add(current_node)
            # remove it from que
            q.dequeue()
        # print(f'bft path: {visited}')

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            pop = s.pop()

            if pop not in visited:
                print(f'DFT: {pop}')
                visited.add(pop)

                for neighbour in self.vertices[pop]:
                    s.push(neighbour)
        # print(f'DFT visited: {visited}')

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """

        # if the visited not supplied make new set (to fix a python gotcha)
        if visited is None:
            visited = set()
        # Add starting vert to the visited set and print the it
        visited.add(starting_vertex)
        print(starting_vertex)

        # loop over each of the verts children
        for child in self.vertices[starting_vertex]:
            # if the child is not in the visited set
            if child not in visited:
                # recursively call dft on the child and visited set
                self.dft_recursive(child, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create new queue
        que = Queue()
        # add starting vertex value into queue. set first path as an empty Set
        que.enqueue({"value": starting_vertex, "path": set()})

        # create visited set to keep track of visited nodes
        visited = set()

        # loop until the queue is empty
        while que.size() > 0:
            # get the next node in queue (the one first in que - FIFO)
            next_in_que = que.queue[0]
            # see if we already visited this node
            if next_in_que["value"] not in visited:
                # if we did not visit this node yet
                # add it to the visited list
                visited.add(next_in_que["value"])

                # if this node is destination node
                if next_in_que["value"] == destination_vertex:
                    # add its value to the path set, so it containts the last node
                    next_in_que["path"].add(next_in_que["value"])
                    # and return PATH
                    return next_in_que["path"]

                # else add all neighbouring nodes to queue
                for neighbour in self.vertices[next_in_que["value"]]:
                    # Make a COPY of the PATH set from current node to neighbour nodes
                    path_to_neighbour = next_in_que["path"].copy()
                    # and add the current node value into it, so neighbouring nodes have path to "parent" node
                    path_to_neighbour.add(next_in_que["value"])

                    # add neighbouring node to queue
                    que.enqueue(
                        {"value": neighbour, "path": path_to_neighbour})

            # remove current node from queue
            que.dequeue()

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = Stack()
        stack.push({"value": starting_vertex, "path": set()})

        visited = set()

        while stack.size() > 0:
            current_node = stack.stack[-1]
            cn_value = current_node["value"]
            cn_path = current_node["path"]

            # Remove current node from stack before you add
            # neighbour nodes in stack
            stack.pop()

            if cn_value not in visited:
                visited.add(cn_value)

                if cn_value == destination_vertex:
                    # add current node as the last node in PATH
                    cn_path.add(cn_value)
                    return cn_path

                for neighbour in self.vertices[cn_value]:
                    neighbour_path = cn_path.copy()
                    neighbour_path.add(cn_value)

                    if neighbour == destination_vertex:
                        neighbour_path.add(neighbour)
                        return neighbour_path
                    else:
                        stack.push(
                            {"value": neighbour, "path": neighbour_path})


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
