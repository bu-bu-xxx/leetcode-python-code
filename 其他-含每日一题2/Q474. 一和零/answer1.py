# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，深度优先搜索，遍历
# 从第一个开始，搜索不超过限制条件的子节点
# 计算剩下的mn数量，然后迭代下一个点，返回最大子集数量
from typing import List
import re


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 统计0，1数量
        len_strs = len(strs)
        count = [[0, 0] for _ in range(len_strs)]
        for i, s in enumerate(strs):
            count[i][1] = len(re.findall(r'([1])', s))
            count[i][0] = len(s) - count[i][1]

        # 深度优先搜索
        count.append([0, 0])

        def dfs(m0, n1, index):
            m0 -= count[index][0]
            n1 -= count[index][1]
            tmp = 0
            for j in range(index + 1, len_strs):
                if count[j][0] <= m0 and count[j][1] <= n1:
                    tmp = max(tmp, dfs(m0, n1, j))
            return tmp + 1

        res = 0
        for l in range(len_strs):
            if count[l][0] <= m and count[l][1] <= n:
                res = max(res, dfs(m, n, l))
        return res


if __name__ == '__main__':
    try1 = Solution()
    strs1 = ["0", "11", "1000", "01", "0", "101", "1", "1", "1", "0", "0", "0", "0", "1", "0", "0110101", "0", "11",
             "01", "00", "01111", "0011", "1", "1000", "0", "11101", "1", "0", "10", "0111"]
    m1 = 9
    n1 = 80
    # print(try1.findMaxForm(strs1, m1, n1))

    print(try1.findMaxForm(strs1, 10000, 10000))
    print(len(strs1))
