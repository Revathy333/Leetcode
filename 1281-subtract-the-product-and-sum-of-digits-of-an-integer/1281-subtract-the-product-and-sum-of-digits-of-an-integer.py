from math import prod
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        return prod(list(map(int,str(n)))) - sum(map(int,list(str(n))))
        