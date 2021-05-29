from tkinter import *
from tkinter import ttk
from Node import Graph
from search_Algo import Search
import matplotlib.pyplot as plt
import networkx as nx

function= ''
node= []
edges=[]
heu={}
startNode =''
goalNode=[]
graph=Graph()
s=Search()

def buildGraph ():
    stringNode=nodeEntry.get()
    stringEdge=edgeEntry.get()
    stringheu=heuEntry.get()
    global startNode,goalNode,node,edges,heu
    startNode = startEntry.get()
    gn=goalEntry.get()
    str=''
    for x in stringNode:
        if (x!=','):
            str+=x
        if (x==','):
            graph.addNode(str)
            node.append(str)
            str=''
    graph.addNode(str)
    node.append(str)
    str1=''
    str2=''
    int1=''
    first=True
    isint=False
    for x in stringEdge:
        if (x!=','and first)and (not isint):
            str1+=x
        if x!= '='and (not first)and (not isint):

            str2+=x
        if x ==',' or x == '-':
            if first : first=False
            else: first=True
        if x== '-':
            isint=False
            graph.connect(str1,str2,int(int1))
            edges.append((str1,str2,int(int1)))

            str1=''
            str2=''
            int1=''
        if isint:
            int1+=x
        if x== '=':
            isint=True
    graph.connect(str1, str2, int(int1))
    edges.append((str1,str2,int(int1)))

    str=''
    isString=True
    int1=''
    for x in stringheu:
        if x!='=' and x != ',' and isString:
            str+=x
        if x == ',':
            isString = True
            heu[str]= int(int1)
            str=''
            int1=''
        if (not isString) and (x != ',' or x != '='):
            int1+=x
        if x == '=':
            isString = False
    heu[str]=int(int1)

    str=''
    for x in gn:
        if (x!=','):
            str+=x
        if (x==','):
            goalNode.append(str)
            str=''
    goalNode.append(str)



def bfs():
    global function
    function = "bfs"
    dict = s.bfs(graph, startNode[0], goalNode)
    labelBfs = Label(frame2, text="The result of the function BFS")
    labelpath = Label(frame2, text="the path is : {}".format(dict['path']))
    labelcost = Label(frame2, text="cost is : {}".format(dict['cost']))
    labelvisited = Label(frame2, text="the visited nodes is is : {}\n".format(dict['visit']))
    labelBfs.pack()
    labelpath.pack()
    labelcost.pack()
    labelvisited.pack()

def dfs():
    global function
    function = "dfs"
    dict = s.dfs(graph, startNode[0], goalNode)
    labelDfs     = Label(frame2, text="The result of the function DFS")
    labelpath    = Label(frame2, text="the path is : {}".format(dict['path']))
    labelcost    = Label(frame2, text="cost is : {}".format(dict['cost']))
    labelvisited = Label(frame2, text="the visited nodes is is : {}\n".format(dict['visit']))
    labelDfs.pack()
    labelpath.pack()
    labelcost.pack()
    labelvisited.pack()

def ucs():
    global function
    function = "ucs"
    dict = s.ucs(graph, startNode[0], goalNode)
    labelUcs     = Label(frame2, text="The result of the function UCS")
    labelpath    = Label(frame2, text="the path is : {}".format(dict['path']))
    labelcost    = Label(frame2, text="cost is : {}".format(dict['cost']))
    labelvisited = Label(frame2, text="the visited nodes is is : {}\n".format(dict['visit']))
    labelUcs.pack()
    labelpath.pack()
    labelcost.pack()
    labelvisited.pack()

def greedy():
    global function
    function = "greedy"
    dict = s.greedy(graph, startNode[0], goalNode,heu)
    labelGreedy     = Label(frame2, text="The result of the function Greedy")
    labelpath    = Label(frame2, text="the path is : {}".format(dict['path']))
    labelcost    = Label(frame2, text="cost is : {}".format(dict['cost']))
    labelvisited = Label(frame2, text="the visited nodes is is : {}\n".format(dict['visit']))
    labelGreedy.pack()
    labelpath.pack()
    labelcost.pack()
    labelvisited.pack()

