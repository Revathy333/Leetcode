class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        snum = set(nums)
        if (len(nums) == len(snum)) and (nums[0]+nums[1] > nums[2]):
            return "scalene"
        elif len(nums) != 3 or (nums[0]+nums[1] <= nums[2]):
            return "none"    
        elif  len(nums) == 3 and  len(snum) == 2:
            return "isosceles"
        else:
            return "equilateral"       


                
