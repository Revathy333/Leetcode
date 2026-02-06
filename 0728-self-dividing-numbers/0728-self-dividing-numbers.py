class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left,right+1):
            count = 0
            if '0' in str(i): 
                continue
            for d in str(i):
                if i % int(d) == 0:
                    count+=1
            if count == len(str(i)):
                res.append(i)        
        return res