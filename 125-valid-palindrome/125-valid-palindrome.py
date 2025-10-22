class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.premadeApproach(s)

    def initialRegexApproach(self, s):
        # Brute force / Initial Approach
        s = s.lower()
        pattern = r"[a-z0-9]"
        s_list = []
        for c in s:
            if re.match(pattern, c):
                s_list.append(c)
        s = "".join(s_list)

        s_reversed = s[::-1]
        if s == s_reversed:
            return True
        else:
            return False
    
    def cleanRegexInitialApproach(self, s):
        pattern = r"[^a-z0-9]"
        replacement = ""
        s = re.sub(pattern, replacement, s.lower())

        s_reversed = s[::-1]
        if s == s_reversed:
            return True
        else:
            return False

    def pointerRegexApproach(self, s):
        s = s.lower()
        alphaNumCharPattern = r"[a-z0-9]"
        l, r = 0, len(s) - 1

        while (l < r):
            # Continues to skip until alpha num character is reached
            while (l < r and not re.match(alphaNumCharPattern, s[l])):
                l += 1
            while (r > l and not re.match(alphaNumCharPattern, s[r])):
                r -= 1
            if (s[l] == s[r]):
                l += 1
                r -= 1
            else:
                return False
        return True
            
    def nonRegexApproach(self, s):
        s = s.lower()
        alphaChars = set(list(chr(num) for num in range(97, 123)))
        numChars = set(list(str(num) for num in range(0, 10)))
        alphaNumChars = alphaChars.union(numChars)
        print(alphaNumChars)
        l, r = 0, len(s) - 1
        while (l < r):
            # Continues to skip until alpha num character is reached
            while (l < r and s[l] not in alphaNumChars):
                l += 1
            while (r > l and s[r] not in alphaNumChars):
                r -= 1
            if (s[l] == s[r]):
                l += 1
                r -= 1
            else:
                return False
        return True

    def premadeApproach(self, s):
        s = s.lower()
        l, r = 0, len(s) - 1
        while (l < r):
            # Continues to skip until alpha num character is reached
            while (l < r and not s[l].isalnum()):
                l += 1
            while (r > l and not s[r].isalnum()):
                r -= 1
            print(f"{s[l]}{l} {s[r]}{r}")
            if (s[l] == s[r]):
                l += 1
                r -= 1
            else:
                return False
        return True