class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        for i in accounts:
            sm = sum(i)
            if sm > result:
                result = sm
        return result        
        