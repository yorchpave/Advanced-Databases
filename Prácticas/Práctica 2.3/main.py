from Graph import *

if __name__ == '__main__':
    myGraph = Graph("Pages")
    myGraph.fromCSV("Oracle_Nodes.csv", "Oracle_Edges.csv")

    print("PageRank Results: \n")
    pageRank = myGraph.pageRank(50)
    for key, value in zip(pageRank.keys(), pageRank.values()):
        print(key + "\t\t" + str(value))

    del myGraph
