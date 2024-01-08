from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        
        return nums[left]
    
# test
s = Solution()
nums = [1,3,5]
print(s.findMin(nums)) # 1
nums = [-1,-1,-1,-1]
print(s.findMin(nums)) # -1
