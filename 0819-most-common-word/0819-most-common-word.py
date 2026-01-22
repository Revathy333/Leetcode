class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        words = paragraph.lower().split()

        for w in sorted(set(words), key=words.count, reverse=True):
            if w not in banned:
                return w