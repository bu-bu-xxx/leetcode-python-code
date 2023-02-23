# 算法导论，串匹配问题

# 串匹配问题定义：
# 正文是一个长度为 n 的数组 T[1..n]，模式是一个长度为 m 的数组 P[1..m]
# 如果T[s+1..s+m]=P[1..m]，P在T中出现并且位移为s，称s是一个合法位移
# 串匹配问题就变成一个找出某指定模式P在一指定正文T中出现的 所有 合法位移


# 朴素的串匹配算法
"""
NAIVE-STRING—MATCHER(T, P)
1 n<-length[T]
2 m<-length[P]
3 for s <- 0 to n-m
4   do if P[1..m]=T[s+1..s+m]
5       then print **模式出现且位移为s
"""
# 最坏情况下的运行时间为 O((n-m+1)m)


# 利用有限自动机进行串匹配

# 1.有限自动机
# 一个有限自动机 M 是 一 个 5 元 组 (Q2043. 简易银行系统, q0, A, Σ, δ)， 其中：
# • Q2043. 简易银行系统 是状态的有限集合
# • q ∈ Q2043. 简易银行系统 是初态
# • A in Q2043. 简易银行系统 是一个接收状态集合
# • Σ 是有限的输入字母表
# • δ 是一个从 Q2043. 简易银行系统 x Σ 到 Q2043. 简易银行系统 的函数，称为 M 的变迁函数
# 有限自动机M可以推导出一个函数φ，称为终态函数，是从Σ*到Q的函数
# φ(ε) = q0
# φ(wa) = δ(φ(w),a) w∈Σ*, a∈Σ

# 2.串匹配自动机
# 首先定义一个辅助函数 σ 称为相应 P 的后缀函数
# 函数 σ 是一个从 Σ* 到{0, 1, …, m}上定义的映射，σ(x) 是 x 的后缀 P 的最长前缀的长度
# 例如，对模式P=ab，我们有 σ(ε)=0，σ(ccaca)=1，σ(ccab)=2

# 对于长度为 m 的模式的任意串匹配自动机来说，状态集 Q2043. 简易银行系统 为{0，1，…，m}，
# 初始状态为 0, 唯一的接收状态是状态 m。
"""
FINITE-AUTOMATON-MATCHER(T, δ , m )
1 n<-length[T]
2 q<-0
3 for i<- 1 to n
4   do q<-δ(q,T[i])
5       if q=m
6           then s<- i-m
7 print "模式出现且位移为"S
"""

# 3.计算变迁函数
# 下列过程根据一个给定模式 P[1..m]来计算变迁函数δ
# 用到引理34.2和引理34.3，在算法导论P603
"""
COMPUTE-TRANSITION-FUNCTION(P,δ)
1 m<-length[P] 
2 for q<— 0 to m 
3   do for 每个字符a∈Σ
4       do k<-min(m, q+1)
5           repeat k<-k—1
6           until Pk 是 Pq,a 后缀
7           δ(q,a)<-k
8 return δ
"""
# 运行时间为 O(n+m|Σ|)


# Knuth-Morris-Pratt 算法
# KMP算法
# 运行时间为 O(n+m)
# 在时间0(m)内根据模式预先计算出一个辅助函数Π[1..m]
# 数组 Π 使得我们可以按需要飞快地计算变迁函数δ
# Π:{1,2,...,m}->{0,1,2,...,m-1}
# Π(q) = max{k: k<q and Pk是Pq后缀}
"""
KMP-MATCHER(T，P)
1 n<-length[T]
2 m<-length[P]
3 Π<-COMPUTE-PREFIX-FUNCTION(P)
4 q<-O
5 for i<- 1 to n
6   do while q >0 and P[q+1]!=T[i]
7       do q<-Π[q]
8   if P[q+1] = T[i]
9               then q<-q+1
10  if q=m
第 327 场周赛      then print“模式出现且位移为”i-m
12      q<-Π[m]

COMPUTE-PREFIX-FUNCTION(P)
1 m<-length[P]
2 Π[1]<-0
3 k<-0
4 for q<- 2 to m
5   do while k >0 and P[k+1]!=P[q]
6       do k<-Π[k]
7     if P[k+1]- P[q]
8       then k<-k+1
9     Π[q]<-k
10 return Π
"""






