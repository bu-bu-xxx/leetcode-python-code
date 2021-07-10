# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，广度优先搜索
# 构建已搜索set
# 每次入队列下一次转动的所有可能，碰到deadend就不存，碰到已搜索的也不存
# 当找到target就返回当前次数
import collections
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1

        begin = tuple("0000")
        searched = set()
        target = tuple(target)
        deadends = {tuple(d) for d in deadends}
        choose = {'0': ['9', '1'],
                  '1': ['0', '2'],
                  '2': ['1', '3'],
                  '3': ['2', '4'],
                  '4': ['3', '5'],
                  '5': ['4', '6'],
                  '6': ['5', '7'],
                  '7': ['6', '8'],
                  '8': ['7', '9'],
                  '9': ['8', '0'],
                  }

        queue = collections.deque()
        queue.append(begin)
        step = 0

        while queue:
            for _ in range(len(queue)):
                tmp = queue.popleft()
                if tmp == target:
                    return step

                for i in range(4):
                    nex1, nex2 = list(tmp[:]), list(tmp[:])
                    nex1[i] = choose[tmp[i]][0]
                    nex2[i] = choose[tmp[i]][1]
                    nex1, nex2 = tuple(nex1), tuple(nex2)
                    if nex1 not in deadends and nex1 not in searched:
                        queue.append(nex1)
                        searched.add(nex1)
                    if nex2 not in deadends and nex2 not in searched:
                        queue.append(nex2)
                        searched.add(nex2)
            step += 1

        return -1
