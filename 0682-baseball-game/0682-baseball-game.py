class Solution:
    def calPoints(self, operations: List[str]) -> int:
        li = []
        for i in operations:
            if i == "D" and len(li) > 0:
                li.append(int(li[-1])*2)
            elif i == "+" and len(li) >= 2:
                s = int(li[-1])+int(li[-2])
                li.append(s)
            elif i == "C" and len(li)!= 0:
                li.pop()        
            elif not i.isalpha() and i != '+':
                num = int(i)
                li.append(i) 
                    
        return sum(list(map(int,li)))                     
        