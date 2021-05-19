# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，两重循环
# 找出^arr[i:k]=0的一串，其中有k-i种三元数

class Solution:
    def countTriplets(self, arr) -> int:
        n = len(arr)
        result = 0
        for i in range(n - 1):
            temp = arr[i]
            for k in range(i + 1, n):
                temp ^= arr[k]
                if temp == 0:
                    result += k - i
        return result
