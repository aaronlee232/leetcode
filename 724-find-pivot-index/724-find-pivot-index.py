class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # get full some of nums array
        total_sum = sum(nums)
        right = 0
        left = 0
        for i in range(len(nums)):
            if i != 0:
                left += nums[i-1]
            right = total_sum - nums[i] - left
            if left == right:
                return i
        return -1
                
                     