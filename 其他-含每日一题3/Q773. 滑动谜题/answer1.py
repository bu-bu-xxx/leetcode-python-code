# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，广度优先遍历
# (i,j,不需要遍历的方向)
# 方向：1往左，2往右，3往上，4往下
import collections
from typing import List


class Solution:
    def find(self, status):
        for i in range(2):
            for j in range(3):
                if status[i][j] == 0:
                    return i, j

    def change(self, status, num):
        ret = [s[:] for s in status]
        dirc = self.find(status)
        if num == 1:
            ret[dirc[0]][dirc[1]], ret[dirc[0]][dirc[1] - 1] = ret[dirc[0]][dirc[1] - 1], ret[dirc[0]][dirc[1]]
            return ret
        if num == 2:
            ret[dirc[0]][dirc[1]], ret[dirc[0]][dirc[1] + 1] = ret[dirc[0]][dirc[1] + 1], ret[dirc[0]][dirc[1]]
            return ret
        if num == 3:
            ret[dirc[0] - 1][dirc[1]], ret[dirc[0]][dirc[1]] = ret[dirc[0]][dirc[1]], ret[dirc[0] - 1][dirc[1]]
            return ret
        if num == 4:
            ret[dirc[0] + 1][dirc[1]], ret[dirc[0]][dirc[1]] = ret[dirc[0]][dirc[1]], ret[dirc[0] + 1][dirc[1]]
            return ret

    def slidingPuzzle(self, board: List[List[int]]) -> int:
        directions = {
            (0, 0): {2, 4},
            (0, 1): {1, 2, 4},
            (0, 2): {1, 4},
            (1, 0): {3, 2},
            (1, 1): {3, 2, 1},
            (1, 2): {3, 1}
        }
        target = [[1, 2, 3], [4, 5, 0]]
        searched = list()
        queue = collections.deque()
        step = 0
        queue.append(board)

        while queue:
            for _ in range(len(queue)):
                tmp = queue.popleft()
                if tmp == target:
                    return step
                for direction in directions[self.find(tmp)]:
                    nex = self.change(tmp, direction)
                    if nex is not None and nex not in searched:
                        queue.append(nex)
                searched.append(tmp)
            step += 1

        return -1


if __name__ == "__main__":
    try1 = Solution()
    board1 = [[4, 1, 2], [5, 0, 3]]
    print(try1.slidingPuzzle(board1))
