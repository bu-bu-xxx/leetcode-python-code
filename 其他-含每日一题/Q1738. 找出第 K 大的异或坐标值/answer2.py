# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，快速选择算法
# xorMatrix[i][j]=xorMatrix[i-1][j]^xorMatrix[i][j-1]^ \
# xorMatrix[i-1][j-1]^matrix[i-1][j-1]
# 计算完xorMatrix变成一维度数组，用快速选择找出第k个数
# 返回等于base的index开始和结尾

class Solution:
    def kthLargestValue(self, matrix, k: int) -> int:
        # 计算xorMatrix
        m, n = len(matrix), len(matrix[0])
        xorMatrix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                xorMatrix[i][j] = xorMatrix[i - 1][j] ^ xorMatrix[i][j - 1] ^ \
                                  xorMatrix[i - 1][j - 1] ^ matrix[i - 1][j - 1]
        result = [xorMatrix[i][j] for i in range(1, m + 1) for j in range(1, n + 1)]

        # 快速排序，从大到小
        import random, operator

        def fastSort(res, begin, end):
            choose = random.randint(begin, end)
            base = res[choose]
            res[begin], res[choose] = res[choose], res[begin]
            slow1, slow2 = begin + 1, begin + 1
            for fast in range(begin + 1, end + 1):
                if res[fast] == base:
                    res[fast], res[slow2] = res[slow2], res[fast]
                    slow2 += 1
                elif res[fast] > base:
                    res[fast], res[slow2] = res[slow2], res[fast]
                    res[slow1], res[slow2] = res[slow2], res[slow1]
                    slow1 += 1
                    slow2 += 1

            res[slow1 - 1], res[begin] = res[begin], res[slow1 - 1]
            slow1 -= 1
            # [slow1,slow2)是等于base的数
            return res, slow1, slow2 - 1

        a, b = 0, m * n - 1
        while a != b:
            result, s1, s2 = fastSort(result, a, b)
            if s1 <= k - 1 <= s2:
                return result[k - 1]
            if s2 < k - 1:
                a = s2 + 1
            else:
                b = s1 - 1
        return result[a]


if __name__ == '__main__':
    import random

    try1 = Solution()

    matrix1 = [[random.randint(0, 10) for _ in range(1000)] for _ in range(1000)]
    k1 = 401
    matrix2 = [[5, 2], [1, 6]]
    k2 = 1
    print(try1.kthLargestValue(matrix2, k2))
