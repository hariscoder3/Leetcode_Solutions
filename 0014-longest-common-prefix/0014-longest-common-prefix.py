class Solution(object):
    def longestCommonPrefix(self, strs):
        common_str = strs[0];
        check_st = ""
        for st in strs[1:]:
            min_len_str = min(len(common_str),len(st))
            for i in range(min_len_str):
                if common_str[i] == st[i]:
                    check_st = check_st + st[i]
                else:
                    break;
            common_str = check_st
            check_st = ""
        return common_str;