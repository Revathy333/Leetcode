class Solution:
    def isPalindrome(self, x: int) -> bool: 
        st = str(x) 
        return True if st[::-1] == str(x) else False           
        