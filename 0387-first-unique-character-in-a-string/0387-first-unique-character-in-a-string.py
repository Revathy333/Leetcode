class Solution(object):
    def firstUniqChar(self, s):
        dict1 = {}
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1
        for ch in s:
            if dict1[ch] == 1:
                return s.index(ch)
        return -1        



        