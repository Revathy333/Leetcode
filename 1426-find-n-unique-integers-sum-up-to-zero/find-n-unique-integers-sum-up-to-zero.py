import random
class Solution:
    def sumZero(self, n: int) -> List[int]:
        li = []
        for i in range(1,n//2 + 1):
            li.extend([i,-i])
        if n % 2 == 1:
            li.append(0)
        return li       
        