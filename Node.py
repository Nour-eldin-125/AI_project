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

def getPath(node, start):
    solList = []
    while node.name != start:
        solList.append(node.name)
        node = node.parent
    solList.append(node.name)
    solList = swap(solList, 0, len(solList) - 1)
    return solList

def swap(list, left, right):
    while not (left >= right):
        temp = list[left]
        list[left] = list[right]
        list[right] = temp
        left += 1
        right -= 1
    return list