# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，直接排序，再找第k个
# xorMatrix[i][j]=xorMatrix[i-1][j]^xorMatrix[i][j-1]^ \
# xorMatrix[i-1][j-1]^matrix[i-1][j-1]

class Solution:
    def kthLargestValue(self, matrix, k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        xorMatrix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                xorMatrix[i][j] = xorMatrix[i - 1][j] ^ xorMatrix[i][j - 1] ^ \
                                  xorMatrix[i - 1][j - 1] ^ matrix[i-1][j-1]
        result = [xorMatrix[i][j] for i in range(1, m + 1) for j in range(1, n + 1)]
        return sorted(result, reverse=True)[k - 1]


if __name__ == '__main__':
    import random
    try1 = Solution()

    matrix1 = [[random.randint(0, 10) for _ in range(1000)] for _ in range(1000)]
    k1 = 401
    print(try1.kthLargestValue(matrix1, k1))
