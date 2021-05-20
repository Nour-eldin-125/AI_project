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
graph.addNode('T')
graph.addNode('N')


graph.connect('A' ,'B' ,3)
graph.connect('A' ,'C' ,6)
graph.connect('B' ,'D' ,4)
graph.connect('B' ,'E' ,5)
graph.connect('B' ,'I' ,8)
graph.connect('C' ,'F' ,1)
graph.connect('C' ,'G' ,9)
graph.connect('G' ,'H' ,10)
graph.connect('C' ,'T' ,2)
graph.connect('I' ,'N' ,3)




s=Search()

h=Huristcis()

s=Search()
s.greedy(graph,'A', ('F',"H"))
s.dfs(graph,'A', ('E',"I"))
s.ucs(graph, 'B',('E',"I"))
s.bfs(graph,'A', ('F',"H"))
s.aStar(graph, 'A', ('F', "H"))