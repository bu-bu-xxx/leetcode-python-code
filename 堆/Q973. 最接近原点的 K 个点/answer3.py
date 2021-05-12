# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 快速选择，自己做，答案给的不好读
# 题设答案唯一

class Solution:
    def kClosest(self, points, k):
        import random
        count = lambda s: s[0] ** 2 + s[1] ** 2

        def closeK(low, high):
            pivot = random.randint(low, high)
            base = count(points[pivot])
            points[pivot], points[low] = points[low], points[pivot]
            i = low + 1
            for j in range(low + 1, high + 1):
                if count(points[j]) < base:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            i -= 1
            points[i], points[low] = points[low], points[i]
            if i == k - 1:
                return points[0:k]
            elif i < k - 1:
                return closeK(i + 1, high)
            else:
                return closeK(low, i - 1)

        return closeK(0, len(points) - 1)


if __name__ == '__main__':
    try1 = Solution()

    points = [[1, 3], [-2, 2]]
    k = 1
    print(try1.kClosest(points, k))
