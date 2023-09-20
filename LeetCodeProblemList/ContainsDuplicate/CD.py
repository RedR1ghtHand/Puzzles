from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        for num in nums:
            for item in nums[nums.index(num)+1::]:
                if num == item:
                    return True
        return False


    def contains_duplicate_alt(self, nums: List[int]) -> bool:
        lnght = len(nums)
        for num in range(lnght-1):
            for item in range(num+1, lnght):
                if nums[num] == nums[item]:
                    return True
        return False


    def contains_duplicate_hash_set(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        return True

