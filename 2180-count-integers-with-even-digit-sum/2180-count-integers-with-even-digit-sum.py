class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(2,num+1):
                temp = i
                s = 0
                while temp > 0:
                    dig = temp % 10
                    temp //= 10
                    s += dig
                if s % 2 == 0:
                    count+=1

        return count            

                    