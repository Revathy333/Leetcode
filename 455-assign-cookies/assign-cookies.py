class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        i = 0
        j = 0
        n , m = len(g) , len(s)
        while i < n and j < m:
            if s[j] >= g[i]:
                i +=1
            j += 1    
        return i                  
