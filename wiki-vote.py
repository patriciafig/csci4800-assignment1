
# Patricia Figueroa
# CSCI 4800 - Programming Assignment 1


import networkx as nx


g = nx.read_adjlist('wiki-Vote.txt', create_using=nx.DiGraph())
g_undir = g.to_undirected()

print 'Number nodes in the network:', len(g)

print 'Number of directed edges in the network:', len(g.edges())

print 'Number of undirected edges in the network:', len(g_undir.edges())