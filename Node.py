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


def ucs_search(graph, startNode, goalNode):

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
        if n in goalNode:
            path = getPath(graph.nodes[n], startNode)
            return path
        else:
            visited.append(n)
            for j in graph.nodes[n].children:
                if not (j.name in visited):
                    fringe_dict[j.name] = [getPathCost(graph,getPath(j,j.name))]
                    fringe_list.clear()
    return None


def getPath(node, start):
    solList = []
    while node.name != start:
        solList.append(node.name)
        node = node.parent
    solList.append(node.name)
    solList.reverse()
    return solList


# Getting the cost of the path from the Start node to the goal node/Nodes
def getPathCost(graph, list):
    cost = 0
    for x in range(0, len(list) - 1):
        cost += graph.getWeightEdge(list[x], list[x + 1])
    return cost