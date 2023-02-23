# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做，数学
import math
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount = sorted(amount)
        if amount[2] >= (amount[0] + amount[1]):
            return amount[2]
        return math.ceil(sum(amount) / 2)
