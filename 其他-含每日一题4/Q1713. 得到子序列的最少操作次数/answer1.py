# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，最长路径问题，动态规划
# 按照拓扑排序的方式画图，倒序遍历arr，计算每个点的最长路径
import collections
from typing import List


class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        nodes = collections.defaultdict(list)
        for i, s in enumerate(arr):
            nodes[s].append(i)

        roads = collections.defaultdict(list)
        mem = []
        for s in target[-1::-1]:
            roads[s] += mem[:]
            mem += nodes[s][:]

        col = [1] * len(arr)
        for i in range(len(arr) - 1, -1, -1):
            now = arr[i]
            tmp = 0
            for nex in roads[now]:
                if nex > i:
                    tmp = max(col[nex], tmp)
            col[i] = tmp + 1

        flag = False
        for val in roads.values():
            if val:
                flag = True
                break

        if flag:
            return len(target) - max(col)
        return len(target)


if __name__ == "__main__":
    try1 = Solution()
    target1 = [6, 4, 8, 1, 3, 2]
    arr1 = [4, 7, 6, 2, 3, 8, 6, 1]
    print(try1.minOperations(target1, arr1))
