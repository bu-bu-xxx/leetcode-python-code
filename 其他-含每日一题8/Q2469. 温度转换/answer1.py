# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 简单
from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.8 + 32]
