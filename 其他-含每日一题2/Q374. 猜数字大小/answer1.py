# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，二分法


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher,
# otherwise return 0
# def guess(num: int) -> int:
def guess(num: int) -> int:
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        def search(low, high):
            mid = (low + high) // 2
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                return search(mid + 1, high)
            else:
                return search(low, mid - 1)

        return search(1, n)
