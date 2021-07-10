# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，广度优先搜索
# 每次出栈一个房间标记为已开，然后搜索未去的钥匙
# 存入队列中
# 最后看是否每个房间都开过
import collections
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        tag = [0] * n

        # 广度优先搜索
        queue = collections.deque([0])
        while queue:
            tmp = queue.popleft()
            tag[tmp] = 1
            for nex in rooms[tmp]:
                if tag[nex] == 0:
                    queue.append(nex)

        # 判断
        if min(tag) == 0:
            return False
        return True
