class Solution:
    def isValid(self, s: str) -> bool:
        #stack to track most recent parenthesis
        #only add opening brackets to stack
        seen = []
        brackets = {'(':')', '{':'}', '[':']'}
        
        for c in s:
            if c in brackets.keys():
                seen.append(brackets[c])
            else:
                if not seen or seen.pop() != c:
                    return False
        return len(seen) == 0