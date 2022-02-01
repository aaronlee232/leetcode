class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nextAvailable = 0;
        
        for num in nums:
            if num != val:
                nums[nextAvailable] = num
                nextAvailable += 1
        
        return nextAvailable