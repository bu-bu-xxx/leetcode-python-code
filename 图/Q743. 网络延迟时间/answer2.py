# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，Dijkstra算法
import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int):
        nex_time = collections.defaultdict(list)
        time_mat = [[0] * (n + 1) for _ in range(n + 1)]
        for u, v, w in times:
            nex_time[u].append(v)
            time_mat[u][v] = w

        heap = [(0, k)]
        time_list = [float('inf')] * (n + 1)
        time_list[k] = 0
        searched = set()

        # 求同源最短路径
        def relax(a, b):
            # a=now b = nex
            if (t := time_list[a] + time_mat[a][b]) < time_list[b]:
                time_list[b] = t
                heapq.heappush(heap, (t, b))

        while heap:
            (val, tmp) = heapq.heappop(heap)
            if tmp in searched:
                continue
            time_list[tmp] = val
            for nex in nex_time[tmp]:
                if nex not in searched:
                    relax(tmp, nex)
            searched.add(tmp)

        if (res := max(time_list[1:])) == float('inf'):
            return -1
        return res


if __name__ == "__main__":
    try1 = Solution()
    times1 = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n1 = 4
    k1 = 2
    print(try1.networkDelayTime(times1, n1, k1))
