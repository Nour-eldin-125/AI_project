from Node import *
from heuristic import Huristcis


class Search():

    def __init__(self):
        pass

    # Dfs Search Algorithm :
    def dfs(self, graph, startNode, goalNode):

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
        fringe = [graph.nodes[startNode]]
        while len(fringe) != 0:
            x = len(fringe) - 1
            n = fringe[x]
            fringe.pop(x)
            visited.append(n)

        # if this node is the goal then print the path to the node and the cost to reach it

            if n.name in goalNode:
                solList = self.getPath(n, startNode)
                print('\nReached goal by DFS algorithm !! \nThe path is : {}'.format(solList))
                # getting a list of names of the visited nodes
                list = []
                for v in visited:
                    list.append(v.name)
                print('Cost : {}\nThe list of visited Nodes : {}\n'.format(self.getPathCost(graph, solList), list))
                return

            # else append the node to the visited list and add its children to the fringe

            else:
                for c in n.children:
                    found = False
                    for v in visited:
                        if v.name == c.name:
                            found = True
                    if found:
                        continue
                    else:
                        fringe.append(c)
        print('\nDFS failed to get the goal')
        return

    # Bfs Search Algorithm :
    def bfs(self, graph, startNode, goalNode):

        # Checking if the start node and the goal node in the graph or not

        if startNode not in graph.nodes:
            print('\nError: startNode \'{}\' not exists!!'.format(startNode))
            return
        for g in goalNode:
            if (g not in graph.nodes):
                print('\nError: goal Node \'{}\' not exists!!'.format(g))
                return

        # Creating the visited and the fringe lists

        visited = []
        fringe = [graph.nodes[startNode]]
        while len(fringe) != 0:
            n = fringe[0]
            fringe.pop(0)
            visited.append(n)
            # if this node is the goal then print the path to the node and the cost to reach it

            if n.name in goalNode:
                solList = self.getPath(n, startNode)
                print('\nReached goal by BFS algorithm !! \nThe path is : {}'.format(solList))
                # Getting a list of names of the visited nodes
                list = []
                for v in visited:
                    list.append(v.name)
                print('Cost : {}\nThe list of visited Nodes : {}\n'.format(self.getPathCost(graph, solList), list))
                return

            # else append the node to the visited list and add its children to the fringe

            else:
                for c in n.children:
                    found = False
                    for v in visited:
                        if v.name == c.name:
                            found = True
                    if found:
                        continue
                    else:
                        fringe.append(c)
        print('\nDFS failed to get the goal')
        return

    # Ucs search Algorithm :
    def ucs(self, graph, startNode, goalNode):

        # Checking if the start node and the goal node in the graph or not

        if startNode not in graph.getNodes():
            print('\nError: start Node \'{}\' not exists!!'.format(startNode))
            return
        for g in goalNode:
            if (g not in graph.getNodes()):
                print('\nError: goal Node \'{}\' not exists!!'.format(g))
                return
        # creating a dict fringe to store the nodes and its cost and a list of visited nodes to store the node names

        fringe_dict = {startNode: 0}
        visited = []

        while len(fringe_dict) != 0:
            # Sorts the fringe according to the cost of node
            fringe_dict = {k: v for k, v in sorted(fringe_dict.items(), key=lambda item: item[1])}
            fringe_list = []
            for j in fringe_dict.keys():
                fringe_list.append(j)
            n = fringe_list[0]
            del fringe_dict[n]
            visited.append(n)
            # if node is the goal stop and print the path and cost

            if n in goalNode:
                path = getPath(graph.nodes[n], startNode)
                print("Reached goal by UCS algorithm !! \nThe path is : {}".format(path))
                print("Cost : {}".format(getPathCost(graph, path)))
                print("The list of visited Nodes : {}".format(visited))
                return path

            # else and it to the visited and add its children to the fringe

            else:
                for j in graph.nodes[n].children:
                    if not (j.name in visited):
                        fringe_dict[j.name] = [getPathCost(graph, getPath(j, j.name))]
                        fringe_list.clear()
        print('\nfailed to get the goal ')
        return None

    # Greedy Search Algorithm :
    def greedy(self, graph, startNode, goalNodes):

        # Checking if the start node and the goal node in the graph or not

        if startNode not in graph.getNodes():
            print('\nError: start Node \'{}\' not exists!!'.format(startNode))
            return
        for g in goalNodes:
            if (g not in graph.getNodes()):
                print('\nError: goal Node \'{}\' not exists!!'.format(g))
                return

        # Creating a object of class heuristics and calling function get huristics to calculate the h(x) of all nodes
        # in graph

        h = Huristcis()
        h.getHuristic(graph, startNode, goalNodes)
        print("\nThe heuristic function of the graph is : {}".format(h.nodes))
        fringe_dict = {startNode: h.nodes[startNode]}
        visited = []

        while fringe_dict is not None:
            # Sorts the fringe according to the heuristics of node
            fringe_dict = {k: v for k, v in sorted(fringe_dict.items(), key=lambda item: item[1])}

            fringe_list = []
            for j in fringe_dict.keys():
                fringe_list.append(j)

            # accessing the names in fringe by using a list (fringe_list)

            n = fringe_list[0]
            del fringe_dict[n]
            visited.append(n)


            if n in goalNodes:
                path = self.getPath(graph.nodes[n], startNode)
                print("Reached goal by Greedy algorithm !! \nThe path is : {}".format(path))
                print("Cost : {}".format(self.getPathCost(graph, path)))
                print("The list of visited Nodes : {}".format(visited))
                return
            else:
                for j in graph.nodes[n].children:
                    if not (j.name in visited):
                        fringe_dict[j.name] = [h.nodes[j.name]]
                        fringe_list.clear()
        print('\nfailed to get the goal ')
        return

        # Greedy Search Algorithm :
    def aStar (self, graph, startNode, goalNodes):

        # Checking if the start node and the goal node in the graph or not

        if startNode not in graph.getNodes():
            print('\nError: start Node \'{}\' not exists!!'.format(startNode))
            return
        for g in goalNodes:
            if (g not in graph.getNodes()):
                print('\nError: goal Node \'{}\' not exists!!'.format(g))
                return

        # creating an object from class Heuristics and calling f_of_X to calculate the summation of the H(x) and the
        # G(x)

        h = Huristcis()
        h.F_of_X(graph, startNode, goalNodes)
        print("\nThe F(x) function of the graph is : {}".format(h.optimalCostNodes))
        fringe_dict = {startNode: h.optimalCostNodes[startNode]}
        visited = []

        while fringe_dict is not None:
            # Sorts the fringe according to the heuristics of node
            fringe_dict = {k: v for k, v in sorted(fringe_dict.items(), key=lambda item: item[1])}

            fringe_list = []
            for j in fringe_dict.keys():
                fringe_list.append(j)
            n = fringe_list[0]
            del fringe_dict[n]
            visited.append(n)

            if n in goalNodes:
                path = self.getPath(graph.nodes[n], startNode)
                print("Reached goal by A* algorithm !! \nThe path is : {}".format(path))
                print("Cost : {}".format(self.getPathCost(graph, path)))
                print("The list of visited Nodes : {}".format(visited))
                return
            else:
                for j in graph.nodes[n].children:
                    if not (j.name in visited):
                        fringe_dict[j.name] = [h.nodes[j.name]]
                        fringe_list.clear()
        print('\nfailed to get the goal ')
        return

    # ===========================================================
    #                   Extra functions :
    # ===========================================================

    # Getting the path to the goal from the start
    def getPath(self, node, start):
        solList = []
        while node.name != start:
            solList.append(node.name)
            node = node.parent
        solList.append(node.name)
        solList.reverse()
        return solList

    # Getting the cost of the path from the Start node to the goal node/Nodes
    def getPathCost(self, graph, list):
        cost = 0
        for x in range(0, len(list) - 1):
            cost += graph.getWeightEdge(list[x], list[x + 1])
        return cost
