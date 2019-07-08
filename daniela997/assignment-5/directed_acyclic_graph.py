import collections


class DirectedAcyclicGraph:
    """
    We represent a DAG via adjacency matrix: if there is an edge from
    vertex A to vertex B, we mark matrix[A][B]; this does NOT mean
    that matrix[B][A] is also marked, since the graph is directed
    """
    def __init__(self):
        """
        Represent adjacency matrix as a dictionary of lists.
        """
        self.vertices = collections.defaultdict(list)

    def add_edge(self, from_vertex, to_vertex):
        """
        Add an edge from one vertex to another by appending
        the vertex for which the edge is incoming to the adjacency list
        of the vertex for which it is outgoing.
        :param from_vertex: Vertex to which the edge is outgoing
        :param to_vertex: Vertex to which the edge is incoming
        """
        self.vertices[from_vertex] += [to_vertex]

    def __topological_sort_recursion(self, vertex, visited, stack):
        """
        Recursive part of topological sort.
        :param vertex: current starting vertex for traversal
        :param visited: vertices already visited
        :param stack: vertices ordered topologically
        :return:
        """
        # If the current vertex has been visited skip it - O(1)
        if vertex in visited:
            return

        # Mark vertex as visited - this is O(1) since visited is a dict
        visited[vertex] = True

        # Walk each adjacent vertex (every vertex that the
        # current one has an outgoing edge to)
        if vertex in self.vertices:
            for adjacent_vertex in self.vertices[vertex]:
                self.__topological_sort_recursion(adjacent_vertex, visited, stack)

        # When recursion returns add vertex to result stack
        stack.append(vertex)

    def topological_sort(self):
        """
        Find an order such that for every directed edge uv from vertex u to vertex v,
        u comes before v in the ordering.
        :return: vertices sorted topologically
        """
        # To keep track of visited vertices, initially all are unvisited
        visited_vertices = collections.defaultdict(lambda: False)
        stack = []

        # For each vertex in the graph perform recursive topological sort
        for vertex in list(self.vertices.keys())[::1]:
            self.__topological_sort_recursion(vertex, visited_vertices, stack)

        return stack
