# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，ez
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        count = 0
        res = 0
        for val in flowerbed:
            if val == 0:
                count += 1
            else:
                res += (count-1) // 2
                count = 0
        res += (count-1) // 2
        return res >= n
