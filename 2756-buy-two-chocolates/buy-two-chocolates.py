class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        choco = 0
        prices.sort()
        org = money
        for i in prices:
            if i <= money:
                choco+=1
                money-=i
            if choco == 2:
                return money
        return org           
           



        
        