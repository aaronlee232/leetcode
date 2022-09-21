class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = [None] * len(nums)
        sm = 0
        for i in range(len(nums)):
            sm += nums[i]
            running[i] = sm
        return running