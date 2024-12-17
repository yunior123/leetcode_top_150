def isValid(s):
    open_b = []
    dicts = {
        "(":")",
        "[":"]",
        "{":"}"
    }
    result = True
    for value in s:
        if value in ["(","[","{"]:
            open_b.append(value)
        elif open_b:
            last = open_b[-1]
            if value != dicts[last]:
                result = False
                break
        else:
            result = False
            break