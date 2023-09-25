import sys


class Vertex:
    def __init__(self, key):
        self._id = key  # the id of the node
        self._connectedTo = {}  # the list of neighbors
        self._color = 'white'   # used by BFS and DFS
        self._distance = sys.maxsize  # distance used by BFS and Dijkstra's algorithm
        self._k = sys.maxsize   # attribute used by Prim's algorithm
        self._pred = None  # memorize the predecessor of the current vertex
        self._disc = 0  # discovery time, used by DFS
        self._fin = 0   # finish time, used by DFS

    def addNeighbor(self, nbr, weight=0):
        self._connectedTo[nbr] = weight

    def __str__(self):
        return str(self._id) + ' connectedTo: ' + str([x._id for x in self._connectedTo])

    def getConnections(self):
        return self._connectedTo.keys()

    def getId(self):
        return self._id

    def getWeight(self, nbr):
        return self._connectedTo[nbr]

    def setPred(self, p):
        self._pred = p

    def getPred(self):
        return self._pred

    def setColor(self, col):
        if col == "white" or col == "black" or col == "gray":
            self._color = col

    def getColor(self):
        return self._color

    def setDistance(self, dist):
        self._distance = dist

    def getDistance(self):
        return self._distance

    def setK(self, k):
        self._k = k

    def getK(self):
        return self._k

    def setDiscovery(self, dtime):
        self._disc = dtime

    def setFinish(self, ftime):
        self._fin = ftime

    def getFinish(self):
        return self._fin

    def getDiscovery(self):
        return self._disc


class Graph:
    def __init__(self, indirect=False):
        self.vertList = {}
        self.numVertices = 0
        self.indirect = indirect
        self.time = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):

        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], weight)
        if self.indirect:  # if the graph is indirect the edges are bidirectional
            self.vertList[t].addNeighbor(self.vertList[f], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


if __name__ == "__main__":
    g = Graph()
    for i in range(6):
        g.addVertex(("v%d" % i))

    g.addEdge("v0", "v1", 5)
    g.addEdge("v0", "v5", 2)
    g.addEdge("v1", "v2", 4)
    g.addEdge("v2", "v3", 9)
    g.addEdge("v3", "v4", 7)
    g.addEdge("v3", "v5", 3)
    g.addEdge("v4", "v0", 1)
    g.addEdge("v5", "v4", 8)
    g.addEdge("v5", "v2", 1)

    for v in g:
        print(v)
        # for w in v.getConnections():
        #    print("( %s , %s )" % (v.getId(), w.getId()))
