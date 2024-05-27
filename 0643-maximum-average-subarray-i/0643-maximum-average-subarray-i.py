class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s = sum(nums[:k])
        max_avg = s/k
        for i in range(len(nums)-k):
            s = s-nums[i]
            s = s+nums[k+i]
            max_avg = max(max_avg,s/k)
        return max_avg