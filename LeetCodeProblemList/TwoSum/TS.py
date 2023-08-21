class TS:
    def twoSum(self, nums, target: int):
        for _ in range(len(nums)):
            for __ in range(_+1, len(nums)):
                if nums[_] + nums[__] == target:
                    return [_, __]
