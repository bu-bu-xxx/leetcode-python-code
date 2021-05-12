# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 归并排序，即堆法
# 先用第一列作为小顶堆
# 每次出堆一个数，就进堆该行下一个数，直到没有下一个数就只出不进
# 出第k次停止

class Solution:
    def kthSmallest(self, matrix, k):
        import heapq
        # 构建小顶堆
        n = len(matrix)
        heap = [(i[0], x, 0) for (x, i) in enumerate(matrix)]
        # 排序
        for _ in range(k):
            (val, x, y) = heapq.heappop(heap)
            if y < n - 1:
                heapq.heappush(heap, (matrix[x][y + 1], x, y + 1))
        # 找到第k个
        return val


if __name__ == '__main__':
    try1 = Solution()

    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(try1.kthSmallest(matrix, k))
