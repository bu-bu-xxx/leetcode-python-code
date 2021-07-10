# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，二分查找


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    pass


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        def search(low, high):
            if low == high:
                return low
            mid = (low + high) // 2
            if isBadVersion(mid):
                return search(low, mid)
            else:
                return search(mid + 1, high)

        return search(1, n)
