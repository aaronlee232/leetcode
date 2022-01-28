class Solution:
    def isValid(self, s: str) -> bool:
        #in order ( { [
        brackets = [0, 0, 0]
        expected = []
        
        for c in s:
            if c == '(':
                brackets[0] += 1
                expected.append(')')
            elif c == '{':
                brackets[1] += 1
                expected.append('}')
            elif c == '[':
                brackets[2] += 1
                expected.append(']')
            elif len(expected) > 0:
                if c == ')':
                    if expected.pop() == c:
                        brackets[0] -= 1
                        if brackets[0] < 0:
                            return False
                    else:
                        return False
                elif c == '}':
                    if expected.pop() == c:
                        brackets[1] -= 1
                        if brackets[1] < 0:
                            return False
                    else:
                        return False
                elif c == ']':
                    if expected.pop() == c:
                        brackets[2] -= 1
                        if brackets[2] < 0:
                            return False
                    else:
                        return False
            else:
                return False
        if sum(brackets) == 0:
            return True
        else:
            return False