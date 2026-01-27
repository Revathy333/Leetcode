class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(1,10):
            if (n*i) % 2 == 0:
                return n*i
               
                
        