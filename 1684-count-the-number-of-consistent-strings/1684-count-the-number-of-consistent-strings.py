class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for w in words:
            for wi in w:
                if wi not in allowed:
                    count+=1
                    break
        return len(words)-count        
