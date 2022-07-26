class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexTarget = dict()
        for i in range(len(nums)):
            if nums[i] in indexTarget:
                return [indexTarget[nums[i]], i]
            key = target - nums[i]
            indexTarget[key] = i
        return []