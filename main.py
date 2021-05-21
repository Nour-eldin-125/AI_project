from heuristic import *
from search_Algo import Search

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


graph.connect('A' ,'B' ,8)
graph.connect('A' ,'C' ,1)
graph.connect('A' ,'D' ,2)
graph.connect('B' ,'E' ,3)
# graph.connect('E' ,'B' ,6)
# graph.connect('E' ,'F' ,11)
graph.connect('C' ,'F' ,4)
graph.connect('F' ,'C' ,5)
graph.connect('F' ,'G' ,4)
graph.connect('F' ,'H' ,4)
graph.connect('C' ,'I' ,4)
graph.connect('I' ,'C' ,4)





s=Search()
s.greedy(graph,'A', ('F',"H"))
s.dfs(graph,'A', ('E',"I"))
s.ucs(graph, 'B',('E',"I"))
s.bfs(graph,'A', ('F',"H"))
s.aStar(graph, 'A', ('F', "H"))