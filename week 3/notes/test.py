import networkx as nx
import operator

graph = nx.karate_club_graph()
graph = nx.convert_node_labels_to_integers(graph, first_label=1)
btwnCent = nx.edge_betweenness_centrality(graph)

print(sorted(btwnCent.items(), key=operator.itemgetter(1), reverse=True)[:5])