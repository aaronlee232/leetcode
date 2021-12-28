class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # two pointers indicating end of substring
        # a set containing character in substring
        # advance r while no duplicates in set
        # when duplicate is found, advance l until duplicate character is found, and keep advancing until a different character is found
        # update max length with every change in substring
        
        maxLength = 0
        sub = {} 
        start = 0
        for i in range(len(s)):
            c = s[i]
            if c in sub.keys() and start <= sub[c] <= i:
                start = sub[c] + 1
                sub[c] = i
            else:
                sub[c] = i
            maxLength = max(maxLength, i - start + 1)
        return maxLength