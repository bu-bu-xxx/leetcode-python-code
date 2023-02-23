# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 二分查找
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        maxSum -= n

        def count(length, i):
            if i <= length:
                return (1 + i) * i / 2
            else:
                return (i + i - length + 1) * length / 2

        len_left = index + 1
        len_right = n - len_left + 1

        def find(min_j, max_j):
            if min_j == max_j:
                return min_j
            mid_j = (min_j + max_j) // 2
            if count(len_left, mid_j) + count(len_right, mid_j) - mid_j > maxSum:
                return find(min_j, mid_j)
            return find(mid_j + 1, max_j)

        return find(1, maxSum + 1)


if __name__ == "__main__":
    try1 = Solution()
    print(try1.maxValue(1, 0, 24))
