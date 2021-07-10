# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 正式开始做题，读了好久这几个方法
# 很巧妙，但是并不能显然看出正确性，证明也略有难度

# 自己做，暴力尝试
# 每个海洋点都找曼哈顿距离为1，2，3，···的距离，找到陆地即返回，有点像贪心算法
# 最后返回每个海洋点最大的最小距离
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        Distance = lambda x1, y1, x2, y2: abs(x1 - x2) + abs(y1 - y2)

        # 找曼哈顿距离为d的点集
        def find(x: int, y: int, d: int) -> List[List[int]]:
            dx = list(range(0, d + 1))
            dy = list(range(d, -1, -1))
            tmp = []
            for i in range(d + 1):
                if 0 <= (x - dx[i]) <= n - 1 and 0 <= (y - dy[i]) <= n - 1:
                    tmp.append([x - dx[i], y - dy[i]])
                if 0 <= (x - dx[i]) <= n - 1 and 0 <= (y + dy[i]) <= n - 1:
                    tmp.append([x - dx[i], y + dy[i]])
                if 0 <= (x + dx[i]) <= n - 1 and 0 <= (y - dy[i]) <= n - 1:
                    tmp.append([x + dx[i], y - dy[i]])
                if 0 <= (x + dx[i]) <= n - 1 and 0 <= (y + dy[i]) <= n - 1:
                    tmp.append([x + dx[i], y + dy[i]])
            return tmp

        res = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    flag = 0
                    for d in range(1, 2 * n - 1):
                        for [i1, j1] in find(i, j, d):
                            if grid[i1][j1] == 1:
                                res = max(res, d)
                                flag = 1
                                break
                        if flag == 1:
                            break
        return res
