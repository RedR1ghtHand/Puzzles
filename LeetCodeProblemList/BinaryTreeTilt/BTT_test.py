from LeetCodeProblemList.BinaryTreeTilt.BTT import TreeNode, findTilt


class TestFindTilt:
    case_1 = TreeNode(
        val=1,
        left=TreeNode(val=2),
        right=TreeNode(val=3)
    )
    case_2 = TreeNode(
        val=4,
        left=TreeNode(
            val=2,
            left=TreeNode(val=3),
            right=TreeNode(val=5)
        ),
        right=TreeNode(
            val=9,
            right=TreeNode(val=7)
        )
    )
    case_3 = TreeNode(
        val=21,
        left=TreeNode(
            val=7,
            left=TreeNode(
                val=1,
                left=TreeNode(val=3),
                right=TreeNode(val=3)
            ),
            right=TreeNode(val=1)
        ),
        right=TreeNode(
            val=14,
            left=TreeNode(val=2),
            right=TreeNode(val=2)
        )
    )

    def test_case_1(self):
        assert findTilt(self.case_1) == 1

    def test_case_2(self):
        assert findTilt(self.case_2) == 15

    def test_case_3(self):
        assert findTilt(self.case_3) == 9
