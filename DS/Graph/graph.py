from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.append(value)

    def dequeue(self):
        return self.dq.popleft()

    def __len__(self):
        return len(self.dq)

class Vertex:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value

class Edge:
    """Each Edge contains a vertex and the weight of the edge"""
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.__adj_list = {}

    def add_node(self, value):
        """ Add the node to adj_list as key and value it will be an empty list"""
        vertex = Vertex(value)
        self.__adj_list[vertex] = []
        return vertex

    def add_edge(self, i_vertex, f_vertex, weight=0):
        if i_vertex not in self.__adj_list:
            raise KeyError('Initial vertex is not found')
        if f_vertex not in self.__adj_list:
            raise KeyError('Final vertex in not found')
        edge = Edge(f_vertex, weight)
        self.__adj_list[i_vertex].append(edge)

    def get_nodes(self):
        return self.__adj_list.keys()

    def size(self):
        return len(self.__adj_list)

    def get_neighbors(self, vertex):
        return self.__adj_list.get(vertex, [])

    def breadth_first(self, i_vertex):
        graph = []
        visited = set()
        q = Queue()

        q.enqueue(i_vertex)
        visited.add(i_vertex)

        while len(q):
            current_vertex = q.dequeue()
            graph.append(current_vertex.value)
            neighbors = self.get_neighbors(current_vertex)
            for edge in neighbors:
                neighbor = edge.vertex
                if neighbor not in visited:
                    q.enqueue(neighbor)
                    visited.add(neighbor)

        return graph



if __name__ == "__main__":
    g = Graph()
    a = g.add_node('A')
    b = g.add_node('B')
    e = g.add_node('E')
    c = g.add_node('C')
    d = g.add_node('D')
    g.add_edge(a, b)
    g.add_edge(b, a)
    g.add_edge(a, e)
    g.add_edge(e, a)
    g.add_edge(a, c)
    g.add_edge(b, d)
    g.add_edge(b, e)
    g.add_edge(e, d)
    g.add_edge(e, c)

    print(g.breadth_first(a))
    print('*' * 50)
    print(g.get_neighbors(b.value))




