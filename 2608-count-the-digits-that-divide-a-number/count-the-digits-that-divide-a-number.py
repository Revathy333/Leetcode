class Solution:
    def countDigits(self, num: int) -> int:
        res = 0 
        for n in str(num):
            digit = int(n)
            if num % digit == 0:
                res+=1
        return res        

            
        