from typing import List
def removeElement(nums: List[int], val: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i += 1
    print(nums)
    return len(nums)


print(removeElement([3,2,2,3], 3)) # 2