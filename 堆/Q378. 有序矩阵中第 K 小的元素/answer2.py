# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 动态规划，自己做
# 依次遍历n行，找到最小的数
# 找到后向后读取一位，到n停止
# 找到第k个最小的数，return

# 时间复杂度太高了，不行

class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        for i in range(n):
            matrix[i].append(10 ** 8)
        record = [0] * n
        for i in range(k):
            min_val = min([matrix[j][record[j]] for j in range(n)])
            for j in range(n):
                if matrix[j][record[j]] == min_val:
                    record[j] += 1
                    break
        return min_val


if __name__ == '__main__':
    try1 = Solution()

    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(try1.kthSmallest(matrix, k))
