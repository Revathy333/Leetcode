class Solution:
    def reverseWords(self, s: str) -> str:
        li = s.split(" ")
        new = []
        for i in li:
            new.append(i[::-1]+" ")    
        return "".join(new).strip()


        