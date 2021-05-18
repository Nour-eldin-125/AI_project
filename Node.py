from priority_queue import *


class Node():

    def __init__(self, name, p=None, goal=False):
        self.name = name
        self.children = []
        self.parent = p
        self.weight_child = {}
        self.goal = goal
        self.huristics = None

    # Getting the child by its number
    def get_By_Num(self, child):
        return self.children[child]

    # Getting the parent of the node
    def get_Parent(self):
        return self.parent

    # Get all the children
    def getChildren(self):
        return self.children

    # Getting the child by it's name
    def getByName(self, data):
        for child in self.children:
            if child.name == data:
                return child

    # Adding a new child to the Node
    def addChild(self, node, weight, goal=False):
        # Adding none existing child
        if node.name not in self.weight_child:
            self.children.append(node)
            self.weight_child[node.name] = weight
            node.parent = self

    # Returning dictionary of all children with there weights
    def getWeightChildren(self):
        return self.weight_child


class Graph():

    def __init__(self):
        self.nodes = {}

    # Adding a non existing Node to graph
    def addNode(self, name):
        if name in self.nodes:
            print('Error: Name {} already exists in nodes !!'.format(name))
        else:
            node = Node(name)  # creates a instance of Node
            self.nodes[name] = node  # stores the node

    # connects the nodes
    def connect(self, sourceNode, destinationNode, weight):
        # checks if the name already exists in the graph
        if sourceNode in self.nodes and destinationNode in self.nodes:
            if sourceNode != destinationNode:  # checks if the names are different
                if weight > 0:  # checks if the weight is positive
                    # connects the nodes
                    self.nodes[sourceNode].addChild(self.nodes[destinationNode], weight)
                else:
                    print('Error: weight negative !!')
            else:
                print('Error: same Names !!')
        else:
            print('Error: Names do not exist !!')

    # returns weight of edge
    def getWeightEdge(self, sourceName, childName):
        if sourceName in self.nodes and childName in self.nodes:  # checks if the Names exists
            if sourceName != childName:  # checks if the Names are different
                weight_child = self.nodes[sourceName].getWeightChildren()
                if childName in weight_child:  # checks if childName is a successor
                    return weight_child[childName]  # returns the weight
                else:
                    print('Error: child does not exists!!')
            else:
                print('Error: same Names !!')
        else:
            print('Error: Names do not exist !!')

    # returns the keys of all successors of a node
    def getSuccessors(self, node_Name):
        if node_Name in self.nodes:
            nodes = self.nodes[node_Name].getChildren()
            node_children = [node.name for node in nodes]
            return node_children
        else:
            print('Error: Name does not exist !!')

    # returns all nodes
    def getNodes(self):
        return self.nodes

    # searching using DFS by name of start and list of the goals .
    def dfs(self, startNode, goalNode):
        for g in goalNode:
            self.nodes[g].goal = True
        visited = []
        fringe = [self.nodes[startNode]]

        while len(fringe) != 0:
            x = len(fringe) - 1
            n = fringe[x]
            fringe.pop(x)
            if n.goal:
                solList = getPath(n,startNode)
                print('\nReached goal! the path is : {}'.format(solList))
                # getting a list of names of the visited nodes
                list = []
                for v in visited:
                    list.append(v.name)
                print('Cost : {}\nThe list of visited Nodes : {}\n'.format(getPathCost(self, solList), list))
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

        print('failed to get the goal')
        return

# searching using ucs by name of start and list of the goals .
def ucs(graph, name_node_start, name_node_goal):
    if name_node_start not in graph.getNodes():
        print('Error: name_node_start \'{}\' not exists!!'.format(name_node_start))
        return
    for g in name_node_goal:
        if (g not in graph.getNodes()):
            print('Error: name_node_goal \'{}\' not exists!!'.format(g))
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
            list = getPath(graph.nodes[name_current_node],name_node_start)
            print('Reached goal! the path is : {} \nCost : {}'.format(list, cumulative_cost_goal))
            print('the list of visited Nodes : {} \n'.format(visited))

        else:
            print('\nUnfulfilled goal.\n')


def swap(list, left, right):
    while not (left >= right):
        temp = list[left]
        list[left] = list[right]
        list[right] = temp
        left += 1
        right -= 1
    return list


# Getting the path to the goal from the start
def getPath(node,start):
    solList = []
    while node.parent.name != start:
        solList.append(node.name)
        node = node.parent
    solList.append(node.name)
    solList = swap(solList, 0, len(solList) - 1)
    return solList


def getPathCost(graph, list):
    cost = 0
    for x in range(0, len(list) - 1):
        cost += graph.getWeightEdge(list[x], list[x + 1])
    return cost


def ucs_search(graph, name_node_start, name_node_goal):
    queue = PriorityQueue()
    names_successors = graph.getSuccessors(name_node_start)

    for name_sucessor in names_successors:
        weight = graph.getWeightEdge(name_node_start, name_sucessor)
        queue.insert((name_sucessor, weight), weight)

    reached_goal, cumulative_cost_goal = False, -1
    visited = [name_node_start]
    while not queue.is_empty():

        name_current_node, cost_node = queue.remove()
        while name_current_node in visited:
            name_current_node, cost_node = queue.remove()
        visited.append(name_current_node)

        if (name_current_node in name_node_goal):
            reached_goal, cumulative_cost_goal = True, cost_node
            break
        names_successors = graph.getSuccessors(name_current_node)

        if names_successors:  # checks if contains successors
            for name_sucessor in names_successors:
                cumulative_cost = graph.getWeightEdge(name_current_node, name_sucessor) + cost_node
                queue.insert((name_sucessor, cumulative_cost), cumulative_cost)

    if (reached_goal):
        return getPath(graph.nodes[name_current_node],name_node_start)
    else:
        return None
