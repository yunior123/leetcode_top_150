from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


        # Find the first decreasing number from the right
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        # Find the first number greater than nums[i] from the right
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1

            # Swap the two numbers
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the numbers from i+1 to the end
        nums[i+1:] = nums[i+1:][::-1]




if __name__ == "__main__":
    nums = [1, 1,5]
    Solution().nextPermutation(nums)
    print(nums) # [1, 5, 1]



