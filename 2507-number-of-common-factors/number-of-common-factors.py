class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        x = min(a,b)
        for i in range(1,x+1):
            if a % i == 0 and b % i == 0:
                count+=1
        return count        
        