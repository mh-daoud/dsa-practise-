#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)
    
    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)

    def topologicalSort(self):
        vistied = []
        stack = []
        for vertex in self.gdict.keys() :
            if vertex not in vistied:
                self.topologicalSort_helper(vistied,stack, vertex)
        print(stack)

    def topologicalSort_helper(self,vistied,stack,vertex):
        vistied.append(vertex)
        for adjacentVertex in self.gdict[vertex]:
            if adjacentVertex not in vistied:
                self.topologicalSort_helper(vistied,stack,adjacentVertex)

        stack.append(vertex)



customDict = { "a" : ["c"],
            "b" : ["c","d"],
            "c" : ["e"],
            "d" : ["f"],
            "e" : [ "h","f"],
            "f" : ["g"],
            "g" : [],
            "h" : [],
               }



g = Graph(customDict)
g.topologicalSort()

