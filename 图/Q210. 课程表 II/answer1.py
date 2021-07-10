# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，深度优先搜索，拓扑排序
# 和Q207类似
# 遍历所有未遍历的点，然后已遍历的点存起来
# 0表示未遍历的点，1表示搜索中的点，2表示已经遍历的点
# 每个点都要搜索所有出点，搜索完就可以入栈
# 如果中途发现搜索中的点，说明有环，不能构成拓扑排序
from typing import List
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        record = [0] * numCourses
        # 构建图
        graph = collections.defaultdict(list)
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
        # 深度优先搜索
        stack = []
        flag = True

        def dfs(node):
            nonlocal flag
            record[node] = 1
            for nex in graph[node]:
                if record[nex] == 1:
                    flag = False
                    return
                elif record[nex] == 0:
                    dfs(nex)
                    if not flag:
                        return
            record[node] = 2
            stack.append(node)

        # 执行
        for i, val in enumerate(record):
            if val == 0 and flag:
                dfs(i)
        if flag:
            return stack[-1::-1]
        else:
            return []


if __name__ == "__main__":
    try1 = Solution()
    a1 = 4
    b1 = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(try1.findOrder(a1, b1))
