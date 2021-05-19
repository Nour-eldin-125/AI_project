from Node import *


class Huristcis():

    def __init__(self):
        self.nodes = {}
        self.optimalCostNodes={}

    def getHuristic(self, graph:Graph, start, goal):
        for g in goal:
            graph.nodes[g].goal = True
        visited = []
        fringe = [start]
        while len(fringe) != 0:
            n = fringe[0]
            fringe.pop(0)

            list=ucs_search(graph=graph,name_node_start= n,name_node_goal= goal)
            if (list==None):
                if n in goal:
                    self.nodes[n]=0
                else:
                    p = graph.nodes[n].parent
                    if (p.name in self.nodes):
                        self.nodes[n] = self.nodes[p.name] + 1

            else:
                self.nodes[n]=len(list)-1
            visited.append(n)
            l=graph.nodes[n].children
            for j in l:
                if (j.name not in visited):
                    fringe.append(j.name)

        return self.nodes

    def F_of_X (self,graph,start,goal):
        for g in goal:
            graph.nodes[g].goal = True
        self.getHuristic(graph,start,goal)
        visited = []
        fringe = [start]
        while len(fringe) != 0:
            n = fringe[0]
            fringe.pop(0)
            if (n in goal):
                self.optimalCostNodes [n]=getPathCost(graph,getPath(graph.nodes[n],start))
            else:
                self.optimalCostNodes [n]= self.nodes[n] + getPathCost(graph,getPath(graph.nodes[n],start))
            visited.append(n)
            l=graph.nodes[n].children
            for j in l:
                if (j.name not in visited):
                    fringe.append(j.name)

        return self.optimalCostNodes
