# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 用自己定义的Heap函数做

from 堆.Heap import Heap


class Solution:
    def lastStoneWeight(self, stones):
        heap = Heap.Heap()
        stones = [-i for i in stones]
        heap.heapify(stones)
        while len(stones) > 1:
            temp1 = heap.heappop(stones)
            temp2 = heap.heappop(stones)
            if temp1 != temp2:
                new = -abs(temp1 - temp2)
                heap.heappush(stones, new)
        if len(stones) == 0: return 0
        return -stones[0]


if __name__ == '__main__':
    try1 = Solution()

    stones = [2, 7, 4, 1, 8, 1]
    print(try1.lastStoneWeight(stones))
