# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，简单
# 遍历每一个数，存对应数位上的1和0的数量
# 再遍历一次计算hm距离总和
# 备注：这个做法不好，用二进制做法做复杂度均降低
import collections
from typing import List


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        count = []
        for num_i in range(len(nums)):
            num = nums[num_i]
            num = str(bin(num))[2:]
            # count不够长，则增长，补齐前面小的数的0
            if (len_add := len(num) - len(count)) > 0:
                count += [collections.Counter(['0'] * num_i) for _ in range(len_add)]
            else:
                # 补齐后面的0
                for j in count[-1:-1 + len_add:-1]:
                    j['0'] += 1
            # 存当前数
            index = 0
            for i in num[-1::-1]:
                count[index][i] += 1
                index += 1

        # 计算hm总和
        result = 0
        for each in count:
            result += each['1'] * each['0']
        return result


if __name__ == '__main__':
    try1 = Solution()
    nums1 = [4, 14, 2]
    print(try1.totalHammingDistance(nums1))
