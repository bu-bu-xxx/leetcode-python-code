# encoding:utf-8
# @Author :ZQY


# 自己做，差分
from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        for first, last, seats in bookings:
            diff[first - 1] += seats
            diff[last] -= seats

        res = [0] * n
        tmp = 0
        for i in range(n):
            tmp += diff[i]
            res[i] = tmp
        return res
