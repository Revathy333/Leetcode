class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        let = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        new = [""]
        for i in digits:
            temp = []
            for old in  new:
                for j  in let[i]:
                    temp.append(old+j)
            new = temp        
        return new            
