from typing import List


class Solution:
    @staticmethod
    def max_area(height: List[int]) -> int:
        res = 0
        for i in range(len(height)):
            for j in range(len(height)):
                if len(height[i:j]) * min(height[i], height[j]) > res:
                    res = len(height[i:j]) * min(height[j], height[i])
        return res

    @staticmethod
    def max_area_alt(height: List[int]) -> int:
        res_area = 0
        l = 0
        r = len(height) - 1

        while l < r:
            curr_area = min(height[l], height[r]) * (r - l)
            res_area = max(res_area, curr_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res_area
