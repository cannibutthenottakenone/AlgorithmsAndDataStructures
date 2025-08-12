# Find the Strongly Connected Component of a Graphs using Kosaraju's algorithm

from Graphs import Graph
from LinearStructures import Stack


# Create the transposed graph
def getTranspose(graph):
    gt = Graph()
    for vert1 in graph:
        for vert2 in vert1.getConnections():
            gt.addEdge(vert2.getId(), vert1.getId())
    return gt


def dfsvisit(graph, startVertex, st):
    startVertex.setColor('gray')
    graph.time += 1
    startVertex.setDiscovery(graph.time)
    for nextVertex in startVertex.getConnections():
        if nextVertex.getColor() == 'white':
            nextVertex.setPred(startVertex)
            dfsvisit(graph, nextVertex, st)
    startVertex.setColor('black')
    graph.time += 1
    startVertex.setFinish(graph.time)
    # save in the stack the ID of the vertex
    st.push(startVertex.getId())


# Perform the first DFS on all the vertex in order and fill the stack
def dfs1(graph, st):
    for aVertex in graph:
        if aVertex.getColor() == 'white':
            dfsvisit(graph, aVertex, st)


# Perform the second DFS and print the SCC
def dfs2(graph, st):
    scc = Stack()
    counter = 0
    while not st.isEmpty():
        startVertex = graph.getVertex(st.pop())
        if startVertex.getColor() == 'white':
            dfsvisit(graph, startVertex, scc)
            counter += 1
            # empty the stack and print the SCC
            print("SCC", counter, end=': ')
            while not scc.isEmpty():
                print(scc.pop(), end=' ')
            print("")


def getSCC(graph):
    st = Stack()
    # Call the first DFS to fill in the stack
    dfs1(graph, st)
    # Create the transposed graph
    trGraph = getTranspose(graph)
    # Run the second DFS to find and print the SCC
    dfs2(trGraph, st)


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

    # myGraph.addEdge("A", "C")
    # myGraph.addEdge("C", "D")
    # myGraph.addEdge("D", "E")
    # myGraph.addEdge("E", "A")
    # myGraph.addEdge("E", "B")
    # myGraph.addEdge("B", "F")
    # myGraph.addEdge("F", "G")
    # myGraph.addEdge("G", "B")

    getSCC(myGraph)