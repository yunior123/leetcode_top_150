from typing import List

def removeDuplicates(nums: List[int]) -> int:
    temp = []
    for n in nums:
        if not(n in temp):
            temp.append(n)
    nums = temp
    return len(nums)


removeDuplicates([1,1,2])