# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，广度优先搜索
# 标记0为未搜索，1为A集合，-1为B集合
# 然后搜索完全部点，标记
import collections
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        tag = [0] * n
        belong = 1
        queue = collections.deque()

        # 输入初始的bfs的点
        def bfs(node) -> bool:
            nonlocal belong
            tag[node] = belong
            queue.append(node)
            while queue:
                belong *= -1
                for _ in range(len(queue)):
                    now = queue.popleft()
                    for nex in graph[now]:
                        if tag[nex] == 0:
                            tag[nex] = belong
                            queue.append(nex)
                        elif tag[nex] != belong:
                            return False
            return True

        # 查询所有点
        for i, val in enumerate(tag):
            if val == 0 and bfs(i) is False:
                return False
        return True


if __name__ == "__main__":
    try1 = Solution()
    graph1 = [[1, 3], [0, 2], [1, 3], [0, 2]]
    print(try1.isBipartite(graph1))
