class Solution:
    def totalMoney(self, n: int) -> int:
        money = 0
        count = 0
        t = 0 
        for i in range(1,n+1):
            t+=1
            if (i-1) % 7 == 0 :
                count+=1
                t=count
                money+=t
            else:                                                       
                money+=t
        return money        
            
