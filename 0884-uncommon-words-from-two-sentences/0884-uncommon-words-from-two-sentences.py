class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = (s1 + " " + s2).split()
        return [w for w in words if words.count(w) == 1] 