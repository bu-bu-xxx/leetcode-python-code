# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，广度优先搜索
# bfs，反向搜寻
# 看从终点出发，每一步能到哪几个点，不重复
import collections
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        searched = set()
        get_dict = collections.defaultdict(list)

        for i, val in enumerate(nums):
            for v in range(1, val + 1):
                if i + v < n:
                    get_dict[i + v].append(i)

        queue = collections.deque([n - 1])
        times = 0
        while queue:
            for _ in range(len(queue)):
                tmp = queue.popleft()
                for nex in get_dict[tmp]:
                    if nex == 0:
                        return times + 1
                    if nex not in searched:
                        searched.add(nex)
                        queue.append(nex)
            times += 1

        return 0
