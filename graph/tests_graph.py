from graph.graphs import graph, directed_graph


# Create graph
g = graph()

# Add some edges:
# 3 -- 4 -- 5 -- 2
# |    |  \ |
# 1 -- 8    6

g.add_edge(3, 4)
g.add_edge(3, 1)
g.add_edge(1, 8)
g.add_edge(4, 8)
g.add_edge(4, 5)
g.add_edge(4, 6)
g.add_edge(5, 2)
g.add_edge(5, 6)


# BFS
print(g.BFS())



# Create directed graph
dg = directed_graph()

# Add some edges:
# 3 .-- 4 --.5 --. 2
# |    .  .  |
# .    |   \ .
# 1 --. 8    6

dg.add_edge(4, 3)
dg.add_edge(3, 1)
dg.add_edge(1, 8)
dg.add_edge(8, 4)
dg.add_edge(4, 5)
dg.add_edge(6, 4)
dg.add_edge(5, 2)
dg.add_edge(5, 6)


# BFS
# Return format: {distance_from_start: [nodes with the same distance of distance_from_start from start}
print(dg.BFS())

# DFS
# Return format: A DFS forest: {key of the root vertex: [key of the descendants]}
print(dg.DFS_recursive())

# Strongly connected components
# Return format: A DFS forest: {key of the root vertex: [key of the descendants]}
# Each tree is a strongly connect subgraph
print(dg.strong_connect())