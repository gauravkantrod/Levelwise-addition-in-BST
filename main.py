from tree_operations import tree_ops

if __name__ == '__main__':
    create_tree = tree_ops()
    root = create_tree.create_tree()
    create_tree.bfs_level_summation(root, 2)