def isValid(s):
    open_b = []
    dicts = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    
    for value in s:
        if value in dicts:  # Check for opening brackets
            open_b.append(value)
        elif open_b:  # Check if the stack is not empty
            last = open_b.pop()  # Remove the last opened bracket
            if value != dicts[last]:  # Check if it matches the closing bracket
                return False
        else:
            return False  # No matching opening bracket
    
    return not open_b  # If the stack is empty, all brackets are matched