# Morris算法
# 该算法的时间复杂度也是O(N)，但是空间复杂度却能达到最优的O(1)

# 中序遍历，会改变树结构的方法
# https://zhuanlan.zhihu.com/p/89858150

# 中序遍历，不改变树结构，用到线索二叉树的知识
# https://zhuanlan.zhihu.com/p/89858150
# 前中后序：https://blog.csdn.net/yangfeisc/article/details/45673947

# 线索二叉树：
# 普通二叉树有n-1个指向空节点，浪费空间了
# 设定空左节点指向前驱节点，并设置ltag，表明指向前驱节点还是左节点
# 同样空右节点指向后驱节点，设置rtag



