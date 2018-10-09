class Node(object):
    def __init__(self, id, name, pageRank = 0):
        self.id = id
        self.name = name
        self.adj = {}
        self.invAdj = {}
        self.connected = 0
        self.pageRank = pageRank

    def addConnection(self, node, cost):
        self.adj[node.id] = [cost, node]
        node.invAdj[self.id] = self
        self.connected += 1

    def updatePageRank(self, d = 0.85):
        accum = 0
        for node in self.invAdj.values():
            accum += node.pageRank / node.connected
        self.pageRank = (1 - d) + (d) * accum


class Graph (object):
    def __init__(self, name="Graph"):
        self.name = name
        self.size = 0
        self.nodes = {}

    def insertNode(self, node):
        self.nodes[node.id] = node
        self.size += 1

    def pageRank(self, iterations = 0):
        keys = self.nodes.keys()
        for _ in range(iterations):
            for key in keys:
                self.nodes[key].updatePageRank(d=0.85)
        pageRankDictionary = {}
        for key in keys:
            pageRankDictionary[self.nodes[key].name] = self.nodes[key].pageRank
        keyValue = zip(pageRankDictionary.keys(), pageRankDictionary.values())
        return dict(sorted(keyValue, key = lambda x: x[1], reverse=True))

    def fromCSV(self, pathToNodes, pathToEdges):
        import pandas as pd
        csvNodes = pd.read_csv(pathToNodes)
        for i, row in csvNodes.iterrows():
            self.insertNode(Node(row['id'], row['label']))
        csvEdges = pd.read_csv(pathToEdges)
        for i, row in csvEdges.iterrows():
            self.nodes[row['Source']].addConnection(self.nodes[row['Target']], 1)
