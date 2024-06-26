# simple Adjacency Matrix implementation

class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2, weight=1):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = weight
        # remove the line if the graph is direct
        self.adjMatrix[v2][v1] = weight

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        # remove the line if the graph is direct
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            print(row)


def main():
    g = Graph(5)
    g.add_edge(0, 1, 5)
    g.add_edge(0, 2, 6)
    g.add_edge(1, 2, 7)
    g.add_edge(2, 0, 4)
    g.add_edge(2, 3, 3)
    g.add_edge(3, 4, 1)

    g.print_matrix()


if __name__ == '__main__':
    main()