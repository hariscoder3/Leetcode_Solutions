class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowels = 0
        count = 0
        for i,char in enumerate(s):
            if char in "aeiou":
                count+=1
            if i-k>=0 and s[i-k] in "aeiou":
                count-=1
            max_vowels = max(max_vowels,count)
        return max_vowels
        