from DS.Graph.graph import *

class Graph(Graph):
    def breadth_first(self, vertex):
        tree = []
        b_first = [vertex]
        visited = set()

        visited.add(vertex)

        while b_first:
            front = b_first.pop(0)
            tree.append(front)

            for neighbor in self.get_neighbors(front):
                if neighbor.vertex not in visited:
                    visited.add(neighbor)
                    b_first.append(neighbor.vertex)

        return tree
