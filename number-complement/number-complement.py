class Solution:
    def findComplement(self, num: int) -> int:
        bits = int(log(num, 2)) + 1
        mask = 2 ** bits - 1
        return num ^ mask