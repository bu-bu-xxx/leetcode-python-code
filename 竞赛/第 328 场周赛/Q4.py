# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 2538. 最大价值和与最小价值和的差值
# 参考Q124
# 用最大路径和递归的方法解
import collections
from typing import List


class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        graph = collections.defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        pre = [-1]
        res = 0

        def dfs(node: int) -> tuple:
            nonlocal res
            if len(graph[node]) == 1 and node != 0:
                return price[node], 0

            sum_val = 0
            suffix_val = -price[node]
            pre.append(node)
            for nex_node in graph[node]:
                if nex_node == pre[-2]:
                    continue
                a, b = dfs(nex_node)
                res = max(res, sum_val + price[node] + b, \
                          suffix_val + price[node] + a)
                sum_val = max(sum_val, a)
                suffix_val = max(suffix_val, b)

            pre.pop()
            return price[node] + sum_val, price[node] + suffix_val

        dfs(0)
        return res


if __name__ == "__main__":
    try1 = Solution()
    n = 8
    edges = [[1, 7], [2, 3], [4, 0], [5, 7], [6, 3], [3, 0], [0, 7]]
    price = [4, 5, 6, 2, 2, 7, 7, 8]
    print(try1.maxOutput(n, edges, price))
