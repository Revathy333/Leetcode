class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mp = {c: chr(97+i) for i,c in enumerate(dict.fromkeys(key.replace(" ","")))}
        return "".join(mp.get(c, c) for c in message)