class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        s1 = sorted(heights)
        for i in range(len(s1)):
            if s1[i] != heights[i]:
                count+=1
        return count        
        