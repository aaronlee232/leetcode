class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two pointers indicating end of substring
        # a set containing character in substring
        # advance r while no duplicates in set
        # when duplicate is found, advance l until duplicate character is found, and keep advancing until a different character is found
        # update max length with every change in substring
        
        maxLength = 0
        sub = {} 
        for i in range(len(s)):
            c = s[i]
            if c in sub.keys():
                while list(sub)[0] != c:
                    sub.pop(list(sub)[0])
                sub.pop(list(sub)[0])
                sub[c] = i
            else:
                sub[c] = i
            maxLength = max(maxLength, len(sub))
        return maxLength