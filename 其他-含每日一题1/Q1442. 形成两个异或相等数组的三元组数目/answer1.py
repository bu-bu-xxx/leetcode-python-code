# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，两重循环
# 时间复杂度O(n2)，空间复杂度O(n2)

class Solution:
    def countTriplets(self, arr) -> int:
        n = len(arr)
        # a值表
        xorList = [[0] * n for _ in range(n)]
        for i in range(n):
            xorList[i][i] = arr[i]
        for i in range(n):
            for j in range(i + 1, n):
                xorList[i][j] = xorList[i][j - 1] ^ arr[j]

        # 找ab相同的数量
        import collections
        count = 0
        for j in range(1, n):
            a = collections.Counter([x[j - 1] for x in xorList[:j]])
            b = collections.Counter(xorList[j][j:])
            for key in a.keys():
                count += a[key] * b[key]

        return count


if __name__ == '__main__':
    try1 = Solution()

    arr1 = [2, 3, 1, 6, 7]
    print(try1.countTriplets(arr1))
