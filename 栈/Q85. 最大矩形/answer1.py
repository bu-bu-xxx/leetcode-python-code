# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 做不了，矩阵没办法运算，除非用numpy包

# numpy矩阵用法
# import numpy
# array1 = numpy.array(matrix) # mat也行
# array1[0:1,0:1]返回一个矩阵
# array1[0,:]返回一个行向量
# array1[0,0]返回一个值
# np.arange = range对大数效率更高
# 不能用切片操作修改矩阵值
# array1[np.arange(0,2),0:3]=[[0,0,0],[0,0,0]]
# 一边用arange，一边用:可以切片修改矩阵数值
# 总的来说不好用

# 暴力算法
# matrix[行][列]
# 先扫描每一列，再扫描每一行，找出这一列连着的1，再横向扫描，得到长度

def matrix_find(matrix, hang_begin, hang_end, lie):
    temp = matrix[hang_begin:(hang_end + 1)]
    if len(temp) == 1:
        return temp[0][lie]
    else:
        ans = []
        for i in temp:
            ans.append(i[lie])
        return ans


def hengXiang(matrix, hang_begin, hang_end, lie):
    # 返回面积
    lie_begin, lie_end = lie, lie
    for j in range(lie, -1, -1):
        if not "0" in matrix_find(matrix, hang_begin, hang_end, j):
            lie_begin = j
        else:
            break
    for j in range(lie, len(matrix[0]), 1):
        if not '0' in matrix_find(matrix, hang_begin, hang_end, j):
            lie_end = j
        else:
            break
    return (hang_end - hang_begin + 1) * (lie_end - lie_begin + 1)


def maximal(matrix) -> int:
    if not matrix:
        return 0

    hang_len = len(matrix[0])  # 一行有多长
    lie_len = len(matrix)  # 一列有多长
    all_s = []
    for j in range(hang_len):
        find1 = 0
        hang_begin, hang_end = 0, 0
        for i in range(lie_len):
            if not find1 and matrix[i][j] == '1':  # 没找到1，当前是1
                hang_begin = i
                find1 = 1
            if find1 and matrix[i][j] == '1':  # 找到1，当前是1
                hang_end = i
            if find1 and (matrix[i][j] == '0' or i == lie_len - 1):  # 找到1，当前是0
                find1 = 0
                all_s.append(hengXiang(matrix, hang_begin, hang_end, j))

    if all_s:
        return max(all_s)
    else:
        return 0


class Solution:
    def maximalRectangle(self, matrix) -> int:
        a = maximal(matrix)
        if not matrix:
            return a
        else:
            lie_len = len(matrix)
            hang_len = len(matrix[0])
            matrixT = matrix
            for i in range(lie_len):
                for j in range(hang_len):
                    matrixT[j][i] = matrix[i][j]  # 转置，出错
            b = maximal(matrixT)
            return max(a, b)


if __name__ == '__main__':
    try1 = Solution()

    matrix = [["1", "0", "1", "0", "0"], \
              ["1", "0", "1", "1", "1"], \
              ["1", "1", "1", "1", "1"], \
              ["1", "0", "0", "1", "0"]]
    print(try1.maximalRectangle(matrix))
