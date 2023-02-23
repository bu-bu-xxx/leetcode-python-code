# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做
# 动态规划，Q139类似
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)

        dp_bool = [1] + [0] * len(s)
        dp_pre = [['']] + [[] for _ in range(len(s))]
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp_bool[j] == 1 and (word := s[j:i]) in wordDict:
                    dp_bool[i] = 1
                    for tmp_str in dp_pre[j]:
                        dp_pre[i].append(tmp_str + ' ' + word)
        return [tmp[1:] for tmp in dp_pre[-1]]


if __name__ == "__main__":
    try1 = Solution()
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(try1.wordBreak(s, wordDict))
