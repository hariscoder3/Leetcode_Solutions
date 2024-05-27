# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        new_list = []
        curr = head
        while curr:
            new_list.append(curr.val)
            curr = curr.next
        
        # get values of Link list in a new_list
        i,j = 0,len(new_list)-1
        max_sum = 0
        while i<=j:
            max_sum = max(max_sum, new_list[i]+new_list[j])
            i+=1
            j-=1
        return max_sum