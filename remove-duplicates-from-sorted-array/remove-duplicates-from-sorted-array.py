class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        def remove(i, end):
            for i in range(i, end - 1):
                nums[i] = nums[i + 1]
        end = len(nums)
        prev = None
        i = end - 1
        while i >= 0:
            if nums[i] == prev:
                remove(i, end)
                end -= 1
            prev = nums[i]
            i -= 1
        return end