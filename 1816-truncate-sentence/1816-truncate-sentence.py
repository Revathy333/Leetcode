class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        arr = s.split(" ")
        new = ""
        k = len(arr) if k > len(arr) else k 
        for i in range(k):
            new+=arr[i]+" "
        return new.strip()    


        