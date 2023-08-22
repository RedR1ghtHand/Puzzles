from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def depth_fist_search(n1, n2):
        if not n1 and not n2:
            return True
        if not n1 or not n2:
            return False
        if (n1.val == n2.val
                and depth_fist_search(n1.left, n2.left)
                and depth_fist_search(n1.right, n2.right)):
            return True
        else:
            return False
    return depth_fist_search(p, q)







