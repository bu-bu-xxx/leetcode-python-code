# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 5791. 统计子岛屿
import collections
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 1:
                    grid1[i][j] = (i, j)
                if grid2[i][j] == 1:
                    grid2[i][j] = (i, j)

        # 并查集
        def find(grid, node: tuple) -> tuple:
            if grid[node[0]][node[1]] == node:
                return node
            grid[node[0]][node[1]] = find(grid, grid[node[0]][node[1]])
            return grid[node[0]][node[1]]

        def merge(grid, node1: tuple, node2: tuple):
            root1 = find(grid, grid[node1[0]][node1[1]])
            root2 = find(grid, grid[node2[0]][node2[1]])
            grid[root2[0]][root2[1]] = root1

        # 构造两个并查集
        for i in range(m):
            for j in range(n):
                if grid1[i][j] != 0:
                    if i - 1 >= 0 and grid1[i - 1][j] != 0:
                        merge(grid1, (i - 1, j), (i, j))
                    if j - 1 >= 0 and grid1[i][j - 1] != 0:
                        merge(grid1, (i, j - 1), (i, j))
                if grid2[i][j] != 0:
                    if i - 1 >= 0 and grid2[i - 1][j] != 0:
                        merge(grid2, (i - 1, j), (i, j))
                    if j - 1 >= 0 and grid2[i][j - 1] != 0:
                        merge(grid2, (i, j - 1), (i, j))

        # 存grid2的所有同源点，再搜索是否都在grid1同源
        count = collections.defaultdict(list)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] != 0:
                    count[find(grid2, (i, j))].append((i, j))

        for nodes in count.values():
            tag = True
            for nd in nodes:
                if grid1[nd[0]][nd[1]] == 0:
                    tag = False
                    break

            if tag:
                ct = collections.Counter()
                for nd in nodes:
                    ct[find(grid1, nd)] += 1
                if ct[find(grid1, nodes[0])] == len(nodes):
                    res += 1
        return res


if __name__ == "__main__":
    try1 = Solution()
    grid1 = [[1, 1, 1, 0, 0], [0, 1, 1, 1, 1], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [1, 1, 0, 1, 1]]
    grid2 = [
        [1, 1, 1, 0, 0], [0, 0, 1, 1, 1], [0, 1, 0, 0, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]]
    print(try1.countSubIslands(grid1, grid2))
