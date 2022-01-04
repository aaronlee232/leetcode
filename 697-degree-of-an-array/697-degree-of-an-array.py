class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        numToFreq = {}
        
        # get all frequencies
        for num in nums:
            if num in numToFreq:
                numToFreq[num] += 1
            else:
                numToFreq[num] = 1
        
        # find degree of array
        degree = 0
        for num in numToFreq.keys():
            if numToFreq[num] > degree:
                degree = numToFreq[num]
        
        # find numbers that share same frequency as degree
        maxFreqNums = []
        for num in numToFreq.keys():
            if numToFreq[num] == degree:
                maxFreqNums.append(num)
        
        # find shortest subarray
        shortest = len(nums)
        for i in range(len(nums)):
            num = nums[i]
            if num in maxFreqNums:
                length = 1
                seen = 1
                j = i + 1
                while seen < degree:
                    if nums[j] == num:
                        seen += 1
                    j += 1
                    length += 1
                shortest = min(shortest, length)
                maxFreqNums.remove(num)
        
        return shortest
                        
                    
        