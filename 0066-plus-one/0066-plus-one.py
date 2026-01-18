class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st = "".join(map(str,digits))
        last = int(st) + 1
        return list(map(int,str(last)))    
        