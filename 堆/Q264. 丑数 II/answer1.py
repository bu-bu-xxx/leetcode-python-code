# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 动态规划，改进评论区的一种算法
# 也叫指针方法，maybe
# 分三个指针，计算下一个丑数

class Solution:
    def nthUglyNumber(self, n):
        a, b, c = 0, 0, 0
        stack = [1]
        A, B, C = 2 * stack[a], 3 * stack[b], 5 * stack[c]
        for _ in range(n - 1):
            stack.append(min_val := min(A, B, C))
            if A == min_val:
                a += 1
                A = 2 * stack[a]
            if B == min_val:
                b += 1
                B = 3 * stack[b]
            if C == min_val:
                c += 1
                C = 5 * stack[c]

        return stack[-1]


if __name__ == '__main__':
    try1 = Solution()

    n = 10
    print(try1.nthUglyNumber(n))
