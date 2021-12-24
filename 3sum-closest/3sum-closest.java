class Solution {
    public int threeSumClosest(int[] nums, int target) {
        
        int currentMaxSum = Integer.MIN_VALUE;
        int sum = 0;
        
        for(int i = 0; i < nums.length; i++) {
           for(int j = i+1; j < nums.length; j++) {
                for(int k = j+1; k < nums.length; k++) {
                    sum = nums[i] + nums[j] + nums[k];
                    // System.out.println(nums[i] +" " +  nums[j]+ " " + nums[k] + " sum: " + sum + " distance from target: " + Math.abs(target-sum) + " record distance: " + Math.abs(target-currentMaxSum));
                    
                    if(Math.abs(target-sum) < Math.abs(target-currentMaxSum) || currentMaxSum == Integer.MIN_VALUE) {
                        currentMaxSum = sum;
                    }
                }
            } 
        }
        
        // if(currentMaxSum == Integer.MIN_VALUE) {
        //     currentMaxSum = sum;
        // }
        return currentMaxSum;
    }
}