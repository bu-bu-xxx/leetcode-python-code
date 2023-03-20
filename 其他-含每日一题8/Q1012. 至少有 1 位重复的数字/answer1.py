# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 分类讨论，有点繁琐
from typing import List


class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        def count_with0(n_len, picks):
            tmp = 1
            for a in range(10 - picks, 10 - picks - n_len, -1):
                tmp *= a
            return tmp

        def count_without0(n_len, picks):
            tmp = 1
            for a in range(10 - picks, 10 - picks - n_len, -1):
                if a == 10 - picks:
                    tmp *= 10 - picks - 1
                else:
                    tmp *= a
            return tmp

        n_str = list(str(n))

        def dfs(pre: List[int], idx: int):
            if idx >= len(n_str):
                return 1
            ret = 0
            val = int(n_str[idx])
            for i in range(val):
                if i not in pre:
                    ret += count_with0(len(n_str) - idx - 1, len(pre) + 1)
            if val not in pre:
                pre.append(val)
                ret += dfs(pre, idx + 1)
            return ret

        res = 0
        val0 = int(n_str[0])
        for i in range(val0 + 1):
            if i == 0:
                for j in range(1, len(n_str)):
                    res += count_without0(j, 0)
            elif i == val0:
                res += dfs([val0], 1)
            else:
                res += count_with0(len(n_str) - 1, 1)

        return n - res


if __name__ == "__main__":
    try1 = Solution()
    n = 20
    print(try1.numDupDigitsAtMostN(n))
