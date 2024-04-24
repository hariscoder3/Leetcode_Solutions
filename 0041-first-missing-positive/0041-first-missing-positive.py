class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        miss_num = 1
        while miss_num in nums:
            miss_num+=1
        return miss_num