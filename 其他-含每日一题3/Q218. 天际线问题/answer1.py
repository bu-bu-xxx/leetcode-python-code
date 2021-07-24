# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，堆排序
# 给房子标序号，用最大堆表示当前最高房子高度
# 从小到大依次遍历房子左端点和右端点
# 左端点：比最高的还高，则入堆，并house.add()，然后输出左端点坐标
#      ：更小的话入堆，add
# 右端点：如果是最高则pop，并且输出第二高房子坐标
#      ：如果不是最高则house-{}
# 每次检查堆顶都要看是否在house里面，不在则pop，添加最矮房子高度0
import heapq
from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # (i,x,y)第i个房子，y<0左端点，y>0右端点
        nodes = []
        for i, (lt, rt, ht) in enumerate(buildings):
            nodes.append((i, lt, -ht))
            nodes.append((i, rt, ht))
        nodes = sorted(nodes, key=lambda s: s[1:3])

        # (-高度,房子序号)
        house = {-1}
        heap = [(0, -1)]
        res = []

        def check_max():
            while heap[0][1] not in house:
                heapq.heappop(heap)
            return -heap[0][0]

        for (i, xt, ht) in nodes:
            if ht < 0:
                ht = -ht
                if ht > check_max():
                    res.append([xt, ht])
                heapq.heappush(heap, (-ht, i))
                house.add(i)
            elif ht > 0:
                house -= {i}
                if check_max() < ht:
                    res.append([xt, check_max()])

        return res


if __name__ == "__main__":
    try1 = Solution()
    buildings1 = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print(try1.getSkyline(buildings1))
