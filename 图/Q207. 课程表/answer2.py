# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，广度优先搜索，拓扑排序
# 先遍历图，记录每个点的出节点，和每个点的入度
# 先把入度为0的点入队列
# 每次出队列，然后去掉这个点，更新入度，入度为0入队列
# 队列空则停止
# 最后看符合拓扑排序的长度和题目要求的长度是否相等
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 遍历图，存出节点和入度
        graph = collections.defaultdict(list)
        in_edges = [0] * numCourses
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
            in_edges[edge[0]] += 1

        # 广度优先搜索
        queue = collections.deque([i for i in range(numCourses) \
                                   if in_edges[i] == 0])
        nums = 0
        while queue:
            node = queue.popleft()
            nums += 1
            for tmp in graph[node]:
                in_edges[tmp] -= 1
                if in_edges[tmp] == 0:
                    queue.append(tmp)

        # 最后判断
        return nums == numCourses


if __name__ == "__main__":
    try1 = Solution()
    numCourses1 = 2
    prerequisites1 = [[1, 0]]
    try2 = Solution()
    numCourses2 = 2
    prerequisites2 = [[1, 0], [0, 1]]
    print(try1.canFinish(numCourses1, prerequisites1))
    print(try2.canFinish(numCourses2, prerequisites2))
