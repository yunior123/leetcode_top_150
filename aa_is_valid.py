class Solution:
    def isValid(self, s: str) -> bool:

        open_b = []

        match_dict = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }

        for char in s:
            if char in match_dict:
                open_b.append(char)
            else:
                if not open_b or (match_dict[open_b[-1]] != char):
                    return False
                open_b.pop()

        return not open_b