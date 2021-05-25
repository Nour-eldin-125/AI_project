class Node():

    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = []
        self.parentName=[]
        self.weight_child = {}


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
    def addChild(self, node, weight):
        # Adding none existing child
        if node.name not in self.weight_child:
            self.children.append(node)
            self.weight_child[node.name] = weight

            node.parent.append(self)
            node.parentName.append(self.name)

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


def ucs( graph, startNode, goalNode):
    fringe_dict = {startNode: 0}
    visited = {}

    while len(fringe_dict) != 0:
        fringe_dict = {k: v for k, v in sorted(fringe_dict.items(), key=lambda item: item[1])}

        list = []
        for l in fringe_dict.keys():
            list.append(l)
        item = list[0]
        cost = fringe_dict[item]
        fringe_dict.pop(item)
        visited[item] = cost
        v = []
        for visit in visited.keys():
            v.append(visit)
        if (item in goalNode):

            return visited

        else:
            for i in graph.nodes[item].children:
                if (i.name not in v):
                    if (i.name in fringe_dict):
                        if fringe_dict[i.name] > graph.getWeightEdge(item, i.name) + cost:
                            fringe_dict[i.name] = graph.getWeightEdge(item, i.name) + cost
                    else:
                        fringe_dict[i.name] = graph.getWeightEdge(item, i.name) + cost
            list.clear()
        return None


def getPathUCS(self, graph: Graph, startNode, start, visited: {}):
    solList = []
    v = len(visited) - 2
    while startNode.name != start:
        solList.append(startNode.name)
        min = 9999
        for p in startNode.parent:
            if (min > visited[p.name] + graph.getWeightEdge(p.name, startNode.name)):
                min = visited[p.name]
                temp = p
        startNode = temp
    solList.append(startNode.name)
    solList.reverse()
    return solList
