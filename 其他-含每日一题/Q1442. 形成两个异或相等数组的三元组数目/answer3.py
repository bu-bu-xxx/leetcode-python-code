# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，一重循环
# 所有arr元素大于0，所以必定两个以上的异或和等于0
# 用字典存前面的val:index，当后面的val相同，说明index'-index中间的异或和为0
# 字典要存val值相同的index个数和index之和

class Solution:
    def countTriplets(self, arr) -> int:
        import collections
        dict_index, dict_num = \
            collections.Counter({0: -1}), collections.Counter({0: 1})
        result = 0
        val = 0
        for index in range(len(arr)):
            val ^= arr[index]
            if val in dict_index:
                result += dict_num[val] * (index - 1) - dict_index[val]
            dict_num[val] += 1
            dict_index[val] += index
        return result
