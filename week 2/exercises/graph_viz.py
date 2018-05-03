# Visualizing Networks

import networkx as nx
import matplotlib.pyplot as plt

# Read the graph
G = nx.read_gpickle('major_us_cities')

# Have a look at the data
print(G.nodes(data=True)[0])
print(G.edges(data=True)[0])

# Have a look at different layouts in networkx
print('Layouts:', [layout for layout in nx.__dir__() if layout.endswith('_layout')])

#######################################################################################

# ==> 1. Default Spring Layout
plt.figure(figsize=(10, 7))
nx.draw_networkx(G)

# ==> 2. Random Layout
plt.figure(figsize=(10, 7))
nx.draw_networkx(G, pos=nx.random_layout(G))

# ==> 3. Circular layout
plt.figure(figsize=(10, 7))
nx.draw_networkx(G, pos=nx.circular_layout(G))

# ==> 4. Spectral layout
plt.figure(figsize=(10, 7))
nx.draw_networkx(G, pos=nx.spectral_layout(G))

# ==> 5. Shell layout
plt.figure(figsize=(10, 7))
nx.draw_networkx(G, pos=nx.shell_layout(G))

# ==> 6. Fruchterman reingold layout
plt.figure(figsize=(10, 7))
nx.draw_networkx(G, pos=nx.fruchterman_reingold_layout(G))

#######################################################################################

# Draw the graph using custom node positions
plt.figure(figsize=(10, 7))

pos = nx.get_node_attributes(G, 'location')
nx.draw_networkx(G, pos)

# Draw the graph adding alpha, removing labels, and softening edge color
plt.figure(figsize=(10, 7))

pos = nx.get_node_attributes(G, 'location')
nx.draw_networkx(G, pos, with_labels=False, alpha=.7, edge_color='.4')

# Draw graph with varying node color, node size, and edge width
plt.figure(figsize=(10, 7))

node_color = [G.degree(v) for v in G.nodes()]
node_size  = [0.0005*nx.get_node_attributes(G, 'population')[v] for v in G.nodes()]
edge_width = [0.015*G[u][v]['weight'] for u, v in G.edges()]

nx.draw_networkx(G, pos, with_labels=False, alpha=.7, cmap='Blues', edge_color='.4',
                 node_color=node_color, node_size=node_size, edge_width=edge_width)

# Draw specific edges and add labels to specific nodes
plt.figure(figsize=(10, 7))

node_color = [G.degree(v) for v in G]
node_size  = [0.0005*nx.get_node_attributes(G, 'population')[v] for v in G]
edge_width = [0.0015*G[u][v]['weight'] for u,v in G.edges()]

nx.draw_networkx(G, pos, node_size=node_size,
                 node_color=node_color, alpha=0.7, with_labels=False,
                 width=edge_width, edge_color='.4', cmap='Blues')

greater_than_770 = [x for x in G.edges(data=True) if x[2]['weight'] > 770]
nx.draw_networkx_edges(G, pos, edgelist=greater_than_770, edge_color='r', alpha=.4, width=.6)
nx.draw_networkx_labels(G, pos, labels={'Los Angeles, CA': 'LA', 'New York, NY': 'NYC'}, font_size=18, font_color='w')

plt.axis('off')
plt.tight_layout()
plt.show()