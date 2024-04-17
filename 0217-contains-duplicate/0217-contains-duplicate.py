class Solution(object):
    def containsDuplicate(self, nums): 
        mydict = {}
        for i in nums:
            if i in mydict:
                return True
            mydict[i] = True
        return False