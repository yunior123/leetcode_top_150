

from typing import List


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Finds the length of the longest common prefix among all pairs of integers
        across two input arrays.

        Args:
            arr1: First array of positive integers.
            arr2: Second array of positive integers.

        Returns:
            The length of the longest common prefix, or 0 if none exists.
        """

        def common_prefix_length(str1, str2):
            """
            Calculates the length of the common prefix between two strings.
            """
            i = 0
            while i < min(len(str1), len(str2)) and str1[i] == str2[i]:
                i += 1
            return i

        # Convert integers to strings for efficient prefix comparison
        str_arr1 = [str(num) for num in arr1]
        str_arr2 = [str(num) for num in arr2]

        longest_prefix_len = 0
        for num1 in str_arr1:
            for num2 in str_arr2:
                longest_prefix_len = max(
                    longest_prefix_len, common_prefix_length(num1, num2)
                )

        return longest_prefix_len

# test
res = Solution().longestCommonPrefix([1, 10, 100], [1000])
print(res)  # 3
res = Solution().longestCommonPrefix([1, 2, 3], [4, 4, 4])
print(res)  # 0



# test
res = Solution().longestCommonPrefix([1,10,100], [1000])
print(res) # 3

res = Solution().longestCommonPrefix([1,2,3], [4,4,4])
print(res) # 0
