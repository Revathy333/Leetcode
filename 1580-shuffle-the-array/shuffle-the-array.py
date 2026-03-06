class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n1 = nums[n:]
        res = []
        for i in range(n):
            res.extend([nums[i],n1[i]])
        return res    
        