def aStar():

    global function
    function = "astar"
    dict = s.aStar(graph, startNode[0], goalNode, heu)
    labelaStar = Label(frame2, text="The result of the function A*")
    labelpath = Label(frame2, text="the path is : {}".format(dict['path']))
    labelcost = Label(frame2, text="cost is : {}".format(dict['cost']))
    labelvisited = Label(frame2, text="the visited nodes is is : {}\n".format(dict['visit']))
    labelaStar.pack()
    labelpath.pack()
    labelcost.pack()
    labelvisited.pack()

def Draw():

    if (function == 'astar'):
        dict = s.aStar(graph, startNode, goalNode, heu)
    elif(function=='dfs'):
        dict = s.dfs(graph, startNode, goalNode)
    elif(function == 'ucs'):
        dict = s.ucs(graph, startNode, goalNode)
    elif(function =='bfs'):
        dict = s.bfs(graph, startNode, goalNode)
    elif(function == 'greedy'):
        dict = s.greedy(graph, startNode, goalNode, heu)

    list=dict['path']
    path=[]
    for x in range(len(list)-1):
        path.append((list[x],list[x+1]))

    notpath=[]
    for e in edges:
        notpath.append((e[0],e[1]))

    for x in path:
        if (x in notpath):
            notpath.remove(x)
    notGoalNode=[]
    for n in node:
        if (n not in goalNode):
            notGoalNode.append(n)

    G = nx.DiGraph()
    G.add_weighted_edges_from(edges)
    pos = nx.planar_layout(G)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=path,
        width=5,
        alpha=0.5,
        edge_color="r",

    )
    nx.draw_networkx_edges(
        G,
        pos,
        edgelist=notpath,
        edge_color='black',
    )

    nx.draw_networkx_nodes(G, pos, nodelist=notGoalNode, node_size=500,
                           node_color='r')
    nx.draw_networkx_nodes(G, pos, nodelist=goalNode, node_size=500, node_color='b')
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, label_pos=0.3)
    plt.show()



root=Tk()
root.title("Graph Search ")

ttk.Label(root, text="Graph").pack()

panedwindow=ttk.Panedwindow(root, orient=HORIZONTAL)
panedwindow.pack(fill=BOTH, expand=True)

frame1=ttk.Frame(panedwindow,width=100,height=300, relief=SUNKEN, padding=10)
frame2=ttk.Frame(panedwindow,width=400,height=400, relief=SUNKEN, padding=10)

panedwindow.add(frame1, weight=1)
panedwindow.add(frame2, weight=4)

LabelEnterNodes=Label(frame1, text="Enter Nodes \n (i.e. A,B,C)")
LabelEnterNodes.pack()

nodeEntry=ttk.Entry(frame1, width=40)
nodeEntry.pack()

LabelEnterEdges=Label(frame1, text="Enter Edges From Node to Node \n (i.e. A,B=1-B,C=2)")
LabelEnterEdges.pack()

edgeEntry=ttk.Entry(frame1, width=40)
edgeEntry.pack()

LabelEnterHeuristics=Label(frame1, text="Enter Heuristics \n (i.e. A=1,B=2)")
LabelEnterHeuristics.pack()

heuEntry=ttk.Entry(frame1, width=40)
heuEntry.pack()

LabelSetStart=Label(frame1, text="Set Start")
LabelSetStart.pack()

startEntry=ttk.Entry(frame1, width=40)
startEntry.pack()

LabelSetGoal=Label(frame1, text="Set Goal")
LabelSetGoal.pack()

goalEntry=ttk.Entry(frame1, width =40)
goalEntry.pack()

Enterbutton=ttk.Button(frame1, text="Enter",command=buildGraph)
Enterbutton.pack(pady=10)

LabelChooseSearch=Label(frame1, text="Choose Search Method").pack(pady=10)

BFSbutton=ttk.Button(frame1, text="BFS",command=bfs)
BFSbutton.pack()

DFSbutton=ttk.Button(frame1, text="DFS",command=dfs)
DFSbutton.pack()

UCSbutton=ttk.Button(frame1, text="UCS",command=ucs)
UCSbutton.pack()

Greedybutton=ttk.Button(frame1, text="Greedy",command=greedy)
Greedybutton.pack()

Abutton=ttk.Button(frame1, text="A*",command=aStar)
Abutton.pack()

Drawbutton=ttk.Button(frame1, text="Draw Graph", width=40, padding=10, command=Draw)
Drawbutton.pack(pady=10)

#Calling Main()
root.mainloop()