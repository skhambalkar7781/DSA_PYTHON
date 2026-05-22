class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.matrix = [[0 for _ in range(vertices)]
                       for _ in range(vertices)]
    
    def display(self):
        for row in self.matrix:
            print(row)
            
    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

g = Graph(4)
# g.display()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.display()
