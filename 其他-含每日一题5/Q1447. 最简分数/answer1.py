# encoding:utf-8
# @Author :ZQY


# 自己做，枚举
from typing import List


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        return [str(a) + "/" + str(b) for b in range(2, n + 1) for a in range(b) if math.gcd(a, b) == 1]
