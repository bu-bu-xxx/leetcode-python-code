# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 先读，算法导论-单源最短路径
#
# 树的一种定义(有向图)：
# 1.所有非根节点的节点有且只有一个根节点，指向根节点
# 2.这个图为连通图
#
# 等价定义：
# 1.是一个无回路图
# 2.所有其他节点到根节点有且仅有一条(不重复节点的)通路
#
# 引理：
# 1.经过初始化和任意次松弛计算，都会形成一棵树
# 2.如果对所有节点计算出d[v]=δ(s,v)，则先辈子图是以s为根的最短路径树
# 备注：最短路径树三个性质：1.连通 2.是树 3.最短路径
#
#
# Dijkstra 算法
# 条件：所有边权非负，w(u,v)>=0
# 算法：
# 1.Dijkstra算法中设置了一结点集合S，从源结点s到集合中结点的最终最短路径的权均
# 已确定，即对所有结点v∈S，有 d[v]=δ(s, v)
# 2.算法反复挑选出其最短路径怙计为最小的节点u∈V-S
# 把u插入集合S中，并对离开u的所有边进行松弛
# 备注：对于S中的点不需要再做松弛，因为已经是最短路径
"""
1. INITIALIZE-SINGLE-SOURCE(G* s)
2  S <- 空集
3  Q2043. 简易银行系统 <- V[G]
4. while Q2043. 简易银行系统!=空集
5.    do u <- EXTRACT-MIN(Q2043. 简易银行系统)
6.        S <- S|{ u }
7.        for 每个顶点 v ∈ Adj[u]-S
8.            do RELAX(u, v, w)
"""


# Bellman-Ford 算法
# 条件：边权可以为负
# 若G不包含从s可达且权为负的回路则算法返回TRUE，对所有结点v∈V有d[v]=δ(s,v)。否则返回False
# 算法：
"""
1. INITIALIZE—SINGLE-SOURCE(G, s)
2. for i=1 to |V[G]|-1
3.    do for 每条边(u, v)∈E[G]
          do RELAX(u, v, w)
5. for 每条边(u, v)∈E[G]
6.    do if d[v]> d[u]+w(u, v)
7.        then return FALSE
8. return TRUE
"""


# 其中的初始化函数和松弛函数
"""
INITIALIZE-SINGLE-SOURCE(G, s)
1. for 每个顶点 v∈[G]
2.    do d[v] <- ∞
3.       Π[v] <- NIL
4. d[s] <- 0

RELAX(u,v,w)    
1. if d[v] > d[u]+w(u, v)
2.    then d[v] <- d[u]+w(u，v)
3.       Π[v] <- u    
"""


# 有向无回路图中的单源最短路径
# 算法：
"""
DAG-SHORTEST-PATHS(G, w, s)
1. 对 G 的结点拓扑排序      
2. INITIALIZE-SINGLE-SOURCE(G, s)
3. for 拓扑序列中的每个结点 u
4.     do for 每个结点 v ∈ Adj[u]
5          do RELAX(u, v, w)
"""


# 解决毎对结点间的最短路径问题的一种递归方法
# W是边权值，D是最短路径


#  Floyd-Warshall 算法
# 设dij为从结点i到结点j且满足所有中间结点均属于集合{1,2,…，k}的一条最短路径的权
# 算法：
"""
Floyd-Warshall(W)
1 n <- rows[W]
2 D <- W
3 for k <- 1 to n
4     do for i <- 1 to n
5         do for j <- 1 to n
6             dij(k) = min( dij(k-1) , dik(k-1)+dkj(k-1) )
7 return D(n)
"""
# 对于路径发现
# 递归式
# Πij(k) = Πij(k-1) if dij(k-1) <= dik(k-1) + dkj(k-1)
#          Πkj(k-1) if dij(k-1) > dik(k-1) + dkj(k-1)
# 可以和上面合并
# 用到引理：最短路径的任意两个中间点，的中间路径，也是最短路径


# SPFA算法
# 是对Dijkstra算法的变形
# https://www.sohu.com/a/244179200_100201031
# 假设是无负环路的，对于负环路可以稍加修改，即可
# 算法过程：
# 用dis数组记录源点到有向图上任意一点距离，其中源点到自身距离为0，
# 到其他点距离为INF。将源点入队，并重复以下步骤：
#
# 1.队首x出队
# 2.遍历所有以队首为起点的有向边(x,i)，若dis[x]+w(x,i)<dis[i]，则更新dis[i]
# 3.如果点i不在当前队列，则i入队
# 4.若队列为空，跳出循环；否则执行1


