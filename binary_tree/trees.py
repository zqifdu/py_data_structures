"""
Author: Zhenyi Qi
link:
"""

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
    def __init__(self):
        self.root = None
        self.nodes = {}
        self.num_nodes = len(self.nodes)


    def set_root(self, root):
        if isinstance(root, int):
            root = node(root)
        self.root = root
        self.nodes = {root.key: root}
        self.num_nodes = len(self.nodes)


    def add_edge(self, parent, child, left_or_right = 'left'):
        if isinstance(parent, int):
            parent = self.nodes[parent]
        if isinstance(child, int):
            child = self.nodes.get(child, node(child))

        self.nodes[child.key] = child

        self.num_nodes = len(self.nodes)
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

    def lca(self, n1, n2):
        '''
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

