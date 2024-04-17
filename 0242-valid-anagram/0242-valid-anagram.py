class Solution(object):
    def isAnagram(self, s, t):
        for i in s:
            if i in t:
                t = t.replace(i,'',1)
            else:
                return False
        
        return len(t)==0
        