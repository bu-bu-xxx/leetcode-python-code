# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，数学
# n=(11...1)k进制，m位数
# 迭代m，不迭代k
# m<=log_k(n)，递减搜索
# k+1 > n**(1/m) > k
import math


class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        for m in range(math.floor(math.log(n, 2)), 1, -1):
            k = math.floor(n ** (1 / m))
            if n * (k - 1) == k ** (m + 1) - 1:
                return str(k)
        return str(n-1)


if __name__ == "__main__":
    try1 = Solution()
    n1 = "1000000000000000000"
    print(try1.smallestGoodBase(n1))
