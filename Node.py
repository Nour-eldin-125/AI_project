class Node():

    def __init__(self, name, p=None, goal=False):
        self.name = name
        self.node = []
        self.parent = p
        self.edges = {}
        self.goal=goal
        self.huristics = None

    # Getting the child by its number
    def get_By_Num(self,child):
        return self.node[child]

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

    # searching using DFS
    def search_Dfs (self,start_node):
        visited = []
        fringe = [start_node]
        while fringe is not None:
            x= len(fringe) - 1
            n=fringe[x]
            fringe.pop(x)
            if (n.goal):
                p=n
                solution=''
                while (p.parent != None):
                    solution += p.name + ' '
                    p=p.parent
                return solution
            else:
                visited.append(n)
                for c in n.child:
                    found=False
                    for v in visited:
                        if v.name == c.name:
                            found=True
                    if (found):
                        continue
                    else:
                        fringe.append(c)

        return 'failure'

