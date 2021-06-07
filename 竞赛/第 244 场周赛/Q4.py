# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# Q4
# 5779. 装包裹的最小浪费空间
from typing import List
import bisect


class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages = sorted(packages)
        boxes = [sorted(b) for b in boxes]
        mod = 10 ** 9 + 7

        pre = [0] * len(packages)
        pre[0] = packages[0]
        for i in range(1, len(pre)):
            pre[i] = pre[i - 1] + packages[i]
        pre.append(0)

        res = float('inf')
        for i, box in enumerate(boxes):
            if box[-1] < packages[-1]:
                continue
            index_last = 0
            tmp = 0
            for b in box:
                index = bisect.bisect_right(packages, b)
                # index = bisect_right(packages, b)
                tmp += (index - index_last) * b - (pre[index - 1] - pre[index_last - 1])
                index_last = index
            res = min(res, tmp)

        if res == float('inf'):
            return -1
        return res % mod


def bisect_right(nums: List[int], val: int):
    def search(left, right):
        mid = (left + right) // 2
        if left == right:
            return left
        if nums[mid] <= val:
            return search(mid + 1, right)
        else:
            return search(left, mid)

    return search(0, len(nums))


if __name__ == '__main__':
    try1 = Solution()
    packages1 = [2, 3, 5]
    boxes1 = [[4, 8], [2, 8]]
    print(try1.minWastedSpace(packages1, boxes1))
