# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，比answer1更投机取巧


class Solution:
    def isNumber(self, s: str) -> bool:

        try:
            a = float(s)
        except:
            return False
        else:
            no = ["Infinity", "-Infinity", "+Infinity",
                  'inf', '-inf', '+inf']
            if s in no:
                return False
            return True
