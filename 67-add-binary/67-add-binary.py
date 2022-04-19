class Solution:
    def addBinary(self, a: str, b: str) -> str:
        #convert to list for easy popping
        a = list(a)
        b = list(b)
        
        val = ''
        carry = 0
        #continue until a, b, and carry are all 0 
        while a or b or carry:
            if a:
                carry += int(a.pop(-1))
            if b:
                carry += int(b.pop(-1))
            val = str(carry % 2) + val
            carry //= 2
        return val
        