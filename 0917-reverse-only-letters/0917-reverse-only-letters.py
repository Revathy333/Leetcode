class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left = 0
        right = len(s)-1
        res = list(s)
        while left < right:
            if res[left].isalpha() and res[right].isalpha():
                res[left] , res[right] = res[right] , res[left]
                left+=1
                right-=1
            elif res[left].isalpha():
                right-=1  
            elif res[right].isalpha():
                left+=1     
            else:
                left+=1
                right-=1     
        return "".join(res)        

