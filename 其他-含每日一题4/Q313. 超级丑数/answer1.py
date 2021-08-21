# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 官方答案，最小堆
# 每次出栈，并入栈所有素数和这个值的积
# 再用哈希表防止重复
import heapq
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        heap = [1]
        mem = set()
        times = 1
        while 1:
            res = heapq.heappop(heap)
            if res not in mem:
                if times == n:
                    return res
                mem.add(res)
                for prime in primes:
                    if prime * res not in mem:
                        heapq.heappush(heap, prime * res)
                times += 1


if __name__ == "__main__":
    import data1

    try1 = Solution()
    n1, primes1 = data1.data1()
    print(try1.nthSuperUglyNumber(n1, primes1))
