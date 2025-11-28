class Solution(object):
    def longestCommonPrefix(self, strs):
        pre = ""

        for i in range(len(strs[0])):
            char = strs[0][i]

            for wor in strs:
                if i >= len(wor) or wor[i] != char:
                    return pre

            pre += char
        return pre     
