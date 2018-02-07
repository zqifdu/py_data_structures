"""
Author: Zhenyi Qi
link:
"""
from functools import wraps

class node(object):
    '''
    Node of a binary tree
    '''
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None


class binary_tree(object):
    '''
    A binary tree
    '''

    def __init__(self):
        self.root = None
        self.nodes = {}
        self.num_nodes = len(self.nodes)


    def _update_num_nodes(func):
        @wraps(func)
        def _num_nodes_wrapper(self, *args, **kwargs):
            results = func(self, *args, **kwargs)
            self.num_nodes = len(self.nodes)
            return results
        return _num_nodes_wrapper


    @_update_num_nodes
    def set_root(self, root):
        if isinstance(root, int):
            root = node(root)
        self.root = root
        self.nodes = {root.key: root}

    @_update_num_nodes
    def add_edge(self, parent, child, left_or_right = 'left'):
        if isinstance(parent, int):
            parent = self.nodes[parent]
        if isinstance(child, int):
            child = self.nodes.get(child, node(child))

        self.nodes[child.key] = child
        self.nodes[child.key].parent = parent

        if left_or_right == 'left':
            parent.left = child
        else:
            parent.right = child


    def pre_order(self, root):
        '''
        Pre-order traversal of the binary tree
        Parameters
        ----------
        root            : root of a tree or subtree

        Returns
        -------
        list of keys of all elements in pre-order
        '''
        # Base case
        if root is None:
            return []

        pre_order_list = [root.key]
        pre_order_list = pre_order_list + self.pre_order(root.left)
        pre_order_list = pre_order_list + self.pre_order(root.right)

        return pre_order_list



    def in_order(self, root):
        '''
        In order traversal of the binary tree
        Parameters
        ----------
        root            : root of a tree or subtree

        Returns
        -------
        list of keys of all elements in order
        '''
        # Base case
        if root is None:
            return []

        in_order_list = self.in_order(root.left)
        in_order_list.append(root.key)
        in_order_list = in_order_list + self.in_order(root.right)

        return in_order_list


    def post_order(self, root):
        '''
        Post order traversal of the binary tree
        Parameters
        ----------
        root            : root of a tree or subtree

        Returns
        -------
        list of keys of all elements in post-order
        '''
        # Base case
        if root is None:
            return []

        post_order_list = self.post_order(root.left)
        post_order_list = post_order_list + self.post_order(root.right)
        post_order_list.append(root.key)

        return post_order_list


    def level_order(self, root, depth, depth_dict):
        '''
        Level-order traversal of a tree
        Parameters
        ----------
        root        : root of a tree or a subtree
        depth       : depth of current node in the whole tree
        depth_dict  : depth_dict of the whole tree

        Returns
        -------
        depth_dict
        '''

        if depth in depth_dict:
            depth_dict.get(depth).append(root.key)
        else:
            depth_dict[depth] = [root.key]
        if root.left:
            self.level_order(root.left, depth + 1, depth_dict)
        if root.right:
            self.level_order(root.right, depth + 1, depth_dict)

        return depth_dict


    def vertical_order(self, root, vert_coord , vert_dict):
        if root is None:
            return
        try:
            vert_dict[vert_coord].append(root.key)
        except:
            vert_dict[vert_coord] = [root.key]

        self.vertical_order(root.left, vert_coord - 1, vert_dict)
        self.vertical_order(root.right, vert_coord + 1, vert_dict)

        return vert_dict

    def top_view(self, root):
        '''
        Return a list of keys of nodes that can be seen from the top.
        Parameters
        ----------
        root

        Returns
        -------

        '''
        vert_dict = self.vertical_order(root, 0, {})
        top_view_list = []
        for vert_coord in sorted(vert_dict.keys()):
            top_view_list.append(vert_dict[vert_coord][0])

        return top_view_list


    def lca(self, n1, n2):
        '''
        Find the lowest common ancerstry of n1 and n2; application of pre-order and post-order traversal
        Parameters
        ----------
        n1: node 1
        n2: node 2

        Returns
        -------
        node which is the lowest common ancestry of n1 and n2.
        '''
        if isinstance(n1, int):
            n1 = self.nodes[n1]
        if isinstance(n2, int):
            n2 = self.nodes[n2]

        in_order_list = self.in_order(self.root)
        post_order_list = self.post_order(self.root)

        key1 = n1.key
        key2 = n2.key
        index_1 = in_order_list.index(key1)
        index_2 = in_order_list.index(key2)

        index_max_post = -1
        if index_2 + 1 < len(in_order_list):
            for ele in in_order_list[index_1:index_2+1]:
                index_max_post = max(post_order_list.index(ele), index_max_post)
        else:
            for ele in in_order_list[index_1:index_2]:
                index_max_post = max(post_order_list.index(ele), index_max_post)

        key_lowest_common_ance = post_order_list[index_max_post]
        lowest_common_ance = self.nodes[key_lowest_common_ance]

        return lowest_common_ance






