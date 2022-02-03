# encoding:utf-8
# @Author :ZQY


# 官方答案，贪心算法
# 更多偏向数学证明
# 可以证明：
# F(m) = max(F<=k)F，F0 = 1
# 2F(x) = F(x+1) + F(x-2)
# 所以一定不会有相邻或重叠的F
# F(m)-1 = F(m-1) + F(m-3) + ... + F(1)orF(2)
# 所以每次选取最大的F(m)即可
import bisect


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # 生成<=k的斐波那契数列
        f_list = [1, 1]
        idx0, idx1 = 0, 1
        while (tmp := f_list[idx0] + f_list[idx1]) <= k:
            f_list.append(tmp)
            idx0 += 1
            idx1 += 1

        # 迭代选数
        res = 0
        while k > 0:
            k -= f_list[bisect.bisect_right(f_list, k) - 1]
            res += 1

        return res
