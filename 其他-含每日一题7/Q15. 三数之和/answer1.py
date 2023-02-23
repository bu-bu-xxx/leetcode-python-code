# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做，动态规划
# 复杂度过高，不合适
# 答案中双指针也可以解，就是考虑一定会选到i，剩下两个数一定指针大于i，即可不重复
import bisect
import collections
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        nums_tmp = [nums[0], nums[1]]
        for i in range(2, len(nums)):
            if nums[i - 2] == nums[i - 1] and nums[i - 1] == nums[i]:
                continue
            nums_tmp.append(nums[i])

        if bisect.bisect_right(nums, 0) - bisect.bisect_left(nums, 0) >= 3:
            res.append([0, 0, 0])
        nums = nums_tmp
        if len(nums) < 3:
            return res

        record = collections.defaultdict(list)
        record[nums[0] + nums[1]].append([nums[0], nums[1]])

        for i in range(2, len(nums)):
            val = nums[i]
            if nums[i - 1] == val:
                idx = bisect.bisect_left(nums, -2 * val)
                if idx < i and nums[idx] == -2 * val and val != 0:
                    res.append([nums[idx], val, val])
                record[val * 2].append([val, val])
                continue

            for s in record[-val]:
                res.append(s + [val])
            for j in range(0, i):
                val2 = nums[j]
                if j > 0 and nums[j] == nums[j - 1]:
                    continue
                record[val2 + val].append([val2, val])

        return res


if __name__ == "__main__":
    try1 = Solution()
    nums = [1, -1, -1, 0]
    print(try1.threeSum(nums))
