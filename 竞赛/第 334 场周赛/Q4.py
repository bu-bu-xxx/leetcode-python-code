# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 2577. 在网格图中访问一个格子的最少时间
# https://leetcode.cn/problems/minimum-time-to-visit-a-cell-in-a-grid/solution/er-fen-da-an-bfspythonjavacgo-by-endless-j10w/
# Dijkstra算法，每个点到的时间设为dis，relax计算dis需要考虑路程和grid的值，取最小
import heapq
from typing import List


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        dis = [[10 ** 6] * n for _ in range(m)]
        dis[0][0] = 0
        node = set()
        heap = [(0, 0, 0)]  # (time,i,j)

        while heap:
            time, i, j = heapq.heappop(heap)
            node.add((i, j))
            if (i, j) == (m - 1, n - 1):
                return time
            for i_add, j_add in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                i_nex, j_nex = i + i_add, j + j_add
                if 0 <= i_nex < m and 0 <= j_nex < n and (i_nex, j_nex) not in node:
                    tmp = max(dis[i][j] + 1, grid[i_nex][j_nex] \
                        if grid[i_nex][j_nex] % 2 == (i_nex + j_nex) % 2 \
                        else grid[i_nex][j_nex] + 1)
                    if dis[i_nex][j_nex] > tmp:
                        dis[i_nex][j_nex] = tmp
                        heapq.heappush(heap, (tmp, i_nex, j_nex))


if __name__ == "__main__":
    try1 = Solution()
    grid = [[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]]
    print(try1.minimumTime(grid))
