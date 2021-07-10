# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，投机取巧
# 正确率低的离谱的一道题
import re


class Solution:
    def isNumber(self, s: str) -> bool:
        if len(res1 := re.findall(r'([A-Za-z])', s)) == 1 and \
                (res1[0] == 'e' or res1[0] == 'E'):
            res2 = re.findall(r'([^a-zA-Z]*)', s)
            try:
                a = float(res2[0])
                b = int(res2[2])
            except:
                return False
            else:
                return True
        elif len(res1) == 0:
            try:
                a = float(s)
            except:
                return False
            else:
                return True
        return False


if __name__ == "__main__":
    try1 = Solution()
    s1 = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10",
          "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]
    print(try1.isNumber(s1[-1]))
    for s2 in s1:
        print(try1.isNumber(s2))
