# encoding:utf-8
# @Author :ZQY


# 5995. 字符串分组
# 不出意外，时间复杂度太高
import collections
from typing import List


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        rec = list(range(len(words)))

        def search(idx):
            if rec[idx] == idx:
                return idx
            rec[idx] = search(rec[idx])
            return rec[idx]

        def merge(idx1, idx2):
            rec[search(idx2)] = search(idx1)

        def judge(s1: str, s2: str):
            tmp = 0
            count = collections.Counter()
            for s in s1:
                count[s] += 1
            for s in s2:
                count[s] -= 1
            if list(count.values()).count(-1) <= 1 and list(count.values()).count(1) <= 1:
                return True
            return False

        for i in range(len(words)):
            for j in range(i):
                if judge(words[i], words[j]):
                    merge(i, j)

        count = collections.Counter()
        for i in range(len(words)):
            count[search(i)] += 1

        ans = list()
        ans.append(len(list(count.keys())))
        ans.append(max(list(count.values())))
        return ans


if __name__ == "__main__":
    try1 = Solution()
    words1 = ["ghnv", "uip", "tenv", "hvepx", "e", "ktc", "byjdt", "ulm", "cae", "ea"]
    print(try1.groupStrings(words1))
