# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，贪心算法
# 从低分到高分开始排序分糖
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        order = sorted(range(len(ratings)), key=lambda s: ratings[s])
        mem = [0] * len(ratings)
        for i in order:
            lt = mem[i - 1] if i - 1 >= 0 and ratings[i - 1] != ratings[i] else 0
            rt = mem[i + 1] if i + 1 < len(ratings) and ratings[i + 1] != ratings[i] else 0
            mem[i] = max(lt, rt) + 1

        return sum(mem)


if __name__ == "__main__":
    try1 = Solution()
    ratings1 = [1, 6, 10, 8, 7, 3, 2]
    print(try1.candy(ratings1))
