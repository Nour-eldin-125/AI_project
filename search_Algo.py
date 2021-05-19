from Node import *
from heuristic import Huristcis


class Search():

    def __init__(self):
        pass

    # Dfs Search Algorithm :
    def dfs(self, graph, startNode, goalNode):
        visited = []
        fringe = [graph.nodes[startNode]]
        while len(fringe) != 0:
            x = len(fringe) - 1
            n = fringe[x]
            fringe.pop(x)
            if n.name in goalNode:
                solList = self.getPath(n, startNode)
                print('\nReached goal by DFS algorithm !! \nThe path is : {}'.format(solList))
                # getting a list of names of the visited nodes
                list = []
                for v in visited:
                    list.append(v.name)
                print('Cost : {}\nThe list of visited Nodes : {}\n'.format(self.getPathCost(graph, solList), list))
                return
            else:
                visited.append(n)
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
        visited = []
        fringe = [graph.nodes[startNode]]
        while len(fringe) != 0:
            n = fringe[0]
            fringe.pop(0)
            if n.name in goalNode:
                solList = self.getPath(n, startNode)
                print('\nReached goal by BFS algorithm !! \nThe path is : {}'.format(solList))
                # Getting a list of names of the visited nodes
                list = []
                for v in visited:
                    list.append(v.name)
                print('Cost : {}\nThe list of visited Nodes : {}\n'.format(self.getPathCost(graph, solList), list))
                return
            else:
                visited.append(n)
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
    def ucs(self, graph, name_node_start, name_node_goal):
        if name_node_start not in graph.getNodes():
            print('\nError: name_node_start \'{}\' not exists!!'.format(name_node_start))
            return
        for g in name_node_goal:
            if (g not in graph.getNodes()):
                print('\nError: name_node_goal \'{}\' not exists!!'.format(g))
                return
        else:
            # UCS uses priority queue, priority is the cumulative cost (smaller cost)
            queue = PriorityQueue()

            # expands initial node
            # get the keys of all successors of initial node
            names_successors = graph.getSuccessors(name_node_start)

            # adds the keys of successors in priority queue
            for name_sucessor in names_successors:
                weight = graph.getWeightEdge(name_node_start, name_sucessor)
                # each item of queue is a tuple (key, cumulative_cost)
                queue.insert((name_sucessor, weight), weight)

            reached_goal, cumulative_cost_goal = False, -1
            visited = [name_node_start]
            while not queue.is_empty():

                # remove item of queue, remember: item of queue is a tuple (key, cumulative_cost)
                name_current_node, cost_node = queue.remove()
                while name_current_node in visited:
                    name_current_node, cost_node = queue.remove()
                visited.append(name_current_node)

                if (name_current_node in name_node_goal):
                    reached_goal, cumulative_cost_goal = True, cost_node
                    break

                # get all successors of name_current_node
                names_successors = graph.getSuccessors(name_current_node)

                if names_successors:  # checks if contains successors
                    # insert all successors of name_current_node in the queue
                    for name_sucessor in names_successors:
                        cumulative_cost = graph.getWeightEdge(name_current_node, name_sucessor) + cost_node
                        queue.insert((name_sucessor, cumulative_cost), cumulative_cost)

            if (reached_goal):
                list = self.getPath(graph.nodes[name_current_node], name_node_start)
                print('\nReached goal by UCS algorithm !! \nThe path is : {} \nCost : {}'.format(list,
                                                                                                 cumulative_cost_goal))
                print('The list of visited Nodes : {} \n'.format(visited))

            else:
                print('\nUnfulfilled goal.\n')

    # Greedy Search Algorithm :
    def greedy(self, graph, startNode, goalNodes):
        h = Huristcis()
        h.getHuristic(graph, startNode, goalNodes)
        print("\nThe heuristic function of the graph is : {}".format(h.nodes))
        fringe_dict = {startNode: h.nodes[startNode]}
        visited = []

        while fringe_dict is not None:
            # Sorts the fringe according to the heuristics of node
            fringe_dict = {k: v for k, v in sorted(fringe_dict.items(), key=lambda item: item[1])}
            list = fringe_dict.keys()
            fringe_list = []
            for j in list:
                fringe_list.append(j)
            n = fringe_list[0]
            del fringe_dict[n]
            if n in goalNodes:
                path = self.getPath(graph.nodes[n], startNode)
                print("Reached goal by Greedy algorithm !! \nThe path is : {}".format(path))
                print("Cost : {}".format(self.getPathCost(graph, path)))
                print("The list of visited Nodes : {}".format(visited))
                return
            else:
                visited.append(n)
                for j in graph.nodes[n].children:
                    if not (j.name == visited):
                        fringe_dict[j.name] = [h.nodes[j.name]]
                        fringe_list.clear()
        print('\nfailed to get the goal ')
        return

    # ===========================================================
    #                   Extra functions :
    # ===========================================================

    # Flipping the list to get the correct path from the start to the goal node/Nodes
    def swap(self, list, left, right):
        while not (left >= right):
            temp = list[left]
            list[left] = list[right]
            list[right] = temp
            left += 1
            right -= 1
        return list

    # Getting the path to the goal from the start
    def getPath(self, node, start):
        solList = []
        while node.name != start:
            solList.append(node.name)
            node = node.parent
        solList.append(node.name)
        solList = self.swap(solList, 0, len(solList) - 1)
        return solList

    # Getting the cost of the path from the Start node to the goal node/Nodes
    def getPathCost(self, graph, list):
        cost = 0
        for x in range(0, len(list) - 1):
            cost += graph.getWeightEdge(list[x], list[x + 1])
        return cost
