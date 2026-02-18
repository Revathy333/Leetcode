class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for i,ch in enumerate(s):
            rev = 26 - (ord(ch) - 97)
            total+=rev*(i+1)

        return total    
        