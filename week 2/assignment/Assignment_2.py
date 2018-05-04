"""
Assignment 2 - Network Connectivity
In this assignment you will go through the process of importing and analyzing an internal
email communication network between employees of a mid-sized manufacturing company.
Each node represents an employee and each directed edge between two nodes represents an individual email.
The left node represents the sender and the right node represents the recipient.
"""

import networkx as nx


# ==> Question 1
# Using networkx, load up the directed multigraph from email_network.txt.
# Make sure the node names are strings.
# This function should return a directed multigraph networkx graph.

def answer_one() -> nx.MultiDiGraph:
    # Your Code Here
    graph = nx.read_edgelist('email_network.txt', delimiter='\t', create_using=nx.MultiDiGraph(),
                             nodetype=str, data=[('time', int)])
    return graph  # Your Answer Here


# ==> Question 2
# How many employees and emails are represented in the graph from Question 1?
# This function should return a tuple (#employees, #emails).

def answer_two():
    # Your Code Here
    graph = answer_one()
    return len(graph.nodes()), len(graph.edges())  # Your Answer Here


# ==> Question 3
# - Part 1. Assume that information in this company can only be exchanged through email.
# When an employee sends an email to another employee, a communication channel has been created,
# allowing the sender to provide information to the receiver, but not vice versa.
# Based on the emails sent in the data, is it possible for information to go from every employee
# to every other employee?
# - Part 2. Now assume that a communication channel established by an email allows information to
# be exchanged both ways.
# Based on the emails sent in the data, is it possible for information to go from every employee
# to every other employee?
# This function should return a tuple of bools (part1, part2).

def answer_three():
    # Your Code Here
    graph = answer_one()
    return nx.is_strongly_connected(graph), nx.is_weakly_connected(graph)  # Your Answer Here


# ==> Question 4
# How many nodes are in the largest (in terms of nodes) weakly connected component?
# This function should return an int.

def answer_four():
    # Your Code Here
    graph = answer_one()
    largest = max(nx.weakly_connected_components(graph), key=len)
    return len(largest)  # Your Answer Here


# ==> Question 5
# How many nodes are in the largest (in terms of nodes) strongly connected component?
# This function should return an int

def answer_five():
    # Your Code Here
    graph = answer_one()
    largest = max(nx.strongly_connected_components(graph), key=len)
    return len(largest)  # Your Answer Here


# ==> Question 6
# Using the NetworkX function strongly_connected_component_subgraphs,
# find the subgraph of nodes in a largest strongly connected component.
# Call this graph G_sc.
# This function should return a networkx MultiDiGraph named G_sc.

def answer_six() -> nx.MultiDiGraph:
    # Your Code Here
    graph = answer_one()
    return max(nx.strongly_connected_component_subgraphs(graph),
               key=lambda x: len(x.nodes()))  # Your Answer Here


# ==> Question 7
# What is the average distance between nodes in G_sc?
# This function should return a float.

def answer_seven():
    # Your Code Here
    graph = answer_six()
    return nx.average_shortest_path_length(graph)  # Your Answer Here


# ==> Question 8
# What is the largest possible distance between two employees in G_sc?
# This function should return an int

def answer_eight():
    # Your Code Here
    graph = answer_six()
    return nx.diameter(graph)  # Your Answer Here


# ==> Question 9
# What is the set of nodes in G_sc with eccentricity equal to the diameter?
# This function should return a set of the node(s).

def answer_nine():
    # Your Code Here
    graph = answer_six()
    return set(nx.periphery(graph))  # Your Answer Here


# ==> Question 10
# What is the set of node(s) in G_sc with eccentricity equal to the radius?
# This function should return a set of the node(s).

def answer_ten():
    # Your Code Here
    graph = answer_six()
    return set(nx.center(graph))  # Your Answer Here


# ==> Question 11
# Which node in G_sc is connected to the most other nodes by a shortest path
# of length equal to the diameter of G_sc?
# How many nodes are connected to this node?
# This function should return a tuple (name of node, number of satisfied connected nodes).

def answer_eleven():
    # Your Code Here
    graph = answer_six()
    diameter, periphery = nx.diameter(graph), nx.periphery(graph)
    result, max_count = None, -1
    for node in periphery:
        sp = nx.shortest_path_length(graph, node)
        count = list(sp.values()).count(diameter)
        if count > max_count:
            result = node
            max_count = count
    return result, max_count  # Your Answer Here


# ==> Question 12
# Suppose you want to prevent communication from flowing to the node that you
# found in the previous question from any node in the center of G_sc, what is
# the smallest number of nodes you would need to remove from the graph (you're
# not allowed to remove the node from the previous question or the center nodes)?
# This function should return an integer.

def answer_twelve():
    # Your Code Here
    graph = answer_six()
    node, center = answer_eleven()[0], nx.center(graph)[0]
    return len(nx.minimum_node_cut(graph, center, node))  # Your Answer Here


# ==> Question 13
# Construct an undirected graph G_un using G_sc (you can ignore the attributes).
# This function should return a networkx Graph.

def answer_thirteen() -> nx.Graph:
    # Your Code Here
    graph = answer_six()
    return nx.Graph(graph.to_undirected())  # Your Answer Here


# ==> Question 14
# What is the transitivity and average clustering coefficient of graph G_un?
# This function should return a tuple (transitivity, avg clustering).

def answer_fourteen():
    # Your Code Here
    graph = answer_thirteen()
    return nx.transitivity(graph), nx.average_clustering(graph)  # Your Answer Here


print(answer_fourteen())
