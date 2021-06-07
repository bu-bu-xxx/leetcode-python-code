# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，动态规划
# 按照边迭代
# 每新迭代一个边，就多了一个点，新的点一定是子节点
# 1.更新已经遍历的点到新的点的距离
# 2.对于已经遍历的点，需要加上新的点到已有的点的距离
# 3.对于新的点，计算已遍历的点到新点的距离和
# 1步骤需要计算父节点到其他节点的距离+1，并加上父节点到当前节点的距离，一并存入路径字典path
# 备注：空间复杂度太高，导致超时
from typing import List


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        import collections
        nodes = [edges[0][0]]  # 已经遍历的点
        res = [0] * n
        path = collections.Counter()
        for edge in edges:
            if edge[0] in nodes:
                father_node, new_node = edge[0], edge[1]
            elif edge[1] in nodes:
                father_node, new_node = edge[1], edge[0]
            else:
                edges.append(edge)
                continue
            # 1.更新添加到path
            for node in nodes:
                path[(node, new_node)] += \
                    path[(father_node, node)] + path[(node, father_node)] + 1
                # 2.更新已遍历的点
                res[node] += path[(node, new_node)]
                # 3.添加新的点到res
                res[new_node] += path[(node, new_node)]
            nodes.append(new_node)

        return res


if __name__ == '__main__':
    from 树.Q834数据.data1 import data1
    try1 = Solution()
    N1, edges1 = data1()
    print(try1.sumOfDistancesInTree(N1, edges1))
