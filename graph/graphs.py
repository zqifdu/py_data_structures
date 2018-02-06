
class node(object):
    def __init__(self, key):
        self.key = key
        self.neighbors = []


class graph(object):
    def __init__(self):
        self.num_nodes = 0
        self.nodes = {}

    def add_edge(self, n1, n2):
        if n1 not in self.nodes:
            self.nodes[n1] = node(n1)
        if n2 not in self.nodes:
            self.nodes[n2] = node(n2)

        self.nodes[n1].neighbors.append(self.nodes[n2])
        self.nodes[n2].neighbors.append(self.nodes[n1])

    
