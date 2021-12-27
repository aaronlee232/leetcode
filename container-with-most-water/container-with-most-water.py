class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointers at either end
        left, right = 0, len(height) - 1
        
        # move pointers toward mid, checking for new max water found
        # only move shorter pointer (only possible way to get a volume larger than current max is to replace shorter)
        # even if a larger length exists close to the current larger pointer, there is no use in moving it while the shorter pointer                 # restricts the height of the water
        
        water = 0
        while left < right:
            # only replace water if a new max is found
            water = max(water, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return water