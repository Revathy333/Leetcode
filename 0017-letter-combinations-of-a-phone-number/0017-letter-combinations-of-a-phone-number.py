class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        let = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        res = [""]
        for i in digits:
            temp = []
            for old in res:
                for v in let[i]:
                    temp.append(old+v)
            res = temp        
        return res      