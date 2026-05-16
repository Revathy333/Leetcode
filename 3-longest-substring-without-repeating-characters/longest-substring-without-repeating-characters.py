class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        str1 = ""
        li = []
        for i in s:
            while i in str1:
                    str1 = str1[1:]
            str1+=i
            li.append(str1)       
        return len((max(li,key=len)))      


        