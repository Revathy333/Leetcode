class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in nums:
            dict1[str(i)] = dict1.get(str(i),0)+1
        res = sorted(dict1, key=dict1.get)
        res = res[-k:]
        return [int(i) for i in res]

        