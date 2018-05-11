import networkx as nx

G = nx.Graph()

G.add_edges_from([('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'D'), ('G', 'C'),
                  ('D', 'E'), ('D', 'G'), ('D', 'H'), ('E', 'H'), ('F', 'H')])

G.node['A']['community'] = 0
G.node['B']['community'] = 0
G.node['C']['community'] = 0
G.node['D']['community'] = 0
G.node['E']['community'] = 1
G.node['F']['community'] = 1
G.node['G']['community'] = 0
G.node['H']['community'] = 1

print(list(nx.cn_soundarajan_hopcroft(G)))