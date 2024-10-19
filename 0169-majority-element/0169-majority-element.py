class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        result = 0
        max_count = 0
        
        for n in nums:
            count[n] = 1+count.get(n,0)
            result = n if count[n]>max_count else result
            max_count = max(count[n],max_count)
        return result