class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        d = 0
        for n in nums:
            while n:
                d += n% 10
                n //= 10
        return abs(sum1 - d)  

      