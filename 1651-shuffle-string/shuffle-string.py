class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ""
        s = zip(indices,s)
        sort_s = sorted(s)
        for k,v in sort_s:
            res+=v
        return res    
      
        