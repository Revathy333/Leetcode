class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                result+=ch.lower()
        return True if result[::-1] == result else False        

