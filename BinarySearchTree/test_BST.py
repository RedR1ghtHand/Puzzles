from BinarySearchTree.BST import Tree


class TestBST:
    def test_insert(self):
        tree = Tree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(8)
        assert tree.root.data == 5
        assert tree.root.left.data == 3
        assert tree.root.right.data == 8

    def test_search(self):
        tree = Tree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(8)
        assert tree.search(5) == 5
        assert tree.search(3) == 3
        assert tree.search(8) == 8
        assert tree.search(10) is None

    def test_search_min(self):
        tree = Tree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(8)
        assert tree.search_min().data == 3

    def test_search_max(self):
        tree = Tree()
        tree.insert(5)
        tree.insert(3)
        tree.insert(8)
        assert tree.search_max().data == 8

    def test_remove_node_empty_tree(self):
        bst = Tree()
        bst.remove(5)
        assert bst.root is None

    def test_remove_node_single_node_tree(self):
        bst = Tree()
        bst.insert(5)
        bst.remove(5)
        assert bst.root is None

    def test_remove_node_with_left_child(self):
        bst = Tree()
        bst.insert(5)
        bst.insert(3)
        bst.remove(5)
        assert bst.root.data == 3
        assert bst.root.left is None
        assert bst.root.right is None

    def test_remove_node_with_right_child(self):
        bst = Tree()
        bst.insert(5)
        bst.insert(8)
        bst.remove(5)
        assert bst.root.data == 8
        assert bst.root.left is None
        assert bst.root.right is None

    def test_remove_node_with_two_children(self):
        bst = Tree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(8)
        bst.remove(5)
        assert bst.root.data == 8
        assert bst.root.left.data == 3
        assert bst.root.right is None

    def test_remove_node_complex_case(self):
        bst = Tree()
        bst.insert(5)
        bst.insert(3)
        bst.insert(8)
        bst.insert(2)
        bst.insert(4)
        bst.insert(7)
        bst.insert(9)
        bst.remove(5)
        assert bst.root.data == 7
        assert bst.root.left.data == 3
        assert bst.root.right.data == 8
        assert bst.root.left.left.data == 2
        assert bst.root.left.right.data == 4
        assert bst.root.right.left is None
        assert bst.root.right.right.data == 9
