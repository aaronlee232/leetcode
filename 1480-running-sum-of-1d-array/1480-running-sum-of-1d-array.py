class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running = []
        sm = 0
        for i in range(len(nums)):
            sm += nums[i]
            running.append(sm)
        return running