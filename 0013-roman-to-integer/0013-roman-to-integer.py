class Solution:
    def romanToInt(self, s: str) -> int:
        hash_map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        summ = 0
        for num in range(len(s)):
            if num<(len(s)-1) and hash_map[s[num]]<hash_map[s[num+1]]:
                summ -= hash_map[s[num]]
            else:
                summ+=hash_map[s[num]]
                
        return summ;