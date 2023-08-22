from LeetCodeProblemList.SameTree.ST import isSameTree, TreeNode


class TestSameTree:
    case_1 = [
        TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3)),
        TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=3))
    ]

    case_2 = [
        TreeNode(val=1, left=TreeNode(val=2)),
        TreeNode(val=1, left=None, right=TreeNode(val=2))
    ]

    case_3 = [
        TreeNode(val=1, left=TreeNode(val=2), right=TreeNode(val=1)),
        TreeNode(val=1, left=TreeNode(val=1), right=TreeNode(val=2))
    ]

    def test_on_empty_tree(self):
        assert isSameTree(None, None) is True
        assert isSameTree(None, TreeNode()) is False
        assert isSameTree(TreeNode(), None) is False

    def test_case_1(self):
        assert isSameTree(*self.case_1) is True

    def test_case_2(self):
        assert isSameTree(*self.case_2) is False

    def test_case_3(self):
        assert isSameTree(*self.case_3) is False

