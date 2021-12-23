class Solution {
    public int countBalls(int lowLimit, int highLimit) {
        HashMap<Integer, Integer> boxToFreq = new HashMap<>();
        int maxSum = 0;
        for(int num = lowLimit; num <= highLimit; num++) {
            int sum = getSum(num);
            if(!boxToFreq.containsKey(sum)) {
                boxToFreq.put(sum, 1);
            } else {
                boxToFreq.put(sum, boxToFreq.get(sum) + 1);
            }
            if(maxSum == 0 || boxToFreq.get(sum) > boxToFreq.get(maxSum)) {
                    System.out.println(boxToFreq.get(sum));
                    maxSum = sum;   
            }
            
        }
        return (maxSum == 0) ? 0 : boxToFreq.get(maxSum);
    }
    
    private int getSum(int num) {
        int sum = 0;
        while(num != 0) {
            int digit = num % 10;
            sum += digit;
            num = (num - digit) / 10;
        }
        return sum;
    }
}