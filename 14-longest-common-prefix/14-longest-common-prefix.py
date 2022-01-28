class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for word in strs:
            i = 0
            newPrefix = ""
            while i < len(prefix) and i < len(word) and word[i] == prefix[i]:
                newPrefix += prefix[i]
                i += 1
            prefix = newPrefix
        
        return prefix
        