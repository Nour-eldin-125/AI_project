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

    # searching using DFS
    def dfs(self, startNode, goalNode):
        self.nodes[goalNode].goal = True
        visited = []
        fringe = [self.nodes[startNode]]

        while len(fringe) != 0:
            x = len(fringe) - 1
            n = fringe[x]
            fringe.pop(x)
            if n.goal:
                solList = getPath(n)
                print(solList)
                # getting a list of names of the visited nodes
                list = []
                for v in visited:
                    list.append(v.name)
                print('The list of visited Nodes : {}\nCost : {}'.format(list,getPathCost(self,solList)))
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


def ucs(graph, key_node_start, key_node_goal):
    if key_node_start not in graph.getNodes() or key_node_goal not in graph.getNodes():
        print('Error: key_node_start \'{}\' or key_node_goal \'{}\' not exists!!'.format(key_node_start, key_node_goal))
    else:
        # UCS uses priority queue, priority is the cumulative cost (smaller cost)
        queue = PriorityQueue()

        # expands initial node
        # get the keys of all successors of initial node
        keys_successors = graph.getSuccessors(key_node_start)

        # adds the keys of successors in priority queue
        for key_sucessor in keys_successors:
            weight = graph.getWeightEdge(key_node_start, key_sucessor)
            # each item of queue is a tuple (key, cumulative_cost)
            queue.insert((key_sucessor, weight), weight)

        reached_goal, cumulative_cost_goal = False, -1
        visited = [key_node_start]
        while not queue.is_empty():

            # remove item of queue, remember: item of queue is a tuple (key, cumulative_cost)
            key_current_node, cost_node = queue.remove()

            visited.append(key_current_node)

            if (key_current_node == key_node_goal):
                reached_goal, cumulative_cost_goal = True, cost_node
                break

            # get all successors of key_current_node
            keys_successors = graph.getSuccessors(key_current_node)

            if keys_successors:  # checks if contains successors
                # insert all successors of key_current_node in the queue
                for key_sucessor in keys_successors:
                    cumulative_cost = graph.getWeightEdge(key_current_node, key_sucessor) + cost_node
                    queue.insert((key_sucessor, cumulative_cost), cumulative_cost)

        if (reached_goal):
            list=getPath(graph.nodes[key_current_node])
            print('\nReached goal! the path is : {} \nCost : {}'.format(list,cumulative_cost_goal))
            print('the list of visited Nodes : {} \n'.format(visited))

        else:
            print('\nUnfulfilled goal.\n')


def swap(list, left, right):
    while (left != right):
        temp = list[left]
        list[left] = list[right]
        list[right] = temp
        left += 1
        right -= 1
    return list


# Getting the path to the goal from the start
def getPath(node):
    solList = []
    while node.parent is not None:
        solList.append(node.name)
        node = node.parent
    solList.append(node.name)
    solList = swap(solList, 0, len(solList) - 1)
    return solList

def getPathCost (graph,list):
    cost=0
    for x in range(0,len(list)-1):
        cost += graph.getWeightEdge(list[x],list[x+1])
    return cost
