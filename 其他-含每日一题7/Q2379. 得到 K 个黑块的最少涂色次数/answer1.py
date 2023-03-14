# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 自己做，简单
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        rec = [0] * len(blocks)
        if blocks[0] == "B":
            rec[0] += 1
        for i in range(1, len(blocks)):
            rec[i] = rec[i - 1]
            rec[i] += 1 if blocks[i] == "B" else 0

        rec1 = rec.copy()
        for i in range(k, len(blocks)):
            rec1[i] = rec[i] - rec[i - k]

        return k - max(rec1)
