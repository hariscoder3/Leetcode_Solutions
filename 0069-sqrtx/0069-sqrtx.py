class Solution(object):
    def mySqrt(self, x):
        left = 1
        right = x
        while left<=right:
            mid = (left+right)//2
            if mid**2 == x:
                return mid
            elif mid**2<x:
                left = mid+1
            else:
                right = mid-1
        return right
        