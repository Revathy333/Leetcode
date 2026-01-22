class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        lst = list(s)
        i, j = 0, len(lst)-1

        while i < j:
            if lst[i] not in vowels:
                i += 1
            elif lst[j] not in vowels:
                j -= 1
            else:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1

        return "".join(lst)
        