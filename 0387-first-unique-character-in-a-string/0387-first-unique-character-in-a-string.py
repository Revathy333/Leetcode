class Solution(object):
    def firstUniqChar(self, s):
        dict1 = {}
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1
        for ch in range(len(s)):
            if dict1[s[ch]] == 1:
                return ch
        return -1        



        