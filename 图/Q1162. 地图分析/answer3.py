# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，单元最短路径
# 添加一个源节点，源节点到陆地路径为0
# 则源节点到海洋节点的距离是最短到陆地距离
# 用Dijkstra算法
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> float:
        n = len(grid)
        # 没找到最短路径的点
        S = {(i, j) for i in range(n) for j in range(n)}
        # 最短路径
        D = [[float('inf')] * n for _ in range(n)]

        # 连接的边，不包括源节点
        def adj(i, j):
            tmp = []
            if i - 1 >= 0:
                tmp.append([i - 1, j])
            if j - 1 >= 0:
                tmp.append([i, j - 1])
            if i + 1 < n:
                tmp.append([i + 1, j])
            if j + 1 < n:
                tmp.append([i, j + 1])
            return tmp

        # relax
        def relax(ui, uj, vi, vj):
            D[vi][vj] = min(D[vi][vj], D[ui][uj] + 1)

        # main
        # 源节点
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    D[i][j] = 0
        # 其他节点
        while S:
            ui, uj = min(S, key=lambda s: D[s[0]][s[1]])
            S -= {(ui, uj)}
            for vi, vj in adj(ui, uj):
                relax(ui, uj, vi, vj)

        res = max(sum(D, []))
        if res == 0 or res == float('inf'):
            return -1
        return res


if __name__ == '__main__':
    try1 = Solution()
    grid1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(try1.maxDistance(grid1))
