# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，深度优先搜索，回溯算法
import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(collections.Counter)
        for fm, to in tickets:
            graph[fm][to] += 1

        res = []
        tag = False

        def dfs(now, num):
            nonlocal tag
            res.append(now)
            if num == len(tickets):
                tag = True
                return
            for nex in sorted(graph[now].keys()):
                if graph[now][nex] > 0:
                    graph[now][nex] -= 1
                    dfs(nex, num + 1)
                    if tag:
                        return
                    graph[now][nex] += 1
            res.pop()

        dfs('JFK', 0)
        return res


if __name__ == "__main__":
    try1 = Solution()
    tickets1 = [["A", "B"], ["JFK", "A"], ["B", "JFK"], ["A", "C"],
                ["C", "ZZZ"], ["ZZZ", "A"]]
    print(try1.findItinerary(tickets1))
