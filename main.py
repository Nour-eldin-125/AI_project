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
graph.addNode('J')


graph.connect('A' ,'B' ,3)
graph.connect('A' ,'C' ,2)
graph.connect('B' ,'D' ,2)
graph.connect('C' ,'B' ,3)
graph.connect('E' ,'B' ,6)
graph.connect('C' ,'F' ,11)
graph.connect('C' ,'E' ,11)

graph.connect('F' ,'D' ,5)

graph.connect('E' ,'G' ,2)

graph.connect('E' ,'H' ,4)
graph.connect('H' ,'I' ,6)
graph.connect('E' ,'H' ,2)
graph.connect('H' ,'J' ,4)
graph.connect('H' ,'C' ,2)





s=Search()
list ={
    'A': 20,
    'B': 100,
    'C': 18,
    'D': 80,
    'E': 8,
    'I': 0,
    'J': 25,
    'F': 70,
    'G': 40,
    'H': 3
}

# s.dfs(graph,'A', ("E"))
# s.ucs(graph, 'A',('J','K'))
# s.bfs(graph,'A', ('J','E'))
s.greedy(graph,'A', ('I'),list)
# s.aStar(graph, 'A', ('J', "K"),list)