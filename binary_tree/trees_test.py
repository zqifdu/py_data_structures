from binary_tree.trees import binary_tree


# ================ test of binary tree ================
bt = binary_tree()

# tree
#        3
#       / \
#      4   2
#     /   / \
#    8   5   6

bt.set_root(3)
print(bt.nodes)

bt.add_edge(3, 4)
bt.add_edge(3, 2, 'right')

bt.add_edge(2, 5)
bt.add_edge(2, 6, 'right')

bt.add_edge(4, 8)

print(bt.num_nodes)

# in_order
root = bt.root
print(bt.in_order(root))

# post_order
print(bt.post_order(root))

# Pre-order
print(bt.pre_order(root))

# LCA
print(bt.lca(3, 4).key)
print(bt.lca(4, 5).key)
print(bt.lca(5, 6).key)
