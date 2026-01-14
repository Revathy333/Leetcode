class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        arr1  = []
        arr2 = []
        for x in nums:
            if x > 0 and x < 10:
                arr1.append(x)
            else:
                arr2.append(x)
        return False if sum(arr1) == sum(arr2) else True        

        