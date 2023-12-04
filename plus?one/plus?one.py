
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # none, empty or 0
        if not digits:
            return []
        m = map(str, digits)
        num = int(''.join(m)) + 1
        return [int(i) for i in str(num)]


if __name__ == '__main__':
    digits = [1, 2, 3]
    print(Solution().plusOne(digits))
    # none, empty or 0
    digits = []
    print(Solution().plusOne(digits))
    digits = [0]
    print(Solution().plusOne(digits))
    # other
    digits = [9]
    print(Solution().plusOne(digits))