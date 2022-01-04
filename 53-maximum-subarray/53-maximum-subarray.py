class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSumForIndex = [None] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                maxSumForIndex[i] = nums[i]
            else:
                maxSumForIndex[i] = max(maxSumForIndex[i-1] + nums[i], nums[i])

        maxSum = maxSumForIndex[0]
        for curSum in maxSumForIndex:
            maxSum = max(maxSum, curSum)
        
        return maxSum
                                