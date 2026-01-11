class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        arr = s.split(" ")
        for i in range(1,len(arr)+1):
            if arr[-i] == "":
                continue
            result+=(arr[-i]+" ")
        return result.strip()    


        