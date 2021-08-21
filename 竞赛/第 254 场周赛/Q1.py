# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 5843. 作为子字符串出现在单词中的字符串数目
from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        mem = [[i, 0] for i in range(len(patterns))]
        count = [0] * len(patterns)
        for ch in word:
            for k in range(len(mem)):
                [i, idx] = mem[k]

                if patterns[i][0] == ch:
                    if len(patterns[i]) == 1:
                        count[i] = 1
                    else:
                        mem.append([i, 1])

                if idx == len(patterns[i]):
                    continue
                if patterns[i][idx] == ch:
                    mem[k][1] += 1
                    if mem[k][1] == len(patterns[i]):
                        count[i] = 1

        return sum(count)


if __name__ == "__main__":
    try1 = Solution()
    patterns2 = ["jksj", "cc"]
    word2 = "csfjksvqfdojsfrjhetnovaoigvgk"
    patterns1 = ["a", "abc", "bc", "d"]
    word1 = "abc"
    print(try1.numOfStrings(patterns2, word2))
