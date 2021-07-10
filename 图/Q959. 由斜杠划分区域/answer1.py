# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 评论区解答，并查集
# 把每个方块的四个顶点作为目标，n行n列方格有(n+1)^2个顶点
# 初始设定四条边上的点同源，其他点不同源
# 每次斜杠连接的两个点如果同源，则多分出一个区域
from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        root_graph = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            for j in range(n + 1):
                root_graph[i][j] = (i, j)

        def find(node: tuple) -> tuple:
            if root_graph[node[0]][node[1]] == node:
                return node
            root_graph[node[0]][node[1]] = find(root_graph[node[0]][node[1]])
            return root_graph[node[0]][node[1]]

        def merge(node1: tuple, node2: tuple) -> bool:
            # 返回是否同源
            root2, root1 = find(node2), find(node1)
            if root2 == root1:
                return True
            root_graph[root2[0]][root2[1]] = root1
            return False

        # 初始化并查集
        for i in range(n + 1):
            root_graph[i][0] = (0, 0)
            root_graph[i][n] = (0, 0)
            root_graph[0][i] = (0, 0)
            root_graph[n][i] = (0, 0)

        # 正式开始遍历斜杠
        res = 1
        for i, edges in enumerate(grid):
            for j, edge in enumerate(edges):
                if edge == "\\":
                    if merge((i, j), (i + 1, j + 1)):
                        res += 1
                elif edge == "/":
                    if merge((i + 1, j), (i, j + 1)):
                        res += 1
        return res


if __name__ == "__main__":
    try1 = Solution()
    grid1 = [
        " /",
        "/ "
    ]
    print(try1.regionsBySlashes(grid1))
