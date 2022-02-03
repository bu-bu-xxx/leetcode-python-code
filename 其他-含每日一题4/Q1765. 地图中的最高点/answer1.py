# encoding:utf-8
# @Author :ZQY


# 自己做，BFS
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        queue = [(-1,-1)]
        m, n = len(isWater), len(isWater[0])
        height = [[-1]*n for _ in range(m)]

        def neighbors(node:tuple)->List[tuple]:
            if node == (-1,-1):
                ret = []
                for i in range(m):
                    for j in range(n):
                        if isWater[i][j] == 1:
                            ret.append((i,j))
            else:
                ret = []
                if node[0]-1>=0:
                    ret.append((node[0]-1,node[1]))
                if node[0]+1 <m:
                    ret.append((node[0]+1,node[1]))
                if node[1] -1>=0:
                    ret.append((node[0],node[1]-1))
                if node[1]+1<n:
                    ret.append((node[0],node[1]+1))
            return ret

        h_tmp = 0
        while queue:
            for _ in range(len(queue)):
                node_tmp = queue.pop(0)
                for neighbor in neighbors(node_tmp):
                    if height[neighbor[0]][neighbor[1]] == -1:
                        height[neighbor[0]][neighbor[1]] = h_tmp
                        queue.append(neighbor)
            h_tmp += 1

        return height


if __name__ == "__main__":
    try1 = Solution()
    isWater = [[0,1,1,1,0,1,1],[0,1,0,1,0,0,0],[0,1,0,1,0,1,1],[1,1,1,1,0,1,0],[1,0,1,1,1,1,1],[1,1,0,0,0,1,1],[1,1,1,1,0,1,0],[1,0,0,1,1,0,0],[1,1,1,0,1,1,0],[1,0,0,0,1,0,1]]
    print(try1.highestPeak(isWater))




