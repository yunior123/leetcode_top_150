from typing import List

# get row from pascal's triangle
# Input: rowIndex = 3 Output: [1,3,3,1]
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #Create a list to store the values
        values = []
        #Create a helper function to create the triangle
        def createTriangle(rowIndex):
            #If the row index is 0
            if rowIndex == 0:
                #Return [1]
                return [1]
            #If the row index is 1
            if rowIndex == 1:
                #Return [1,1]
                return [1,1]
            #Create a list to store the values
            row = [1]
            #Create a variable to store the previous row
            prevRow = createTriangle(rowIndex - 1)
            #Loop through the previous row
            for i in range(len(prevRow) - 1):
                #Add the sum of the current element and the next element to the list
                row.append(prevRow[i] + prevRow[i+1])
            #Add 1 to the list
            row.append(1)
            #Return the list
            return row
        #Call the helper function
        return createTriangle(rowIndex)
    

#Test cases
solution = Solution()
answer = solution.getRow(3)
assert answer == [1,3,3,1], f"Wrong answer: {answer}"
print('Passed all test cases!')



        