class Solution:
    def findGCD(self, nums: List[int]) -> int:
        sm = min(nums)
        big = max(nums)
        for i in range(1,min(nums)+1):
            if min(nums) % sm == 0 and big % sm == 0:
                return sm  
            sm-=1     
        