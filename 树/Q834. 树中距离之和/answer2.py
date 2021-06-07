# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 高分答案
# 空间复杂度降为O(n)
# 主要思想就是分层，每个节点的距离和就是层数得来的
from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        tree = [[] for _ in range(N)]
        # 存每个点连接的点有哪些
        for baba, child in edges:
            tree[baba].append(child)
            tree[child].append(baba)
        depth = [0 for _ in range(N)]
        count = [0 for _ in range(N)]

        def dfsForDepthAndCount(baba0, grandpa):
            # 从根节点往子节点遍历
            # depth为层数，count为子节点数量(含自己)
            count[baba0] = 1
            for child0 in tree[baba0]:
                if child0 != grandpa:
                    depth[child0] = depth[baba0] + 1
                    dfsForDepthAndCount(child0, baba0)
                    count[baba0] += count[child0]

        dfsForDepthAndCount(0, -1)
        answer = [0 for _ in range(N)]
        answer[0] = sum(depth)

        def dfsForAnswer(baba1, grandpa):
            # 计算距离和
            for child1 in tree[baba1]:
                if child1 != grandpa:
                    # 关键在下面这个计算公式，通过父节点计算得到子节点距离和
                    answer[child1] = answer[baba1] + N - 2 * count[child1]
                    dfsForAnswer(child1, baba1)

        dfsForAnswer(0, -1)
        return answer


if __name__ == '__main__':
    from 树.Q834数据.data1 import data1
    try1 = Solution()
    N1, edges1 = data1()
    print(try1.sumOfDistancesInTree(N1, edges1))
