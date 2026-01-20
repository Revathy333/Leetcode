class Solution:
    def sortSentence(self, s: str) -> str:
        li = s.split(" ")
        res = [""]*len(li)
        print(li)
        for w in li:
            res[int(w[-1])-1] = w[:-1]
        return " ".join(res)  
              