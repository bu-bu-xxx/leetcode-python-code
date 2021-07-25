# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，数学，贪心算法
# 1.可以证明，sum(gas)>=sum(cost)则可以环绕一周
# 2.因为有且仅有一个答案，所以可证明，假设从起点开始，到达i点的油箱油最少(负数)，则i+1点为起点
from typing import List

import numpy


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        store = [0] * len(gas)
        ans = 0
        for i in range(len(gas)):
            ans += gas[i] - cost[i]
            store[i] = ans
        return int(numpy.argmin(store) + 1) % len(gas)


if __name__ == "__main__":
    try1 = Solution()
    gas1 = [1, 2, 3, 4, 5]
    cost1 = [3, 4, 5, 1, 2]
    print(try1.canCompleteCircuit(gas1, cost1))
