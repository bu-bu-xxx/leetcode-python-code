# encoding:utf-8
# @Author :ZQY


# 自己做，简单数学题
from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)*2
        for t in range(len(arr)):
            tmp = arr.index(len(arr)-t)
            arr = arr[:tmp+1][-1::-1]+arr[tmp+1:]
            res[2*t] = tmp+1
            arr = arr[:len(arr)-t][-1::-1] + arr[len(arr)-t:]
            res[2*t+1] = len(arr)-t

        return res




