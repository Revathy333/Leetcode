class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            sec = target - nums[i]
            if  sec in dic:
                return [dic[sec],i]
            dic[nums[i]] = i    
        