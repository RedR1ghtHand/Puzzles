import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            cur = self.root
            while cur:
                if cur.data > data:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(data)
                        return
                else:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = Node(data)
                        return

    def remove(self, key):
        if self.root is not None:
            self.root = self._remove_rec(self.root, key)

    def _remove_rec(self, root, key):
        if root is None:
            return root
        if key < root.data:
            root.left = self._remove_rec(root.left, key)
        elif key > root.data:
            root.right = self._remove_rec(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min_right_subtree = self.search_min(root.right)
            root.data = min_right_subtree.data
            root.right = self._remove_rec(root.right, min_right_subtree.data)
        return root

    def search_min(self, node=None):
        if node is None:
            node = self.root
        while node.left is not None:
            node = node.left
        return node

    def search_max(self, node=None):
        if node is None:
            node = self.root
        while node.right is not None:
            node = node.right
        return node

    def search(self, val):
        current = self.root
        while current is not None:
            if val == current.data:
                return current.data
            elif val < current.data:
                current = current.left
            else:
                current = current.right
        return None

    def display(self):

        def plot_node(node, x, y):
            if node:
                plt.text(x, y, str(node.data), color="white", fontweight='bold', ha='center', va='center',
                         bbox=dict(facecolor='blue', edgecolor='black', boxstyle='circle'))

                if node.left:
                    plt.plot([x, x - 1], [y, y - 1], 'b-', linewidth=1.5)
                    plot_node(node.left, x - 1, y - 1)

                if node.right:
                    plt.plot([x, x + 1], [y, y - 1], 'b-', linewidth=1.5)
                    plot_node(node.right, x + 1, y - 1)

        if self.root:
            fig, ax = plt.subplots()
            plot_node(self.root, 0, 0)
            ax.set_axis_off()
            plt.show()


if __name__ == '__main__':
    bst = Tree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(40)
    bst.insert(100)
    bst.insert(10)
    print(bst.search(10))
    bst.display()