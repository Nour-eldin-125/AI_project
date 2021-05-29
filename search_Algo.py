from Node import *



class Search():

    def __init__(self):
        pass

    # Dfs Search Algorithm :
    def dfs(self, graph, startNode, goalNode):

        if(startNode in goalNode):
            return startNode

        # Checking if the start node and the goal node in the graph or not

        if startNode not in graph.getNodes():
            print('\nError: start Node \'{}\' not exists!!'.format(startNode))
            return
        for g in goalNode:
            if (g not in graph.nodes):
                print('\nError: goal Node \'{}\' not exists!!'.format(g))
                return

        # Creating the visited and the fringe lists

        visited = []
        fringe = [startNode]
        while len(fringe) != 0:
            x = len(fringe) - 1
            n = fringe[x]
            fringe.pop(x)
            visited.append(n)

        # if this node is the goal then print the path to the node and the cost to reach it

            if n in goalNode:
                solList=self.getPath(graph,graph.nodes[n],startNode,visited)
                print('\nReached goal by DFS algorithm !! \nThe path is : {}'.format(solList))
                # getting a list of names of the visited nodes
                print('Cost : {}\nThe list of visited Nodes : {}\n'.format(self.getPathCost(graph, solList), visited))

                dict = {
                    'path': solList,
                    'cost': self.getPathCost(graph, solList),
                    'visit': visited
                }
                return dict

            # else append the node to the visited list and add its children to the fringe

            else:
                for c in graph.nodes[n].children:
                    if c.name not in visited:
                        fringe.append(c.name)
        print('\nDFS failed to get the goal')

    # Bfs Search Algorithm :
    def bfs(self, graph:Graph, startNode, goalNode):

        # Checking if the start node and the goal node in the graph or not

        if startNode not in graph.nodes:
            print('\nError: startNode \'{}\' not exists!!'.format(startNode))
            return
        for g in goalNode:
            if g not in graph.nodes:
                print('\nError: goal Node \'{}\' not exists!!'.format(g))
                return

        # Creating the visited and the fringe lists
        visited = []
        fringe = [startNode]
        while len(fringe) != 0:
            n = fringe[0]
            fringe.pop(0)
            visited.append(n)

            # if this node is the goal then print the path to the node and the cost to reach it
            if n in goalNode:

                solList = self.getPathBfs(graph,graph.nodes[n], startNode,visited)
                print('\nReached goal by BFS algorithm !! \nThe path is : {}'.format(solList))
                # Getting a list of names of the visited nodes

                print('Cost : {}\nThe list of visited Nodes : {}\n'.format(self.getPathCost(graph, solList), visited))

                dict = {
                    'path': solList,
                    'cost': self.getPathCost(graph, solList),
                    'visit': visited
                }
                return dict

            # else append the node to the visited list and add its children to the fringe

            else:
                for c in graph.nodes[n].children:
                    if (c.name not in visited) and (c.name not in fringe):
                        fringe.append(c.name)

        print('\nBFS failed to get the goal')
        return

    # Ucs search Algorithm :
    def ucs(self, graph, startNode, goalNode):
        fringe_dict={startNode: 0}
        visited={}

        while len(fringe_dict)!=0:
            fringe_dict = {k: v for k, v in sorted(fringe_dict.items(), key=lambda item: item[1])}

            list = []
            for l in fringe_dict.keys():
                list.append(l)
            item = list[0]
            cost = fringe_dict[item]
            fringe_dict.pop(item)
            visited[item] = cost
            v=[]
            for visit in visited.keys():
                v.append(visit)
            if (item in goalNode):

                print('goal is : {}'.format(item))
                print('cost is : {}'.format(cost))
                print('path is : {}'.format(self.getPathUCS(graph,graph.nodes[item],startNode,visited)))
                print('Visited Nodes are : {}'.format(visited))
                dict={
                    'path':self.getPathUCS(graph,graph.nodes[item],startNode,visited),
                    'cost':cost,
                    'visit':visited
                }
                return dict

            else:
                for i in graph.nodes[item].children:
                    if (i.name not in v):
                        if (i.name in fringe_dict):
                            if fringe_dict[i.name]>graph.getWeightEdge(item, i.name) + cost:
                                fringe_dict[i.name] = graph.getWeightEdge(item, i.name) + cost
                        else:
                            fringe_dict[i.name] = graph.getWeightEdge(item, i.name) + cost

                list.clear()
        print('failed to get the goal.')


    # Greedy Search Algorithm :

    def greedy(self, graph, startNode, goalNodes,heuristic_list:{}):

        # Checking if the start node and the goal node in the graph or not

        if startNode not in graph.getNodes():
            print('\nError: start Node \'{}\' not exists!!'.format(startNode))
            return
        for g in goalNodes:
            if (g not in graph.getNodes()):
                print('\nError: goal Node \'{}\' not exists!!'.format(g))
                return

        print("\nThe heuristic function of the graph is : {}".format(heuristic_list))
        fringe_dict = {startNode: heuristic_list[startNode]}
        visited = {}

        while fringe_dict is not None:
            # Sorts the fringe according to the heuristics of node
            fringe_dict = {k: v for k, v in sorted(fringe_dict.items(), key=lambda item: item[1])}

            list = []
            for l in fringe_dict.keys():
                list.append(l)
            # accessing the names in fringe by using a list (fringe_list)

            n = list[0]
            value = fringe_dict[n]
            del fringe_dict[n]
            visited[n]=value



            if n in goalNodes:
                print('the start node is : {}'.format(startNode))
                path = self.getPath_H_of_X(graph.nodes[n], startNode,heuristic_list,visited)
                print("Reached goal by Greedy algorithm !! \nThe path is : {}".format(path))
                print("Cost : {}".format(self.getPathCost(graph, path)))
                print("The list of visited Nodes : {}".format(visited))

                dict = {
                    'path': path,
                    'cost': self.getPathCost(graph, path),
                    'visit': visited
                }

                return dict
            else:
                for i in graph.nodes[n].children:
                    if (i.name not in visited.keys()):
                        fringe_dict[i.name] = heuristic_list[i.name]
                list.clear()
        print('\nfailed to get the goal ')


        # Greedy Search Algorithm :
    def aStar (self, graph, startNode, goalNode,heuristic_list:{}):
        fringe_dict = {startNode: 0+heuristic_list[startNode]}
        fringe_cost={startNode:0}
        visited = {}

        while len(fringe_dict) != 0:
            fringe_dict = {k: v for k, v in sorted(fringe_dict.items(), key=lambda item: item[1])}
            list = []
            for l in fringe_dict.keys():
                list.append(l)
            item = list[0]
            cost = fringe_cost[item]
            visited[item] = fringe_dict[item]
            fringe_dict.pop(item)

            v = []
            for visit in visited.keys():
                v.append(visit)
            if (item in goalNode):
                print('\ngoal is in A-Star: {}'.format(item))
                print('cost is : {}'.format(fringe_cost[item]))
                print('path is : {}'.format(self.getPathUCS(graph, graph.nodes[item], startNode, fringe_cost)))
                print('Visited Nodes are : {}'.format(visited))

                dict = {
                    'path': self.getPathUCS(graph, graph.nodes[item], startNode, fringe_cost),
                    'cost': fringe_cost[item],
                    'visit': visited
                }
                return dict

            else:
                for i in graph.nodes[item].children:
                    if (i.name not in v):
                        if (i.name in fringe_dict):
                            if fringe_dict[i.name] > graph.getWeightEdge(item, i.name) + cost:
                                fringe_cost[i.name] = graph.getWeightEdge(item, i.name) + cost
                                fringe_dict[i.name] = graph.getWeightEdge(item,i.name)+cost+heuristic_list[i.name]
                        else:
                            fringe_cost[i.name] = graph.getWeightEdge(item, i.name) + cost
                            fringe_dict[i.name] = graph.getWeightEdge(item, i.name) + cost + heuristic_list[i.name]
                list.clear()
        print('failed to get the goal.')

        # # Checking if the start node and the goal node in the graph or not
        #
        # if startNode not in graph.getNodes():
        #     print('\nError: start Node \'{}\' not exists!!'.format(startNode))
        #     return
        # for g in goalNodes:
        #     if (g not in graph.getNodes()):
        #         print('\nError: goal Node \'{}\' not exists!!'.format(g))
        #         return
        #
        # # creating an object from class Heuristics and calling f_of_X to calculate the summation of the H(x) and the
        # # G(x)
        #
        # print("\nThe F(x) function of the graph is : {}".format(h.optimalCostNodes))
        # fringe_dict = {startNode: h.optimalCostNodes[startNode]}
        # visited = []
        #
        # while fringe_dict is not None:
        #     # Sorts the fringe according to the heuristics of node
        #     fringe_dict = {k: v for k, v in sorted(fringe_dict.items(), key=lambda item: item[1])}
        #
        #     fringe_list = []
        #     for j in fringe_dict.keys():
        #         fringe_list.append(j)
        #     n = fringe_list[0]
        #     del fringe_dict[n]
        #     visited.append(n)
        #
        #     if n in goalNodes:
        #         path = self.getPath(graph.nodes[n], startNode)
        #         print("Reached goal by A* algorithm !! \nThe path is : {}".format(path))
        #         print("Cost : {}".format(self.getPathCost(graph, path)))
        #         print("The list of visited Nodes : {}".format(visited))
        #         return
        #     else:
        #         for j in graph.nodes[n].children:
        #             if not (j.name in visited):
        #                 fringe_dict[j.name] = [h.nodes[j.name]]
        #                 fringe_list.clear()
        # print('\nfailed to get the goal ')
        # return

    # ===========================================================
    #                   Extra functions :
    # ===========================================================

    # Getting the path to the goal from the start
    def getPath(self,graph:Graph, node, start,visited:[]):
        solList = []
        v=len(visited)-2
        while node.name != start:
            solList.append(node.name)
            c=0
            while v >= 0:
                if visited[v] in node.parentName:
                    node=graph.nodes[visited[v]]
                    c=v
                    break
                v-=1
            v=c
        solList.append(node.name)
        solList.reverse()
        return solList

    def getPathBfs(self, graph: Graph, node, start, visited: []):
        solList = []
        while node.name != start:
            solList.append(node.name)
            for v in visited:
                if (v in node.parentName):
                    node = graph.nodes[v]
                    break
        solList.append(node.name)
        solList.reverse()
        return solList

    def getPathUCS(self, graph: Graph, startNode:Node, start, visited: {}):
        solList = []
        visit=[]
        for v in visited.keys():
            visit.append(v)
        while startNode.name != start:
            solList.append(startNode.name)
            if len(startNode.parentName)==1:
                startNode=startNode.parent[0]
                continue
            for p in startNode.parent:
                    if (p.name not in visit):
                        continue
                    elif (visited[p.name] == visited[startNode.name] - graph.getWeightEdge(p.name, startNode.name)):
                        startNode = p
                        break
        solList.append(startNode.name)
        solList.reverse()
        return solList

    def getPath_H_of_X(self, startNode:Node, start, heu: {},visit:{}):
        solList = []
        value=''
        while startNode.name != start:
            solList.append(startNode.name)
            min = 9999
            print(solList)
            for p in startNode.parent:
                if p.name in visit:
                    if min > heu[p.name]:
                        if (p == value) or p.name in solList:
                            continue
                        if (p in startNode.children):
                            value = startNode

                        min = heu[p.name]
                        temp = p
                else:
                    continue
            startNode = temp
        solList.append(startNode.name)
        solList.reverse()
        return solList

    def getPath_F_of_X(self, graph: Graph, startNode, start, visited: {}):
        solList = []
        v = len(visited) - 2
        while startNode.name != start:
            solList.append(startNode.name)
            min = 9999
            for p in startNode.parent:
                if (min>visited[p.name]+graph.getWeightEdge(p.name,startNode.name)):
                    min=visited[p.name]
                    temp=p
            startNode=temp
        solList.append(startNode.name)
        solList.reverse()
        return solList

    # Getting the cost of the path from the Start node to the goal node/Nodes
    def getPathCost(self, graph, list):
        cost = 0
        for x in range(0, len(list) - 1):
            cost += graph.getWeightEdge(list[x], list[x + 1])
        return cost
