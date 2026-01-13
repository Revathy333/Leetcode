class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        for x in strs:
            key = "".join(sorted(x))
            if key not in dict1:
                dict1[key] = []
            dict1[key].append(x)
        return list(dict1.values())  

 




        