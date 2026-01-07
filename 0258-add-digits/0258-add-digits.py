class Solution(object):
    def addDigits(self, num):
        if num < 10:
            return num 
        else:    
            total=0
            while num > 0:
                r = num % 10
                total += r
                num = num // 10
            return self.addDigits(total)   

        