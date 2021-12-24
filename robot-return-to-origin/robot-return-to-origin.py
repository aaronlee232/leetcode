class Solution:
    def judgeCircle(self, moves: str) -> bool:
        yChange = 0
        xChange = 0
        for c in moves:
            if c == 'U':
                yChange += 1
            elif c== 'D':
                yChange -= 1
            elif c == 'R':
                xChange += 1
            elif c == 'L':
                xChange -= 1
        if xChange == yChange == 0:
            return True
        else:
            return False
        