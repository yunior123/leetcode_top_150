class Solution:
    def isHappy(self, n: int) -> bool:
        
       
        seen = set()
        

        while n != 1:
  
            if n in seen:
                return False
           
            seen.add(n)
           
            n = self.get_next(n)
        
      
        return True
    
    def get_next(self, n):
        total_sum = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total_sum += digit ** 2
        return total_sum