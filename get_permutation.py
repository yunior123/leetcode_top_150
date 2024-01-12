class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # 1. Create a list of numbers from 1 to n
        nums = [str(num) for num in range(1, n + 1)]
        
        # 2. Create a factorial lookup table
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)
        
        # 3. Find the permutation
        permutation = ''
        k -= 1
        for i in range(n - 1, -1, -1):
            index = k // factorial[i]
            k -= index * factorial[i]
            permutation += nums[index]
            nums.pop(index)
        
        return permutation
        