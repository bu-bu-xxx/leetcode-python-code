# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，并查集
# 如果发现不等的属于一个根，则False
# 否则True
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        base = ord('a')
        state = list(range(26))

        def find(num: int) -> int:
            if state[num] == num:
                return num
            state[num] = find(state[num])
            return state[num]

        def merge(num1: int, num2: int):
            root1 = find(num1)
            root2 = find(num2)
            state[root2] = root1

        for (letter1, sign, _, letter2) in equations:
            num1 = ord(letter1) - base
            num2 = ord(letter2) - base
            if sign == '=':
                merge(num1, num2)
        for (letter1, sign, _, letter2) in equations:
            num1 = ord(letter1) - base
            num2 = ord(letter2) - base
            if sign == '!':
                if find(num1) == find(num2):
                    return False

        return True
