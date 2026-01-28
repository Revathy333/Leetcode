class Solution:
    def isPalindrome(self, x: int) -> bool:
        # while temp > 0:
        #     dig = temp % 10
        #     temp //= 10
        #     rev+=str(dig)
        # if rev == str(x) or x < 10:
        #     return True
        # elif x > -10 or rev != str(x):     
        #     return False  
        st = str(x) 
        return True if st[::-1] == str(x) else False           
        