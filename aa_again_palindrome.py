class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = f"{x}"

        for i, s in enumerate(x_str):

            if x_str[len(x_str) - 1 -i] != s:
                return False

        return True

         

   