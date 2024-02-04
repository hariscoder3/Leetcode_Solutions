class Solution(object):
    def isPalindrome(self, x):
        original_num = x
        is_negative = False
        if x<0:
            x = abs(x)
        reverse_num = 0
        while(x!=0):
            last_digit = x%10
            reverse_num = reverse_num*10+last_digit
            x = x//10
        if is_negative:
            reverse_num = int(str(reverse_num)+"-");
        if original_num == reverse_num:
            return True
        else:
            return False