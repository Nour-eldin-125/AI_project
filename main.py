from Node import Node

x=Node(name='A')

x.add(name='g', weight=50)
x.add(name='b', weight=60)
x.add(name='h',weight=80)

z=x.get_By_Name('g')
c=x.get_By_Name('h')
z.add(name='j',weight=20)
c.add(name='l',weight=30)
s=c.get_By_Num(0)
s.add(name='m',goal=True,weight=40)

print(x.search_Dfs(x))

print(z.parent.name)
print(x.edges)
