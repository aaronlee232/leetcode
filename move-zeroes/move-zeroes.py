class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in reversed(range(len(nums))):
            if nums[i] == 0 and i != len(nums) - 1:
                del nums[i]
                nums.append(0)
                
                