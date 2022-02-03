# encoding:utf-8
# @Author :ZQY


# 自己做，贪心算法
# 备注：时间复杂度超了，有点难
# 依次找1，2，3...个数之和有没有k


class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # 生成<=k的斐波那契数列
        f_list = [1, 1]
        idx0, idx1 = 0, 1
        while (tmp := f_list[idx0] + f_list[idx1]) <= k:
            f_list.append(tmp)
            idx0 += 1
            idx1 += 1

        # 贪心搜索
        old_set = {0}
        for res in range(1, k + 1):
            new_set = set()
            for i in f_list:
                for j in old_set:
                    if i + j == k:
                        return res
                    if i + j < k:
                        new_set.add(i + j)
            old_set = new_set
