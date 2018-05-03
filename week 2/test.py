import networkx as nx

G = nx.Graph()
G.add_edges_from([('A', 'K'), ('A', 'B'), ('A', 'C'), ('B', 'C'),
                  ('B', 'K'), ('C', 'E'), ('C', 'F'), ('D', 'E'),
                  ('E', 'F'), ('E', 'H'), ('F', 'I'), ('I', 'J')])

### ==> Average distance
print(nx.average_shortest_path_length(G))
### ==> Diameter
print(nx.diameter(G))
### ==> Eccentricity
print(nx.eccentricity(G))
### ==> Radius
print(nx.radius(G))
