class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLength = 0
        for num in numSet:
            if num - 1 not in numSet:
                curNum = num
                length = 1
            
                while curNum + 1 in numSet:
                    curNum += 1
                    length += 1
            
                maxLength = max(maxLength, length)
        return maxLength
                
                