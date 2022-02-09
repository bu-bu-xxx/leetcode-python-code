# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 5853. 从子集的和还原数组
# 第二名的答案
import collections
from typing import List


class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        def remove_v(nt, t):
            assert t >= 0
            to_remove = collections.Counter()
            small = []
            large = []
            for v in nt:
                if to_remove[v] > 0:
                    to_remove[v] -= 1
                    continue
                small.append(v)
                large.append(v + t)
                to_remove[v + t] += 1
            if not len(small) * 2 == len(nt):
                return None, None

            return small, large

        def solve(n=n, sums=sums):
            if sums is None:
                sums = sums
            if n == 1:
                return [sums[1]] if sums[0] == 0 else [sums[0]]

            sums = sorted(sums)
            t = sums[-1] - sums[-2]
            # 要么存在t，要么存在-t
            small, large = remove_v(sums, t)
            if small is None:
                return None

            if t in sums:
                t1 = solve(n - 1, small)
                if not t1 is None:
                    return [t] + t1
            if -t in sums:
                t1 = solve(n - 1, large)
                if not t1 is None:
                    return [-t] + t1
            return None

        return solve()


if __name__ == "__main__":
    try1 = Solution()
    n1 = 5
    sums1 = [1084, 1269, -117, 1201, 155, 204, -49, 0, -166, 997, -234, 272, 1152, 389, 1435, 321, 38, 555, 1035, 831,
             880, -400, -283, 714, 1318, 918, 597, 646, 117, 480, 438, 763]
    print(try1.recoverArray(n1, sums1))
