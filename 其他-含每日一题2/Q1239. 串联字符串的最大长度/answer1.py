# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做，广度优先遍历
# queue存每一种可能
import collections
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        queue = collections.deque()
        queue.append(set())

        # bfs，每次出队列所有元素
        for i in range(0, len(arr)):
            arr_tmp = set(arr[i])
            if len(arr_tmp) != len(arr[i]):
                continue
            for _ in range(len(queue)):
                tmp = queue.popleft()
                queue.append(tmp)
                tmp1 = tmp.copy()
                tmp1 |= arr_tmp
                if len(tmp) + len(arr_tmp) == len(tmp1):
                    queue.append(tmp1)
        return max([len(s) for s in queue])


if __name__ == "__main__":
    try1 = Solution()
    arr1 = ["cha", "r", "act", "ers"]
    print(try1.maxLength(arr1))
