class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ind = []
        count = -1
        for w in words:
            count+=1
            if x in w:
                ind.append(count)
        return ind        