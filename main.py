from Node import *
from heuristic import *

graph = Graph()
graph.addNode('A')
graph.addNode('B')
graph.addNode('C')
graph.addNode('D')
graph.addNode('E')
graph.addNode('F')
graph.addNode('G')
graph.addNode('H')
graph.addNode('I')


graph.connect('A' ,'B' ,2)
graph.connect('A' ,'C' ,2)
graph.connect('B' ,'D' ,2)
graph.connect('B' ,'E' ,2)
graph.connect('B' ,'I' ,2)
graph.connect('C' ,'F' ,2)
graph.connect('C' ,'G' ,2)
graph.connect('G' ,'H' ,2)


graph.dfs('A', ('E',"I"))
ucs(graph, 'B',('E',"I"))

h=Huristcis()
h.getHuristic(graph=graph,start='A',goal=('E',"H"))
print(h.nodes)