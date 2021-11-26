class Solution {
    public int searchInsert(int[] nums, int target) {
        return searchHelper(nums, target, 0, nums.length - 1);
    }
    
    private int searchHelper(int[] nums, int target, int low, int high) {
        if(low > high) {
            return low;
        }
        
        int mid = (low + high)/2;
        
        if(nums[mid] == target) {
            return mid;
        } else if(nums[mid] > target) {
            return searchHelper(nums, target, low, mid - 1);
        } else {
            return searchHelper(nums, target, mid + 1, high);
        }
    }
}