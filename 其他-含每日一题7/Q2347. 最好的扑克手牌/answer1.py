# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 简单，自己做
import collections
from typing import List


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        ranks_dict = collections.Counter(ranks)
        if len(set(suits)) == 1:
            return "Flush"
        elif 3 in ranks_dict.values() \
                or 4 in ranks_dict.values() \
                or 5 in ranks_dict.values():
            return "Three of a Kind"
        elif 2 in ranks_dict.values():
            return "Pair"
        else:
            return "High Card"


if __name__ == "__main__":
    try1 = Solution()
    ranks = [5, 8, 2, 11, 4]
    suits = ["d", "a", "d", "b", "c"]
    print(try1.bestHand(ranks, suits))
