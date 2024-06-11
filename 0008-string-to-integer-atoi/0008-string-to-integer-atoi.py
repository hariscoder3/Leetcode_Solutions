class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s)==0:
            return 0
        
        sign = 1
        if s[0] == "-" or s[0]=="+":
            if s[0]=="-":
                sign = -1
            else:
                sign=1
            s = s[1:]

        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result*10 + int(char)
        
        result *= sign;
        result = max(min(result,2**31 - 1),-2**31)
        return result