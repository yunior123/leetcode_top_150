
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diagonal = 0
        max_area = 0
        for i in range(len(dimensions)):
            diagonal = (dimensions[i][0] ** 2 + dimensions[i][1] ** 2) ** 0.5
            area = dimensions[i][0] * dimensions[i][1]
            if diagonal > max_diagonal:
                max_diagonal = diagonal
                max_area = area
            elif diagonal == max_diagonal:
                max_area = max(area, max_area)
        return max_area
    
# test
s = Solution()
dimensions = [[9,3],[8,6]]
print(s.areaOfMaxDiagonal(dimensions))
dimensions = [[3,4],[4,3]]
print(s.areaOfMaxDiagonal(dimensions))
    

# [[9,3],[8,6]] -> 48
# [[3,4],[4,3]] -> 12