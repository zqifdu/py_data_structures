from graph.graphs import graph


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

