from util import Queue


class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, vertex_from, vertex_to):
        if vertex_from in self.vertices and vertex_to in self.vertices:
            self.vertices[vertex_from].add(vertex_to)


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for link in ancestors:
        graph.add_vertex(link[0])
        graph.add_vertex(link[1])
        graph.add_edge(link[0], link[1])
    print(graph.vertices)

    q = Queue()
    longest_list = 0
    furthest_ancestor = -1
    for parent in graph.vertices:
        q.enqueue([parent])
        found = []
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]

            if v not in found:
                if v == starting_node:
                    if len(path) > longest_list:
                        longest_list = len(path)
                        furthest_ancestor = parent
                    else:
                        break
                found.append(v)
                for next_vert in graph.vertices[v]:
                    new_path = list(path)
                    new_path.append(next_vert)
                    q.enqueue(new_path)
    if furthest_ancestor == starting_node:
        furthest_ancestor = -1
    print(furthest_ancestor)
    return furthest_ancestor


if __name__ == '__main__':
    graph = Graph()
