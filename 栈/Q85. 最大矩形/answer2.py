# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 矩形化成柱状图
# 列出和matrix同样大小的矩阵，矩阵每个值代表左边同一行1的数量(包括自己的1)
# 分列数次数计算最大柱状图面积，变成Q84，answer3

def largestRectangleArea(heights) -> int:
    h_len = len(heights)
    stack = []
    record = []
    val = []
    for i in range(h_len):
        while stack and heights[i] <= heights[stack[-1]]:
            a = stack.pop()
            val.append((i - record[a] - 1) * heights[a])
        record.append(stack[-1] if stack else -1)
        stack.append(i)
    while stack:
        a = stack.pop()
        val.append((len(heights) - record[a] - 1) * heights[a])
    return max(val)


class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        i_len = len(matrix)
        j_len = len(matrix[0])
        matrix_left = ['a'] * i_len
        for i in range(i_len):
            tag1 = 0  # 标志前面连续的1的个数
            temp = [0] * j_len
            for j in range(j_len):
                if matrix[i][j] == '1':
                    tag1 += 1
                    temp[j] = tag1
                else:
                    tag1 = 0
                    temp[j] = 0
            matrix_left[i] = temp

        # 对每一列进行测试
        temp = [1] * i_len
        max_val = 0
        for j in range(j_len):
            for i in range(i_len):
                temp[i] = matrix_left[i][j]
            max_val = max(max_val, largestRectangleArea(temp))

        return max_val


if __name__ == '__main__':
    try1 = Solution()

    matrix = [["1", "0", "1", "0", "0"], \
              ["1", "0", "1", "1", "1"], \
              ["1", "1", "1", "1", "1"], \
              ["1", "0", "0", "1", "0"]]

    print(try1.maximalRectangle(matrix))
