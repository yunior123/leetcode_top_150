
from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0

        # Iterate through each word, checking for prefix-suffix pairs with subsequent words
        for i in range(n):
            for j in range(i + 1, n):
                word1 = words[i]
                word2 = words[j]

                # Efficiently check for prefix and suffix conditions
                if word2.startswith(word1) and word2.endswith(word1):
                    count += 1

        return count




# test
res = Solution().countPrefixSuffixPairs(["a","aba","ababa","aa"])
print(res) # 4

res = Solution().countPrefixSuffixPairs(["pa","papa","ma","mama"])
print(res) # 2

res = Solution().countPrefixSuffixPairs(["abab","ab"])
print(res) # 0