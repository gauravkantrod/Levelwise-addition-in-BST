from BSTnode import Node


class tree_ops:
    def create_tree(self):
        root = Node(1)

        root.left = Node(2);
        root.right = Node(3);

        root.left.left = Node(4);
        root.left.right = Node(5);
        root.right.left = Node(6);
        root.right.right = Node(7);

        root.left.left.left = Node(8);
        root.left.left.right = Node(9);
        root.left.right.left = Node(10);
        root.left.right.right = Node(11);
        root.right.left.left = Node(12);
        root.right.right.left = Node(13);
        root.right.left.right = Node(14);
        root.right.right.right = Node(15);

        return root

    def bfs_level_summation(self, root, level):
        count = 0
        total = 0

        q = []
        q.append(root)
        q.append(None)

        while q:
            p = q.pop(0)

            if p is None:
                return

            if count == level:
                total += p.data

            # print(p.data, end = ' ')

            if p.left:
                q.append(p.left)
            if p.right:
                q.append(p.right)

            if q[0] is None:
                q.pop(0)
                # print()
                q.append(None)
                count = count + 1

                if count > level:
                    print("Total at level {} is {}".format(level, total))
                    return
                sum = 0