# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，并查集
# 先排序按边权值从低到高
# 按边依次合并，当最终点和起点同源时，返回当前权值

# 另一种方法：
# 用二分法设定最大权值
# 每次把小于该权值的边进行并查集合并，最后查看终点和起点是否同源
# 此方法不写代码
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]):
        edges = []
        m, n = len(heights), len(heights[0])
        state = [[(i, j) for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    edges.append((abs(heights[i - 1][j] - heights[i][j]), (i - 1, j), (i, j)))
                if j - 1 >= 0:
                    edges.append((abs(heights[i][j - 1] - heights[i][j]), (i, j - 1), (i, j)))
        edges = sorted(edges)

        def find(i0: int, j0: int) -> tuple:
            if state[i0][j0] == (i0, j0):
                return i0, j0
            state[i0][j0] = find(state[i0][j0][0], state[i0][j0][1])
            return state[i0][j0]

        def merge(i1: int, j1: int, i2: int, j2: int):
            root1 = find(i1, j1)
            root2 = find(i2, j2)
            state[root2[0]][root2[1]] = root1

        for edge in edges:
            merge(edge[1][0], edge[1][1], edge[2][0], edge[2][1])
            if find(m - 1, n - 1) == find(0, 0):
                return edge[0]

        return 0
