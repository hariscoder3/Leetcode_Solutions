class Solution(object):
    def isPerfectSquare(self, num):
        left = 1
        right = num
        while left<=right:
            mid = (left+right)//2
            if mid**2 == num:
                return True
            elif mid**2<num:
                left = mid+1
            else:
                right = mid-1
        return False