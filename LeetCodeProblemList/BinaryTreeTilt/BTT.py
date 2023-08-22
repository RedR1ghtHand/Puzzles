from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findTilt(root: Optional[TreeNode]) -> int:
    result_tilt = [0]

    def calculate_tilt(node, tilt):
        if not node:
            return 0

        left = calculate_tilt(node.left, tilt)
        right = calculate_tilt(node.right, tilt)
        tilt[0] += abs(left - right)

        return left + right + node.val

    calculate_tilt(root, result_tilt)
    return result_tilt[0]

