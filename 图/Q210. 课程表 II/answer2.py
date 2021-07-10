# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，广度优先搜索，拓扑排序
# 和Q207类似
# 每次遍历存入度为0的点到队列
# 出队列则删除这个点，更新一次出度表
# 出队列的点即为拓扑排序
# 如果最后的输出数组长度不等于总长度，则说明不可拓扑排序
from typing import List
import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        count = [0] * numCourses
        for edge in prerequisites:
            graph[edge[1]].append(edge[0])
            count[edge[0]] += 1
        # 初始化队列
        queue = collections.deque([i for i in range(numCourses) \
                                   if count[i] == 0])
        res = []
        # 广度优先搜索
        while queue:
            tmp = queue.popleft()
            res.append(tmp)
            for nex in graph[tmp]:
                count[nex] -= 1
                if count[nex] == 0:
                    queue.append(nex)

        if len(res) == numCourses:
            return res
        else:
            return []
