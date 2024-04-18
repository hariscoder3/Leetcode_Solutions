class Solution(object):
    def findDisappearedNumbers(self, nums):
        updated = set(nums)
        disappered_nums = []
        for i in range(1,len(nums)+1):
            if i not in updated:
                disappered_nums.append(i)
        return disappered_nums