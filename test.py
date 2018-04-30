import networkx as nx

G = nx.Graph()
G.add_edge('A', 'B', weight=6, relation='friend')
G.add_edge('B', 'C', weight=6, relation='co-worker')

G.add_node('A', role='manager')
G.add_node('B', role='trader')
G.add_node('C', role='analyst')

print(G.nodes(data=True))
print(G.nodes(data='role'))