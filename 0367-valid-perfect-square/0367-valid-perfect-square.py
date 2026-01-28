class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        s = int(num ** 0.5)
        return True if s*s == num else False   
        