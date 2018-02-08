'''
Author: Zhenyi Qi

'''


from functools import wraps
from collections import deque

class vertex(object):
    def __init__(self, key):

        # Key value
        self.key = key

        # Neighboring vertices
        self.neighbors = []

        # Discover status
        self.color = 'white'

        # Predecessor in a search
        self.pi = None

        # Distance from the root through a tree constructed through a BFS
        self.d = -1

        # Discover time in a DFS
        self.dt = -1

        # Finish time in a DFS
        self.ft = -1

class graph(object):
    '''
    Unweighted bidirection graph.
    '''
    def __init__(self):
        self.num_v = 0
        self.vertices = {}
        self.root = None


    def _update_num_v(func):
        @wraps(func)
        def _update_num_wrapper(self, *args, **kwargs):
            self.num_v = len(self.vertices)
            return func(self, *args, **kwargs)

        return _update_num_wrapper


    def _re_color(func):
        @wraps(func)
        def _recolor_wrapper(self, *args, **kwargs):
            results = func(self, *args, **kwargs)
            for v in self.vertices.values():
                v.color = 'white'

            return results
        return _recolor_wrapper


    @_update_num_v
    def add_edge(self, v1, v2):
        if self.vertices == {}:
            self.root = vertex(v1)
            self.vertices[v1] = self.root

        if v1 not in self.vertices:
            self.vertices[v1] = vertex(v1)
        if v2 not in self.vertices:
            self.vertices[v2] = vertex(v2)

        self.vertices[v1].neighbors.append(self.vertices[v2])
        self.vertices[v2].neighbors.append(self.vertices[v1])



    @_re_color
    def BFS(self, re_color = True):
        '''
        Breadth-first search of the graph
        Returns
        -------

        '''
        if re_color:
            for v in self.vertices.values():
                v.color = 'white'

        queue = deque()
        v_init = self.root
        v_init.color = 'gray'
        v_init.pi = None
        v_init.d = 0

        queue.append(v_init)
        discover_list = {}
        while queue:
            curr_v = queue.popleft()
            discover_list[curr_v.d] = discover_list.get(curr_v.d, []) + [curr_v.key]

            for neighbor in curr_v.neighbors:
                if neighbor.color == 'white':
                    neighbor.color = 'gray'
                    neighbor.pi = curr_v
                    neighbor.d = curr_v.d + 1

                    queue.append(neighbor)
            curr_v.color = 'black'

        return discover_list


    @_re_color
    def DFS_recursive(self, re_color = True):
        '''
        Recursively do DFS
        Parameters
        ----------
        re_color

        Returns
        -------

        '''
        if re_color:
            for v in self.vertices.values():
                v.color = 'white'

        self.time = 0

        def helper(curr_v):
            self.time += 1
            curr_v.dt = self.time
            curr_v.color = 'gray'

            for neighbor in curr_v.neighbors:
                if neighbor.color == 'white':
                    neighbor.pi = curr_v
                    helper(neighbor)

            self.time += 1
            curr_v.ft = self.time
            curr_v.color = 'black'

        for v in self.vertices:
            if v.color == 'white':
                helper(v)

        self.time += 1
        v.ft = self.time

    