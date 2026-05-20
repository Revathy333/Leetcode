class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[:k])
        avg = sums / k 
        for i in range(k,len(nums)):
            sums+=nums[i]
            sums-=nums[i-k]
            avg = max(avg, sums/k)
        return avg    

        