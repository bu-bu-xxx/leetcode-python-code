# encoding:UTF-8
# @Author :ZQY
# edition :Python3.8


# 暴力算法

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)
import bisect


class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.rec = []

    def seat(self) -> int:
        if len(self.rec) == 0:
            self.rec.append(0)
            return 0
        else:
            length = self.rec[0] - 0
            index = 0
            for i in range(1, len(self.rec)):
                if (tmp := (self.rec[i] - self.rec[i - 1]) // 2) > length:
                    length = tmp
                    index = self.rec[i - 1] + tmp
            if (self.n - 1 - self.rec[-1]) > length:
                length = self.n - 1 - self.rec[-1]
                index = self.n - 1
            tmp = bisect.bisect_right(self.rec, index)
            self.rec = self.rec[0:tmp] + [index] + self.rec[tmp:]
            return index

    def leave(self, p: int) -> None:
        tmp = bisect.bisect_left(self.rec, p)
        self.rec = self.rec[0:tmp] + self.rec[tmp + 1:]
