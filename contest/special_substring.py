# You are given a string s that consists of lowercase English letters.

# A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

# Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

# A substring is a contiguous non-empty sequence of characters within a string.
# ex 1
# Input: s = "aaaa"
# Output: 2
# Explanation: The longest special substring which occurs thrice is "aa": substrings "(aa)aa", "a(aa)a", and "aa(aa)".
# It can be shown that the maximum length achievable is 2.
# ex 2
# Input: s = "abcdef"
# Output: -1
# Explanation: There exists no special substring which occurs at least thrice. Hence return -1.
#ex 3
# Input: s = "abcaba"
# Output: 1
# Explanation: The longest special substring which occurs thrice is "a": substrings "(a)bcaba", "abc(a)ba", and "abcab(a)".
# It can be shown that the maximum length achievable is 1.

class Solution:

    def count_substrings(self, s, substring):
        count = 0
        for i in range(len(s)-len(substring)+1):
            if s[i:i+len(substring)] == substring:
                count += 1
        return count
    
    def maximumLength(self, s: str) -> int:
        substrings = []
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                substring = s[i:j]
                if len(set(substring)) == 1:
                    substrings.append(substring)

     
        substrings = list(set(substrings))

        best_substrings = []
        for substring in substrings:
            if self.count_substrings(s, substring) >= 3:
                best_substrings.append(substring)
        if best_substrings:
            return max([len(substring) for substring in best_substrings])
        return -1




        







if __name__ == '__main__':
    solution = Solution()
    assert solution.maximumLength('aaaa') == 2
    assert solution.maximumLength('abcdef') == -1
    assert solution.maximumLength('abcaba') == 1
