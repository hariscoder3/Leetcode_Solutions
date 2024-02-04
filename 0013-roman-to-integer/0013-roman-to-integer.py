class Solution(object):
    def romanToInt(self, s):
        integer_value = 0
        
        reverse_str = s[::-1]
        i = 0;
        
        for char in reverse_str:
            if char == "I":
                integer_value = integer_value+1;
            elif char == "V"  and (i+1)<len(reverse_str) and reverse_str[i+1]=="I":
                integer_value = (integer_value+5)-2;
            elif char == "X"  and (i+1)<len(reverse_str) and reverse_str[i+1]=="I":
                integer_value = (integer_value+10)-2;
            elif char == "L"  and (i+1)<len(reverse_str) and reverse_str[i+1]=="X":
                integer_value = (integer_value+50)-20;
            elif char == "C"  and (i+1)<len(reverse_str) and reverse_str[i+1]=="X":
                integer_value = (integer_value+100)-20;
            elif char == "D"  and (i+1)<len(reverse_str) and reverse_str[i+1]=="C":
                integer_value = (integer_value+500)-200;
            elif char == "M"  and (i+1)<len(reverse_str) and reverse_str[i+1]=="C":
                integer_value = (integer_value+1000)-200;
            elif char == "V":
                integer_value = integer_value+5;
            elif char == "X":
                integer_value = integer_value+10;
            elif char == "L":
                integer_value = integer_value+50;
            elif char == "C":
                integer_value = integer_value+100;
            elif char == "D":
                integer_value = integer_value+500;
            elif char == "M":
                integer_value = integer_value+1000;
            i=i+1;
        return integer_value;