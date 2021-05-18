from Node import *
from priority_queue import PriorityQueue

class Huristcis():

    def __init__(self):
        self.nodes = {}

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
                        print(p.name, self.nodes[p.name])

            else:
                self.nodes[n]=len(list)
            visited.append(n)
            l=graph.nodes[n].children
            for j in l:
                if (j.name not in visited):
                    fringe.append(j.name)
            print ('fringe is : {}'.format(fringe))
            print('visited is : {}'.format(visited))
            print ('huristics is : {}'.format(self.nodes[n]))





