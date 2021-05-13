class Node():

    def __init__(self,name,edge=None):
        self.name = name
        self.node = []
        self.parent = edge
        self.edges = {}

    # Getting the parent of the node
    def get_Parent(self):
        return self.parent

    # Getting the child by it's name
    def get_By_Name(self, data):
        for child in range(0, len(self.node)):
            if (self.node[child].name == data):
                return self.node[child]

    # Adding a new child to the Node
    def add(self,name,weight):
        node1 = Node(name=name)
        self.node.append(node1)
        node1.parent = self
        self.edges['{}'.format(name)]=weight
        return node1
