class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.inclusive_itter_search(nums, target)
        # return self.recursive_inclusive_search(0, len(nums) - 1, nums, target)

    def inclusive_itter_search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while (low <= high):
            mid = (low + high) // 2
            if (nums[mid] > target):
                high = mid - 1
            elif (nums[mid] < target):
                low = mid + 1
            else:   
                return mid
        return -1
            
    def exclusive_itter_search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        
        while (low < high):
            mid = (low + high) // 2
            if (nums[mid] > target):
                high = mid
            elif (nums[mid] < target):
                low = mid + 1
            else:
                return mid
        return -1
            
    def recursive_inclusive_search(self, low: int, high: int, nums: List[int], target: int) -> int:
        # Not found exit condition
        if (low > high):
            return -1

        mid = (low + high) // 2

        # Found exit condition
        if (nums[mid] == target):
            return mid
        
        if (nums[mid] > target):
            return self.recursive_inclusive_search(low, mid - 1, nums, target)
        else:
            return self.recursive_inclusive_search(mid + 1, high, nums, target)

    def recursive_exclusive_search(self, low: int, exc_high: int, nums: List[int], target: int) -> int:
        # Not found exit condition
        if (low > exc_high):
            return -1

        mid = (low + exc_high) // 2

        # Found exit condition
        if (nums[mid] == target):
            return mid
        
        if (nums[mid] > target):
            return self.recursive_inclusive_search(low, mid, nums, target)
        else:
            return self.recursive_inclusive_search(mid + 1, exc_high, nums, target)