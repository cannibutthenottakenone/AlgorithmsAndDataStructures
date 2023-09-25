# Verify if an undirected graph is a tree
#
# An undirected graph is a tree if the following conditions are verified:
# - There are no cycles
# - The graph is connected
#
# HINTS: You can use DFS to perform both the verifications!

from Graphs import Graph


# Return True if the graph is a tree, false otherwise
def isTree(graph):

    # reset all vertices to white
    for aVertex in graph:
        aVertex.setColor('white')
        aVertex.setPred(-1)

    # get the first vertex of the graph
    keys = list(graph.getVertices())
    aVertex = graph.getVertex(keys[0])

    # Cycle verification
    if _isCyclic(graph, aVertex):
        # print("Cycle found")
        return False

    # Disconnection verification
    # If there are still white vertices after a single DFS the graph is disconnected
    for aVertex in graph:
        if aVertex.getColor() == 'white':
            # print("The graph is disconnected")
            return False

    return True


# Check if a graph contains cycle(s) using DFS
# Return True if there is at least one cycle
def _isCyclic(graph, startVertex):
    startVertex.setColor('gray')

    for nextVertex in startVertex.getConnections():

        # If one of the neighbors is gray and it is not the predecessor of the current node there is a cycle
        if nextVertex.getColor() == 'gray' and nextVertex is not startVertex.getPred():
            return True

        if nextVertex.getColor() == 'white':
            nextVertex.setPred(startVertex)

            # Recursive check
            if _isCyclic(graph, nextVertex):
                return True

    startVertex.setColor('black')

    return False


if __name__ == "__main__":

    # WARNING: DO NOT MODIFY THE GRAPH STRUCTURE!
    g1 = Graph(True)

    g1.addEdge("v0", "v1")
    g1.addEdge("v1", "v2")
    g1.addEdge("v1", "v3")
    g1.addEdge("v3", "v4")
    g1.addEdge("v2", "v0")  # this line creates a cycle

    # WARNING: DO NOT MODIFY THE GRAPH STRUCTURE!
    g2 = Graph(True)

    g2.addEdge("v0", "v1")
    g2.addEdge("v1", "v2")
    g2.addEdge("v1", "v3")
    g2.addEdge("v3", "v4")
    g2.addEdge("v5", "v6")  # this line creates a disconnected graph

    # WARNING: DO NOT MODIFY THE GRAPH STRUCTURE!
    g3 = Graph(True)

    g3.addEdge("v0", "v1")
    g3.addEdge("v1", "v2")
    g3.addEdge("v1", "v3")
    g3.addEdge("v3", "v4")
    g3.addEdge("v5", "v4")

    # Expected result = FALSE
    print(isTree(g1))

    # Expected result = FALSE
    print(isTree(g2))

    # Expected result = TRUE
    print(isTree(g3))

