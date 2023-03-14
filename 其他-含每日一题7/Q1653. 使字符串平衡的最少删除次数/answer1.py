# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做，简单
class Solution:
    def minimumDeletions(self, s: str) -> int:
        left = [0] * len(s)
        right = [0] * len(s)

        tmp = 0
        for i in range(len(s)):
            left[i] = tmp
            if s[i] == "b":
                tmp += 1

        tmp = 0
        for i in range(len(s) - 1, -1, -1):
            right[i] = tmp + left[i]
            if s[i] == "a":
                tmp += 1

        return min(right)
