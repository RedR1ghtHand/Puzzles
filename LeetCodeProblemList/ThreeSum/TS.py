from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    # generic solution
    res = []
    for i in range(len(nums)):
        for j in range(1, len(nums)):
            for k in range(2, len(nums)):
                if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
                    res.append([nums[i], nums[j], nums[k]])
    return res


def three_sum_with_two_pointers(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -= 1
            else:
                triplet = [nums[i], nums[l], nums[r]]
                result.append(triplet)
                while l < r and nums[l] == triplet[1]:
                    l += 1
                while l < r and nums[r] == triplet[2]:
                    r -= 1
    return result
