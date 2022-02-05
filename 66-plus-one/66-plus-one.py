class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i, digit in reversed(list(enumerate(digits))):
            val = digit + carry
            carry, newDigit = divmod(val,10)
            digits[i] = newDigit
        
        if carry > 0:
            digits.insert(0, carry)
        
        return digits