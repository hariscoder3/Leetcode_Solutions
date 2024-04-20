class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)-1
        for j in range(n):
            for i in range(n):
                if nums[i]>nums[i+1]:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
            
        