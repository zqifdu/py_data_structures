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

bt.add_edge(3, 4)
bt.add_edge(3, 2, 'right')

bt.add_edge(2, 5)
bt.add_edge(2, 6, 'right')

bt.add_edge(4, 8)
try:
    assert bt.nodes[4].parent == bt.nodes[3]
    assert (bt.nodes[5]).parent == bt.nodes[2]
    assert bt.nodes[2].left == bt.nodes[5]
    assert bt.nodes[2].right == bt.nodes[6]
    print('Adding edge passed')
except:
    print('Adding edge failed')

try:
    assert bt.num_nodes == 6
    print('Number of nodes passed')
except:
    print('Number of nodes failed')

# in_order
root = bt.root
try:
    assert bt.in_order(root) == [8, 4, 3, 5, 2, 6]
    print('In-order traversal passed')
except:
    print('In-order traversal failed')

# post_order
try:
    assert bt.post_order(root) == [8, 4, 5, 6, 2, 3]
    print('Post-order traversal passed')
except:
    print('Post-order traversal failed')


# Pre-order
try:
    assert bt.pre_order(root) == [3, 4, 8, 2, 5, 6]
    print('Pre-order traversal passed')
except:
    print('Pre-order traversal failed')


# Level-order
try:
    assert bt.level_order(root, 0, {}) == {0: [3], 1: [4, 2], 2: [8, 5, 6]}
    print('Level-order traversal passed')
except:
    print('Level-order traversal failed')


# Vertical-order
try:
    assert bt.vertical_order(root, 0, {}) == {0:[3, 5], 1:[2], 2:[6], -2:[8], -1:[4]}
    print('Vertical-order traversal passed')
except:
    print('Vertical-order traversal failed')

# Top-view
try:
    assert bt.top_view(root) == [8, 4, 3, 2, 6]
    print('Top view passed')
except:
    print('Top view failed')

# LCA
try:
    assert bt.lca(3, 4).key == 3
    assert bt.lca(4, 5).key == 3
    assert bt.lca(5, 6).key == 2
    print('LCA passed')
except:
    print('LCA faild')
