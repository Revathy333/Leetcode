class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res = title.split(" ")
        for i in range(len(res)):
            if len(res[i]) < 3:
                res[i] = res[i].lower()
                continue
            res[i] = res[i].capitalize()
        return " ".join(res)    
        