# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，广度优先搜索+哈希表
# 用(当前的点,所有点的遍历情况)为搜索目标
import collections
from typing import List


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        mem = set()
        n = len(graph)
        queue = collections.deque([(i, 2 ** i) for i in range(n)])
        mem |= set(queue)
        res = 0

        while 1:
            for _ in range(len(queue)):
                tmp = queue.popleft()
                if tmp[1] == 2 ** n - 1:
                    return res

                for nex in graph[tmp[0]]:
                    if (tmp_nex := (nex, tmp[1] | 2 ** nex)) not in mem:
                        mem.add(tmp_nex)
                        queue.append(tmp_nex)

            res += 1


if __name__ == "__main__":
    try1 = Solution()
    graph1 = [[1, 2, 3], [0], [0], [0]]
    print(try1.shortestPathLength(graph1))
