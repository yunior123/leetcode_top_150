# For s = "We expect the %f%% growth this week", the output should be
# solution(s) = "We expect the {}% growth this week".
# pattern to substitute %f% where f is any character

def solution(s):
    newString = ''
    i = 0
    while i < len(s):
        if s[i] == '%' and s[i+1] != '%' and s[i+2] == '%':
            newString += '{}'
            i += 3
        else:
            newString += s[i]
            i += 1
    return newString



# Test cases

s = solution("We expect the %f%% growth this week")
assert  s == "We expect the {}% growth this week", f"Wrong answer: {solution('We expect the %f%% growth this week')}"