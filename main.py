from Node import Node

x=Node(name='A')

x.add(name='g', weight=50)
x.add(name='b', weight=60)

z=x.get_By_Name('g')
print(z.parent.name)
print(x.edges)
