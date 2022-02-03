# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做
# Q12.整数转罗马数字，反过来就是
# 从右往左遍历，碰到等于或更大的数加上，小的数减去

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        val = roman_dict[s[-1]]
        prev = s[-1]
        for i in s[-2::-1]:
            if roman_dict[i] >= roman_dict[prev]:
                val += roman_dict[i]
            else:
                val -= roman_dict[i]
            prev = i
        return val
