from typing import List

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. Find the row
        row = self.find_row(matrix, target)
        
        # 2. Find the column
        column = self.find_column(matrix, row, target)
        
        # 3. Return true if the target is found
        return matrix[row][column] == target
    
    def find_row(self, matrix: List[List[int]], target: int) -> int:
        # 1. Initialize the row
        row = 0
        
        # 2. Find the row
        for i in range(len(matrix)):
            if matrix[i][0] <= target:
                row = i
        
        return row
    
    def find_column(self, matrix: List[List[int]], row: int, target: int) -> int:
        # 1. Initialize the column
        column = 0
        
        # 2. Find the column
        for i in range(len(matrix[row])):
            if matrix[row][i] == target:
                column = i
        
        return column