# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 5852. 最小化目标值与所选元素的差
from typing import List


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        m,n = len(mat),len(mat[0])
        dp = [0]*target*2
        dp[0] = 1
        for i in range(m):
            dp_nex = [0]*target*2
            for k in range(target*2):
                if dp[k] == 1:
                    for j in range(n):
                        if mat[i][j]+k<len(dp_nex):
                            dp_nex[mat[i][j]+k] = 1
            dp = dp_nex

        res = abs(sum([min(mat[i]) for i in range(m)])-target)
        for i,val in enumerate(dp):
            if val == 1:
                res = min(abs(target-i),res)
        return res


if __name__ == "__main__":
    try1 = Solution()
    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    target1 = 13
    print(try1.minimizeTheDifference(mat1,target1))


