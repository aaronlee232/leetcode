class Solution:
    def isValid(self, s: str) -> bool:
        # Need to check brackets from start to finish. 
        # When open bracket is seen, keep type in mind move on to next character
        # When closed bracket is seen, recall previous open bracket and verify matching types before moving on
        # Mimics stack functionality

        # keep track of open brackets
        # Itterate through string s
        # add open bracket to stack if open bracket seen
        # pop latest open bracket from stack if closed bracket seen
        # check for an existing open bracket and matching type

        # Cases:
        # 1. close bracket, but no previous unclosed open brackets
        # 2. close bracket, but no matching previous oepn bracket
        # 3. open bracket remains unclosed by end of string 
        
        bracket_pairs = {'(': ')', '{': '}', '[': ']'}
        opened_brackets = []
        for bracket in s:
            if bracket in bracket_pairs:
                # Open bracket: Add to seen list
                opened_brackets.append(bracket)
            else: 
                # Closed bracket edge case: Check for existing open brackets
                if len(opened_brackets) == 0:
                    return False

                # Closed bracket: Check for matching open bracket
                recent_open = opened_brackets.pop()
                if bracket_pairs[recent_open] != bracket:
                    return False

        # Open bracket edge case: Check for remaining unclosed brackets
        if len(opened_brackets) > 0:
            return False

        return True
