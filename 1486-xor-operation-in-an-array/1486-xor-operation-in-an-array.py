class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        result = 0
        for i in range(0 , n):
            s1 = start+(2*i)
            if i == 0:
                result = start ^ s1  
            nums.append(s1)
            result = result ^ s1
        return  result   

        