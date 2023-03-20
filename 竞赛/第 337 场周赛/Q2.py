# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 6322. 检查骑士巡视方案
from typing import List


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        if grid[0][0] != 0:
            return False
        rec = dict()
        n = len(grid)
        for i in range(n):
            for j in range(n):
                rec[grid[i][j]] = (i, j)

        pre = rec[0]
        for num in range(1, n * n):
            now = rec[num]
            a = abs(now[0] - pre[0])
            b = abs(now[1] - pre[1])
            if (a == 2 and b == 1) or (a == 1 and b == 2):
                pre = now
                continue
            else:
                return False
        return True
