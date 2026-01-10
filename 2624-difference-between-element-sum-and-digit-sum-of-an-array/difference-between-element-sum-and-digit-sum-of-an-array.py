class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        single = list(map(int, "".join(map(str, nums))))
        sum1 = 0 
        sum2 = 0 
        for n1 in nums:
            sum1+=n1
        for n2 in single:
            sum2+=n2
        return abs(sum1 - sum2)         

      