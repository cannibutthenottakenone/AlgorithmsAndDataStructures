# Find the Strongly Connected Component of a Graph using Kosaraju's algorithm:

# - Perform DFS traversal of the graph. Push node to stack as soon as becomes black
# - Create the transpose graph by reversing the edges
# - Pop nodes one by one from the stack and again to DFS on the modified graph
# - Print the connected components


from Graphs import Graph
from LinearStructures import Stack

# Method for creating the transposed graph
#
# TODO
#


# Standard DFS Visit implementation to be modified
def dfsvisit(graph, startVertex):
    startVertex.setColor('gray')
    graph.time += 1
    startVertex.setDiscovery(graph.time)
    for nextVertex in startVertex.getConnections():
        if nextVertex.getColor() == 'white':
            nextVertex.setPred(startVertex)
            dfsvisit(graph, nextVertex)
    startVertex.setColor('black')
    graph.time += 1
    startVertex.setFinish(graph.time)


# First DFS, fill the stack in inverted finishing order
# HERE THE STANDARD IMPLEMENTATION TO BE MODIFIED
def dfs1(graph):
    for aVertex in graph:
        if aVertex.getColor() == 'white':
            dfsvisit(graph, aVertex)


# Second DFS, find and print the SCC
# HERE THE STANDARD IMPLEMENTATION TO BE MODIFIED
def dfs2(graph):
    for aVertex in graph:
        if aVertex.getColor() == 'white':
            dfsvisit(graph, aVertex)


# Method that run the algorithm
def getSCC(graph):

    st = Stack()

    # Call to the first DFS
    #
    # TODO
    #

    # Call to transpose method
    #
    # TODO
    #

    # Call to the second DFS
    #
    # TODO
    #


# Test code
if __name__ == "__main__":
    myGraph = Graph()
    myGraph.addEdge("A", "B")
    myGraph.addEdge("B", "C")
    myGraph.addEdge("D", "B")
    myGraph.addEdge("C", "C")
    myGraph.addEdge("B", "E")
    myGraph.addEdge("C", "F")
    myGraph.addEdge("D", "G")
    myGraph.addEdge("E", "A")
    myGraph.addEdge("E", "D")
    myGraph.addEdge("F", "H")
    myGraph.addEdge("G", "E")
    myGraph.addEdge("H", "I")
    myGraph.addEdge("I", "F")

    getSCC(myGraph)