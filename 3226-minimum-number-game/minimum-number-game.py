class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        while len(nums) > 0:
            ali = nums.pop(nums.index(min(nums)))
            bob = nums.pop(nums.index(min(nums)))
            arr.extend([bob,ali])
        return arr    


