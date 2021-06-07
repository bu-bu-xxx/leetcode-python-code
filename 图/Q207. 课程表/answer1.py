# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，深度优先搜索，拓扑排序
# 每次搜索当前节点的所有出节点，当所有出节点都已搜索，则入栈当前节点
# 三种状态：
# 0：未搜索，则转换为1搜索中
# 1：搜索中，中途碰到搜索中，说明有环
# 2：已搜索，则过，查看下一个
# 已经入栈的一定是栈底的，可以保证后入栈不影响拓扑排序的逻辑
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 出节点集合
        graph = collections.defaultdict(list)
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])

        # 深度优先搜索
        flag = True
        # stack = []
        state = [0] * numCourses

        def dfs(node: int):
            nonlocal flag
            if not flag:
                return
            state[node] = 1
            for nex in graph[node]:
                if state[nex] == 0:
                    dfs(nex)
                elif state[nex] == 1:
                    flag = False
                    return
                # else:
                #     continue
            # stack.append(node)
            state[node] = 2

        # 调用
        for i, u in enumerate(state):
            if u == 0 and flag:
                dfs(i)

        return flag


if __name__ == "__main__":
    try1 = Solution()
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    try2 = Solution()
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print(try1.canFinish(numCourses1, prerequisites1))
    print(try2.canFinish(numCourses2, prerequisites2))
