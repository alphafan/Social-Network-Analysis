"""
Assignment 3
In this assignment you will explore measures of centrality on two networks,
a friendship network in Part 1, and a blog network in Part 2.
"""

# ==> Part 1
# Answer questions 1-4 using the network G1,
# a network of friendships at a university department.
# Each node corresponds to a person, and an edge indicates friendship.
# The network has been loaded as networkx graph object G1.

import networkx as nx

G1 = nx.read_gml('friendships.gml')


# - Question 1
# Find the degree centrality, closeness centrality, and normalized
# betweeness centrality (excluding endpoints) of node 100.
# This function should return a tuple of floats
# (degree_centrality, closeness_centrality, betweenness_centrality).

def answer_one():
    # Your Code Here
    return nx.degree_centrality(G1)[100], nx.closeness_centrality(G1)[100], \
           nx.betweenness_centrality(G1)[100]  # Your Answer Here


# For Questions 2, 3, and 4, assume that you do not know anything about the structure of the network,
# except for the all the centrality values of the nodes. That is, use one of the covered centrality
# measures to rank the nodes and find the most appropriate candidate.

# Question 2
# Suppose you are employed by an online shopping website and are tasked with selecting one user
# in network G1 to send an online shopping voucher to. We expect that the user who receives the
# voucher will send it to their friends in the network. You want the voucher to reach as many
# nodes as possible. The voucher can be forwarded to multiple users at the same time, but the travel
# distance of the voucher is limited to one step, which means if the voucher travels more than one
# step in this network, it is no longer valid. Apply your knowledge in network centrality to select
# the best candidate for the voucher.
# This function should return an integer, the name of the node.

def answer_two():
    # Your Code Here

    return  # Your Answer Here
