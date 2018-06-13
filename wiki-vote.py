
# Patricia Figueroa
# CSCI 4800 - Programming Assignment 1

import networkx as nx
from sets import *

g = nx.read_adjlist('wiki-Vote.txt', create_using=nx.DiGraph())
g_undirected = g.to_undirected()

#degrees = g.degree().values()
#in_degrees = g.in_degree().values()
#out_degrees = g.out_degree().values()
#list(g.in_degree().values())


print 'Number nodes in the network:', len(g)

print 'Number of directed edges in the network:', len(g.edges())

print 'Number of undirected edges in the network:', len(g_undirected.edges())

count = 0
for node in g.nodes():
    if g.out_degree(node) > 100:
        count += 1
print 'Number of nodes with more than 100 outgoing edges:', count


zero_out_nodes = Set()
for node in g.nodes():
    if g.out_degree(node) == 0:
        zero_out_nodes.add(node)

print 'Number of nodes of zero out-degree:', len(zero_out_nodes)


zero_in_nodes = Set()
for node in g.nodes():
    if g.in_degree(node) == 0:
        zero_in_nodes.add(node)


print 'Number of nodes of zero in-degree:', len(zero_in_nodes)


