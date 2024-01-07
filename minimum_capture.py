

class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if a == e:
            if c != a: return 1
            if not b < d < f and not f < d < b: return 1
        if b == f:
            if d != b: return 1
            if not a < c < e and not e < c < a: return 1
        
        dx, dy = e - c, f - d
        if abs(dx) != abs(dy): return 2
        dx //= abs(dx)
        dy //= abs(dy)
        
        x, y = c, d
        while (x, y) != (e, f):
            x += dx
            y += dy
            if (x, y) == (a, b): return 2
        return 1
    


   
    
# test
s = Solution()
a = 1 
b = 1
c = 8
d = 8
e = 2
f = 3
print(s.minMovesToCaptureTheQueen(a, b, c, d, e, f)) # 2
a = 5
b = 3
c = 3
d = 4
e = 5
f = 2
print(s.minMovesToCaptureTheQueen(a, b, c, d, e, f)) # 1
a = 4
b = 3
c = 3
d = 4
e = 2
f = 5
print(s.minMovesToCaptureTheQueen(a, b, c, d, e, f)) # 1
a = 4
b = 3
c = 3
d = 4
e = 5
f = 2
print(s.minMovesToCaptureTheQueen(a, b, c, d, e, f)) # 2