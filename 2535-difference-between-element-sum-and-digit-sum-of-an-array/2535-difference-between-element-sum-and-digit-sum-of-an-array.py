class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        sum2 = sum(int(r) for d in nums for r in str(d))    
        return abs(sum2-sum1)
          

      