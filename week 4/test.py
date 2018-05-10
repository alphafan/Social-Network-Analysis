import networkx as nx

G = nx.karate_club_graph()

print(sorted(nx.adamic_adar_index(G), key=lambda x: x[2], reverse=True))