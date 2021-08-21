# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，数学
# 满足"a1b"<=n 的最大"ab"，则该位置1出现"ab"+1次


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n == 0:
            return 0
        if 1 <= n <= 9:
            return 1

        n = str(n)
        res = 0
        for i in range(len(n)):
            beg, end = n[0:i], n[i + 1:]
            if n[i] == "0":
                res += (int(beg)) * (10 ** len(end))
            elif n[i] == "1":
                res += int(beg + end) + 1
            else:
                if beg == "":
                    beg = "0"
                res += (int(beg) + 1) * (10 ** len(end))

        return res
