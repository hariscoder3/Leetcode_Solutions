def comb(nums,target,List,ans):
    if target == 0:
        ans.sort()
        if(ans in List):
            return
        List.append(ans)
        return
    for num in nums:
        if num>target:
            continue
        l = ans.copy()
        l.append(num)
        comb(nums,target-num,List,l)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        List = []
        ans = []
        comb(candidates,target,List,ans)
        return List