class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs:
            i = 0
            while i < len(prefix) and i < len(word) and word[i] == prefix[i]:
                i += 1
            prefix = word[0:i]
        
        return prefix
        