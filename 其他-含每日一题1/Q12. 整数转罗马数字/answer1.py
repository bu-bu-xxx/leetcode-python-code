# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，定义规则
# 这题关键就是看谁规则定义的好，其实能做出来就行
# 罗马数字是把num每个位置上的数字分别转换，再叠加起来
# 可以定义好这种规则，并且存储好0-9对应的罗马数字

class Solution:
    def intToRoman(self, num: int) -> str:
        Rome_num = [('I', 'V', 'X'), ('X', 'L', 'C'), ('C', 'D', 'M'), ('M', None, None)]
        rule = {
            '0': lambda s: '',
            '1': lambda s: s[0] * 1,
            '2': lambda s: s[0] * 2,
            '3': lambda s: s[0] * 3,
            '4': lambda s: s[0] + s[1],
            '5': lambda s: s[1],
            '6': lambda s: s[1] + s[0] * 1,
            '7': lambda s: s[1] + s[0] * 2,
            '8': lambda s: s[1] + s[0] * 3,
            '9': lambda s: s[0] + s[2],
        }
        # 从个位开始遍历num
        result = ''
        for i, n in enumerate(reversed(str(num))):
            result = rule[n](Rome_num[i]) + result
        return result
