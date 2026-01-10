class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum = 0
        for i in str(x):
            dig = int(i)
            sum+=dig
        return sum if x % sum == 0 else -1    
