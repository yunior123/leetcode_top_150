
from typing import List
from collections import Counter

# class Solution:
#     def mostFrequentPrime(self, mat: List[List[int]]) -> int:
#         m, n = len(mat), len(mat[0])
#         directions = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))  # Possible directions

#         prime_counts = Counter()
#         for i in range(m):
#             for j in range(n):
#                 for dx, dy in directions:
#                     x, y = i, j
#                     num = 0
#                     while 0 <= x < m and 0 <= y < n:
#                         num = num * 10 + mat[x][y]
#                         if num > 10 and self.is_prime(num):
#                             prime_counts[num] += 1
#                         x += dx
#                         y += dy

#         if not prime_counts:
#             return -1

#         most_frequent_prime = prime_counts.most_common(1)[0][0]  # Get the most frequent prime number
#         return most_frequent_prime


#     def is_prime(self,num):

#         if num <= 1:
#             return False
#         if num <= 3:
#             return True
#         if num % 2 == 0 or num % 3 == 0:
#             return False
#         i = 5
#         while i * i <= num:
#             if num % i == 0 or num % (i + 2) == 0:
#                 return False
#             i += 6
#         return True

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

        def is_prime(num: int) -> bool:
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

        def generate_numbers(row, col) -> List[int]:
            numbers = []
            for dx, dy in directions:
                x, y = row, col
                num = mat[row][col]
                while 0 <= x + dx < m and 0 <= y + dy < n:
                    num = num * 10 + mat[x + dx][y + dy]
                    if num > 10 and is_prime(num):
                        numbers.append(num)
                    x, y = x + dx, y + dy
            return numbers

        freq_map = {}
        for row in range(m):
            for col in range(n):
                numbers = generate_numbers(row, col)
                for num in numbers:
                    freq_map[num] = freq_map.get(num, 0) + 1

        max_freq = -1
        most_frequent_prime = -1
        for prime, freq in freq_map.items():
            if freq > max_freq:
                max_freq = freq
                most_frequent_prime = prime
            elif freq == max_freq and prime > most_frequent_prime:
                most_frequent_prime = prime

        return most_frequent_prime


# test
mat = [[1,1],[9,9],[1,1]]
sol = Solution()
print(sol.mostFrequentPrime(mat)) # 19
mat = [[7]]
print(sol.mostFrequentPrime(mat)) # -1
mat = [[9,7,8],[4,6,5],[2,8,6]]
print(sol.mostFrequentPrime(mat)) # 97
mat = [[1,2,6],[7,9,8]]
print(sol.mostFrequentPrime(mat)) # 97

    
      