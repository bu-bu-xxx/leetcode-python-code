# encoding:utf-8
# @Author :ZQY


# 参考宫水三叶答案，差分
# web: https://leetcode-cn.com/link/?target=https%3A//mp.weixin.qq.com/s?__biz%3DMzU4NDE3MTEyMA%3D%3D%26mid%3D2247490329%26idx%3D1%26sn%3D6d448a53cd722bbd990fda82bd262857%26chksm%3Dfd9cb006caeb3910758522054564348b7eb4bde333889300bd5d249950be12a5b990b5d2c059%26token%3D168273153%26lang%3Dzh_CN%23rd
# 差分就像前缀和的逆过程
# 主要计算，区间修改，单点查询
from typing import List


class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        diff = [0] * len(nums)
        n = len(nums)

        # 差分计算
        def diffEvaluate(beg, end, val):
            if 0 <= beg < len(nums):
                diff[beg] += val
            if 0 <= end + 1 < len(nums):
                diff[end + 1] -= val

        for i in range(len(nums)):
            x = nums[i]
            if i >= x:
                diffEvaluate(0, i - x, 1)
                diffEvaluate(i + 1, n - 1, 1)
            else:
                diffEvaluate(i + 1, i - x + n, 1)

        # 计算前缀和，即k轮得分
        max_points = -1
        res = 0
        points = 0
        for time in range(len(nums)):
            points += diff[time]
            if points > max_points:
                max_points = points
                res = time
        return res


if __name__ == "__main__":
    try1 = Solution()
    nums = [2, 3, 1, 4, 0]
    print(try1.bestRotation(nums=nums))
