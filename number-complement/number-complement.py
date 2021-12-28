class Solution:
    def findComplement(self, num: int) -> int:
        # mask for 3,4,5,6 bits = 111, 1111, 11111, 111111, so on
        # creates a mask by shifting over 1 by n bits to create n number of trailing 0s with 1 extra bit at the front
        # subtracting 1 then reduces mask to correct length and fills in with all 1s
        return num ^ ((1 << num.bit_length()) - 1)