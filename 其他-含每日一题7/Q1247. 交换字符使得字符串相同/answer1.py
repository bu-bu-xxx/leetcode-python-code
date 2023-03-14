# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做，数学
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x = 0
        y = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    x += 1
                else:
                    y += 1

        if (x + y) % 2 == 1:
            return -1
        if x % 2 == 1:
            return (x + y) // 2 + 1
        if x % 2 == 0:
            return (x + y) // 2
