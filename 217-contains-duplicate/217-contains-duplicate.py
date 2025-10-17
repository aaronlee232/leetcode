class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return self.bruteForce(nums)
        # return self.improvedBruteForce(nums)
        return self.sortedSolution(nums)
        # return self.setSolution(nums)

    # Time efficiency: O(n^2)
    # Space complexity: O(1)
    def bruteForce(self, nums: List[int]):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (i != j and nums[i] == nums[j]):
                    return True
        return False

    # Time efficiency: O(n^2)
    # Space complexity: O(1)
    def improvedBruteForce(self, nums: List[int]):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] == nums[j]):
                    return True
        return False

    # Time complexity: O(nlogn)
    # Space complexity: O(n) sort() uses auxillary space  
    def sortedSolution(self, nums: List[int]):
        nums.sort()
        for i in range(1, len(nums)):
            if (nums[i] == nums[i-1]):
                return True
        return False 

    # Time complexity: O(nlogn)
    # Space complexity: O(n)
    def setSolution(self, nums: List[int]):
        nums_set = set(nums)
        return len(nums_set) != len(nums)
        