class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        non_repeat_list = set()
        for num in nums:
            if num in non_repeat_list:
                return num
            else:
                non_repeat_list.add(num)