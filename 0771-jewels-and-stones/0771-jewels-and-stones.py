class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for j in jewels:
            c1 = stones.count(j)
            count+=c1

        return count            

        