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
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
        else:
            print("Warning, vertex exists")

    def add_edge(self, vertex_from, vertex_to):
        """
        Add a directed edge to the graph.
        """
        if vertex_from in self.vertices and vertex_to in self.vertices:
            self.vertices[vertex_from].add(vertex_to)
        else:
            print("Warning, supplied vertex does not exist")
            # TODO

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()

        q.enqueue(starting_vertex)

        found = [starting_vertex]

        while q.size() > 0:
            for vertex in self.vertices[q.queue[0]]:
                if vertex not in found:
                    q.enqueue(vertex)
                    found.append(vertex)
            q.dequeue()
        print(f'BFT: {found}')

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()

        s.push(starting_vertex)

        found = []

        while s.size() > 0:
            current = s.pop()
            if current not in found:
                found.append(current)
                for next_vert in self.vertices[current]:
                    s.push(next_vert)

            # for vertex in self.vertices[s.stack[-1]]:
            #     if vertex not in found:
            #         s.push(vertex)
            #         found.append(vertex)

        print(f'DFT: {found}')

    def dft_recursive(self, starting_vertex, path=[]):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """

        path += [starting_vertex]

        for vertex in self.vertices[starting_vertex]:
            if vertex not in path:
                path = self.dft_recursive(vertex, path)

        return path

        # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()

        q.enqueue([starting_vertex])

        found = []

        while q.size() > 0:
            print(f'queue before dequeue = {q}')
            path = q.dequeue()
            print(f'path = {path}')
            v = path[-1]
            print(f'v = {v}')

            if v not in found:
                if v == destination_vertex:
                    return path

                found.append(v)
                print(f'found = {found}')
                print()
                for next_vert in self.vertices[v]:
                    print(f'v = {v}')
                    print(f'self.vertices[v] = {self.vertices[v]}')
                    print(f'next_vert = {next_vert}')
                    new_path = list(path)
                    print(f'new_path = {new_path}')
                    new_path.append(next_vert)
                    print(f'new_path = {new_path}')
                    q.enqueue(new_path)
                    print(f'queue with new_path = {q}')

            # for vertex in self.vertices[q.queue[0]]:
            #     if vertex == destination_vertex:
            #         q.enqueue(vertex)
            #         found.append(vertex)
            #         break
            #     elif vertex not in found:
            #         q.enqueue(vertex)
            #         found.append(vertex)
            # q.dequeue()
        # print(f'BFT solution: {found}')

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()

        s.push([starting_vertex])

        found = []

        while s.size() > 0:
            path = s.pop()
            v = path[-1]

            if v not in found:
                if v == destination_vertex:
                    return path
                found.append(v)
                for next_vert in self.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    s.push(new_path)


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
    # graph.dft(1)

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
    # graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # print(f'DFT Recursion: {graph.dft_recursive(1)}')

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(f'BFS: {graph.bfs(1, 6)}')

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(f'DFS: {graph.dfs(1, 6)}')
