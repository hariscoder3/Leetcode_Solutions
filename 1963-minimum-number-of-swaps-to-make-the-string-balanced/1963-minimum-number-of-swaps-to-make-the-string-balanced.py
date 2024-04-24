class Solution:
    def minSwaps(self, s: str) -> int:
        open_brackets = 0
        swaps = 0
        for ch in s:
            if ch == '[':
                open_brackets +=1
            elif ch==']':
                if open_brackets>0:
                    open_brackets-=1
                else:
                    swaps +=1
                    open_brackets+=1
        return swaps