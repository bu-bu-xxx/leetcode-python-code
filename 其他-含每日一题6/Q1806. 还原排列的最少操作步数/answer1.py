# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 暴力尝试
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm = [i for i in range(n)]
        arr = list(range(n))

        for i in range(1, n):
            arr = arr[0::2] + arr[1::2]
            if arr == perm:
                return i
