class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        if not strs:
            return output

        for i, char in enumerate(strs[0]):

            for j, word in enumerate(strs):
                if i >= len(word) or word[i] != char:
                    return output
                
            output += char
        
        return output