class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 2 == 0:
            return -1
        
        remainder_set = set()
        num = 1
        while num % k != 0:
            if num % k in remainder_set:
                return -1
                
            remainder_set.add(num % k)
            num = num * 10 + 1
            
        return int(math.log(num, 10)) + 1