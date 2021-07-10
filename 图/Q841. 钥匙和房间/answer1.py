# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，深度优先搜索
# 递归，标记当前房间已经来过，打开没去过的房间
# 最后看是否每个房间都来过
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        tag = [0] * n

        # 深度优先搜索
        def dfs(room):
            tag[room] = 1
            for nex in rooms[room]:
                if tag[nex] == 0:
                    dfs(nex)

        # 执行
        dfs(0)
        if min(tag) == 0:
            return False
        return True
