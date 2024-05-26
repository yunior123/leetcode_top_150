

from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        good_pairs_count = 0
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] % (nums2[j] * k) == 0:
                    good_pairs_count += 1
        
        return good_pairs_count

# Example usage:
solution = Solution()
print(solution.numberOfPairs([1, 3, 4], [1, 3, 4], 1))  # Output: 5
print(solution.numberOfPairs([1, 2, 4, 12], [2, 4], 3))  # Output: 2
