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


graph.connect('A' ,'B' ,8)
graph.connect('A' ,'C' ,9)
graph.connect('B' ,'D' ,12)
graph.connect('B' ,'A' ,7)
graph.connect('C' ,'A' ,10)
graph.connect('B' ,'E' ,11)
graph.connect('C' ,'F' ,6)
graph.connect('C' ,'G' ,4)

graph.connect('D' ,'F' ,8)

graph.connect('E' ,'G' ,2)

graph.connect('E' ,'H' ,1)
graph.connect('F' ,'H' ,1)
# graph.connect('H' ,'I' ,6)
# graph.connect('E' ,'H' ,2)
# graph.connect('H' ,'J' ,4)
# graph.connect('H' ,'C' ,2)



'''
A=14,B=10,C=5,D=8,E=1,F=1,G=100,H=0

A,B=8-A,C=9-B,A=7-C,A=10-B,D=12-B,E=11-C,F=6-C,G=4-D,F=8-E,G=2-E,H=1-F,H=1
'''

s=Search()
list ={
    'A': 14,
    'B': 10,
    'C': 5,
    'D': 8,
    'E': 1,
    # 'I': 1,
    # 'J': 25,
    'F': 1,
    'G': 100,
    'H': 0
}

# s.dfs(graph,'A', ("E"))
# s.ucs(graph, 'A',('J','K'))
# s.bfs(graph,'A', ('J','E'))
s.greedy(graph,'A', ('H'),list)
# s.aStar(graph, 'A', ('J', "K"),list)