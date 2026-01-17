class Solution:
    def frequencySort(self, s: str) -> str:
        dict1 = {}
        s1  = ""
        for ch in s:
            dict1[ch] = dict1.get(ch,0) + 1
        d = dict(sorted(dict1.items(),key=lambda x:x[1],reverse=True))
        for k,v in d.items():
            for i in range(v):
                s1+=k
        return s1


        