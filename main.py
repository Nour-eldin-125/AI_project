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
graph.addNode('K')


graph.connect('A' ,'B' ,8)
graph.connect('A' ,'C' ,1)
graph.connect('A' ,'D' ,2)
graph.connect('B' ,'E' ,3)
graph.connect('E' ,'B' ,6)
graph.connect('E' ,'F' ,11)
graph.connect('C' ,'E' ,11)

graph.connect('F' ,'C' ,5)

graph.connect('C' ,'F' ,2)



graph.connect('F' ,'G' ,4)
graph.connect('D' ,'G' ,6)
graph.connect('D' ,'H' ,2)
graph.connect('G' ,'K' ,4)
graph.connect('E' ,'I' ,2)
graph.connect('E' ,'J' ,1)





s=Search()
list ={
    'A': 4,
    'B': 3,
    'C': 4,
    'D': 9,
    'E': 1,
    'I': 1,
    'J': 0,
    'F': 7,
    'G': 3,
    'H': 1,
    'K': 0
}

# s.dfs(graph,'A', ("E"))
s.ucs(graph, 'A',('J','K'))
# s.bfs(graph,'A', ('J','E'))
# s.greedy(graph,'A', ('J','K'),list)
s.aStar(graph, 'A', ('J', "K"),list)