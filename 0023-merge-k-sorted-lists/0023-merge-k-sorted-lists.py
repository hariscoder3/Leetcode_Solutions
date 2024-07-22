# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        array = []
        for List in lists:
            x = List
            while x:
                array.append(x.val)
                x = x.next
        array = sorted(array,reverse=True)
        ans = None
        for x in array:
            ans = ListNode(x,ans)
        return ans