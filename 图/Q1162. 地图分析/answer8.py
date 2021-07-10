# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 非官方答案，BFS
# 多源最短路径转化为单源最短路径
# 1.把所有陆地入队列，最短路径D值改为0
# 2.1.每次更新当前距离，并出所有队列的点
# 2.2.每次出队列的点，然后搜索四周的点，如果没有值，则D存入当前距离，并入队列
# 3.如果队列不为空则重复2，空则结束
import collections
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        D = [[None] * n for _ in range(n)]
        queue = collections.deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    D[i][j] = 0
                    queue.append([i, j])

        def nex(ui, uj) -> List[List[int]]:
            nex_node = []
            if ui - 1 >= 0:
                nex_node.append([ui - 1, uj])
            if uj - 1 >= 0:
                nex_node.append([ui, uj - 1])
            if ui + 1 < n:
                nex_node.append([ui + 1, uj])
            if uj + 1 < n:
                nex_node.append([ui, uj + 1])
            return nex_node

        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                tmp = queue.popleft()
                for nex_i, nex_j in nex(tmp[0], tmp[1]):
                    if D[nex_i][nex_j] is None:
                        D[nex_i][nex_j] = step
                        queue.append([nex_i, nex_j])

        try:
            res = max(sum(D, []))
            if res == 0:
                return -1
            return res
        except:
            return -1
