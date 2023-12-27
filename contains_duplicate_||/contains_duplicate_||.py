from typing import List
# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # create a dictionary to store the index of each element
        index_dict = {}

        # iterate through the list
        for i in range(len(nums)):

            # if the element is not in the dictionary, add it
            if nums[i] not in index_dict:
                index_dict[nums[i]] = i

            # if the element is in the dictionary, check if the difference between the current index and the index of the element in the dictionary is less than or equal to k
            else:
                if i - index_dict[nums[i]] <= k:
                    return True

                # if the difference is greater than k, update the index of the element in the dictionary
                else:
                    index_dict[nums[i]] = i

        return False

        