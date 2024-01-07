
from collections import Counter
from typing import List


class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        
        x1 = set(nums1)
        x2 = set(nums2)
        
        if len(x1 - x2) >= n // 2:
            return n // 2 + min(len(x2), n // 2)
        if len(x2 - x1) >= n // 2:
            return n // 2 + min(len(x1), n // 2)
        
        a, b = len(x1 - x2), len(x2 - x1)
        c = len(x1 & x2)
        return min(a + b + c, n)



    
    
# test
s = Solution()
nums1 = [1,2,1,2]
nums2 = [1,1,1,1]
print(s.maximumSetSize(nums1, nums2)) # 2
nums1 = [1,2,3,4,5,6]
nums2 = [2,3,2,3,2,3]
print(s.maximumSetSize(nums1, nums2)) # 5
nums1 = [1,1,2,2,3,3]
nums2 = [4,4,5,5,6,6]
print(s.maximumSetSize(nums1, nums2)) # 6