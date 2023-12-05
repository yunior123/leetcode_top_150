class Solution:
    #Given two binary strings a and b, return their sum as a binary string. Input: a = "1010", b = "1011" Output: "10101"
    def addBinary(self, a: str, b: str) -> str:
        #Convert the binary strings to integers
        a = int(a,2)
        b = int(b,2)
        #Add the integers
        c = a + b
        #Convert the sum to a binary string
        c = bin(c)
        #Remove the '0b' from the beginning of the string
        c = c[2:]
        return c
        