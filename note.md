## $A^*$算法

本质上多了个启发函数，优化了Dijkstra算法和最佳优先搜索

<https://zhuanlan.zhihu.com/p/54510444>



LeetCode:

<https://leetcode-cn.com/problems/open-the-lock/solution/da-kai-zhuan-pan-suo-by-leetcode-solutio-l0xo/>



## $SSSP$问题

### Dijkstra 算法

```
先读，算法导论-单源最短路径

树的一种定义(有向图)：
1.所有非根节点的节点有且只有一个父节点节点，指向根节点
(根节点没有父节点)
2.这个图为连通图

等价定义：
1.是一个无回路图
2.所有其他节点到根节点有且仅有一条(不重复节点的)通路

引理：
1.经过初始化和任意次松弛计算，都会形成一棵树
2.如果对所有节点计算出d[v]=δ(s,v)，则先辈子图是以s为根的最短路径树
备注：最短路径树三个性质：1.连通 2.是树 3.最短路径


Dijkstra 算法
条件：所有边权非负，w(u,v)>=0
算法：
1.Dijkstra算法中设置了一结点集合S，从源结点s到集合中结点的最终最短路径的权均
已确定，即对所有结点v∈S，有 d[v]=δ(s, v)
2.算法反复挑选出其最短路径怙计为最小的节点u∈V-S
把u插入集合S中，并对离开u的所有边进行松弛
备注：对于S中的点不需要再做松弛，因为已经是最短路径
```

```
1. INITIALIZE-SINGLE-SOURCE(G* s)
2  S <- 空集
3  Q2043. 简易银行系统 <- V[G]
4. while Q2043. 简易银行系统!=空集
5.    do u <- EXTRACT-MIN(Q2043. 简易银行系统)
6.        S <- S|{ u }
7.        for 每个顶点 v ∈ Adj[u]-S
8.            do RELAX(u, v, w)
```



### Bellman-Ford 算法

```
Bellman-Ford 算法
条件：边权可以为负
若G不包含从s可达且权为负的回路则算法返回TRUE，对所有结点v∈V有d[v]=δ(s,v)。否则返回False
算法：
```

```
1. INITIALIZE—SINGLE-SOURCE(G, s)
2. for i=1 to |V[G]|-1
3.    do for 每条边(u, v)∈E[G]
          do RELAX(u, v, w)
5. for 每条边(u, v)∈E[G]
6.    do if d[v]> d[u]+w(u, v)
7.        then return FALSE
8. return TRUE
```

- 其中的初始化函数和松弛函数

```
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
```



### Floyd-Warshall 算法

```
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
```



### SPFA算法

```
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
```

## 一些函数及问题

### ASCII码——ord chr

```
ord(s)：获得字符 s 的 ASCII 值
chr(s)：获得数字 s 对应的字母
```

### 实例函数、类函数

类里面实例函数、类函数

@classmethod、静态函数@staticmethod的区别

<https://www.cnblogs.com/-xiaowu/p/4955888.html>



### collections 

```
# collections设置栈或者队列
# import collections
# collections.deque双端列表，头部插入与删除的时间复杂度为O(1)
# popleft,appendleft
# list(deque)还原变成list


# collections.Counter(xx)
# Counter()作为dict()的一个子类，可以求a['22'],a = collections.Counter()
# 输入列表，字符串，字典，将元素进行数量统计
# 计数后返回一个字典，键值为元素，值为元素个数
"""
str = "abcbcaccbbad"
li = ["a","b","c","a","b","b"]
print ("Counter(s):", Counter(str))
print ("Counter(li):", Counter(li))
Counter(s): Counter({'b': 4, 'c': 4, 'a': 3, 'd': 1})
Counter(li): Counter({'b': 3, 'a': 2, 'c': 1})
"""


# update
"""
d1 =Counter(str)
d1.update('123')
print(d1)
"""
# print增加了'123'，的字典


# 有序字典，defaultdict
"""
from collections import defaultdict
s=[('yellow',1),('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d=defaultdict(list)
for k, v in s:
    d[k].append(v)
a=sorted(d.items())
print(a)
"""
# 运行结果：
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
# 可填list，set，dict等，结果会存为该格式
# 空结果返回是None
```

### import自己写的包的方法

<https://zhuanlan.zhihu.com/p/63143493>

### lambda函数

```
# 以下写法等价
def add1(a, b, c):
    return a + b + c

add2 = lambda a, b, c: a + b + c
```

### nonlocal global

```
# global关键字修饰变量后标识该变量是全局变量，对该变量进行修改就是修改全局变量
# 而nonlocal关键字修饰变量后标识该变量是上一级函数中的局部变量
# 如果上一级函数中不存在该局部变量，nonlocal位置会发生错误

# nonlocal作用于上一层嵌套函数
# global作用于全局

"""
a = 1
def a1():
    a = 2
    def a2():
        nonlocal a
        a+=1
        print('a2',a)
    a2()
    print('a1', a)

a1()
print('a0',a)
"""
# 结果
"""
a2 3
a1 3
a0 1
"""
```

### numpy矩阵用法

```
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
```

### 注意事项

```
# 1.文件名不能取try

# 2.from xxx import *和import xxx的区别
# from xxx import *可以直接调用函数名  func()
# import xxx需要  xxx.func()

# 3.函数变量传递
# 如果变量是可变的，比如字典、数组等，函数里面改变这个变量值，主程序的这个变量会改变
# 如果变量是不可变的，比如字符串，则函数里修改这个变量，也不会改变主程序里面变量的值

# 4.递归函数return
# 递归函数满足条件需要一次return，每一次递归都需要一次return，否则会返回None
# 参考 堆/Q215/answer3
```

### raise try except else finally

<https://www.jb51.net/article/190680.htm>

```
"""
if 1:
    raise ValueError('123')
"""
# 上面的报错会停止运行，并输出报错


"""
try:
    if 1:
        raise ValueError
except ValueError: # 如果引发该ValueError异常，运行
    print('123455')
else: # 如果无异常，运行
	print('1233')
finally: # 无论是否异常都运行
	pass
	
print('2323')
"""
# 上面就会继续运行，try的作用
```

```
# try-except-else-finally

# try:运行出错则会运行except代码
# except( ):括号内输入报错原因，然后执行下面的语句
# else:其他报错原因
# finally:无论try是否出错都执行
# 记得加:
# try会到出错的时候停止，不执行错误语句，这时候可以查询错误语句的运行参数
```

### set集合的用法

<https://www.runoob.com/python3/python3-set.html>

```
# 集合是不重复的

# 运算符
# - 差集
# & 交集
# | 并集
# ^ 异或

# set([1]) or {1} 生成
# s.add( x ) 一个
# s.update( x ) 多个，元组、集合、列表都可以
# s.remove( x ) 会报错
# s.discard( x ) 不会报错
```

### sort sorted

```
# sorted
# sorted语法格式：  sorted(可迭代对象,key=函数名,reverse=False/True)
# 作用：从可迭代对象中，依次取出一个元素，该元素再按照key规定的排列依据排序。
# 可迭代对象：即可依次取值的对象，例如：集合，序列（列表，字符串，元组），字典等。
# key : 是列表排列的依据，一般可以自定义一个函数返回排序的依据，再把函数名绑定给key。
# reverse : 译为反转，reverse默认等于False，从小到大排序。等于True时，从大到小排序。
"""
不能用 d_order=sorted(d,key=lambda x:x[1],reverse=False)
要用 d_order=sorted(d.items(),key=lambda x:x[1],reverse=False)
"""


# sort
# 列表的L.sort()方法：  L.sort(key=函数名,reverse=False/True)
# L.sort()：会自动遍历列表中的元素，即依次取出一个元素。再以key绑定的函数为依据排序。
"""
L = list(dict_items([('a', 1), ('c', 3), ('b', 2)])
L.sort(key=lambda x:x[1],reverse=False)
"""
```

### unicode

查看文件编码格式

<https://www.cnblogs.com/skaarl/p/10159243.html>

```
"""
encode 和 decode
a = '中国'
b1 = a.encode('unicode-escape')
print(b1)
b2 = b1.decode('unicode-escape')
print(b2)

print(a.encode('gbk'))
print(a.encode('gbk').decode('gbk'))

# 我设置了默认utf-8编码
# 以下等价
print(a.encode('UTF8'))
print(a.encode('UTF-8'))
print(a.encode())
print(a.encode().decode())
"""
```

### pycharm快捷键

```
# Ctrl + q 快速查看当前函数帮助文档
# Ctrl + p 函数参数提示
# alt + enter 万能键，代码补全，import导入补全等等等
# Ctrl + shift + F10 运行当前页面的代码
```

### 文件和目录

- python遍历目录下的所有文件和目录详细介绍

<https://blog.csdn.net/sinat_29957455/article/details/82778306>

- python如何判断一个文件是否存在

<https://m.php.cn/article/420141.html>

 - python文件路径操作方法总结

目录名，文件名，拼接，等等

<https://www.jb51.net/article/202535.htm>

- python创建一个目录

一次只能创建一个目录，该目录已存在会报错

<https://www.cnblogs.com/mengqingjian/articles/9074077.html>

- python复制粘贴剪切文件

<https://zhidao.baidu.com/question/265498587.html>

```
"""
import shutil
print(help(shutil.copyfile))
print(help(shutil.copy))
print(help(shutil.move))
"""
```

### 字符串前缀

python中 r''	b''	u''	f'' 的含义

<https://blog.csdn.net/qq_35290785/article/details/90634344>

### 进制转换 进制运算

- 十进制转二进制：bin(10)
- 十进制转八进制：oct(10)
- 十进制转十六进制：hex(10)



- 二进制转十进制：int("1010",2)
- 八进制转十进制：int("12",8)
- 十六进制转十进制：int("ba",16)



**二进制位运算**

- 右移：105>>3
- 左移：1<<3

- 按位与：a&b
- 按位或：a|b
- 按位异或：a^b

### 元组 tuple

```python
# 表示元组
a = (1,)
a= tuple([1])

# 元组运算，相加
a = (1,)+(2,3)
a = tuple([1])+(2,3)
```



## tkinter python自带的gui

B站	<https://www.bilibili.com/video/BV1jW411Y7dL>

web	<https://www.runoob.com/python/python-gui-tkinter.html>

```
"""
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

# Label
var = tk.StringVar()
var0 = '123'
l1 = tk.Label(master=window, textvariable=var, font=('仿宋', 30), width=10, height=5)
l1.pack()
var.set('123')

# Entry
e = tk.Entry(window)

# Text
t = tk.Text(window, height=2)


# Button
def insert_point():
    str_var = e.get()
    t.insert('insert', str_var)
b1 = tk.Button(master=window, text='insert', width=5, height=5, command=insert_point)


# Frame
frm = tk.Frame(window)
frm.pack()
frm.pack()
frm_l = tk.Frame(frm)
frm_r = tk.Frame(frm)
frm_l.pack(side='left')
frm_r.pack(side='right')
tk.Label(frm_l, text='left').pack()
tk.Label(frm_r, text='right').pack()


# messagebox
# 必须 from tkinter import messagebox
def hit_me():
    messagebox.showerror(title='hi', message='error')
    messagebox.showwarning(title='hi', message='warning')
    messagebox.showinfo(title='hi', message='info')


tk.Button(window, text='hit me', command=hit_me).pack()

# pack
# e.pack()
# b1.pack()
# t.pack()

# mainloop
window.mainloop()
"""
```

## 堆（优先队列）

最小堆原理

<https://zhuanlan.zhihu.com/p/66418556>



代码

```
# 堆heapq模块
# 只支持最小堆，最大堆需要用相反数

# 模块heapq中一些重要的函数：
"""
heap = []:创建一个空堆
item = heap[0]:返回最小元素，但是不pop
heappush(heap, x):将x压入堆中
item = heappop(heap):从堆中弹出最小的元素
heapify(heap):把列表变成堆
item = heapreplace(heap, x):弹出最小的元素，并将x压入堆中
"""

# 阅读文档
import collections
print(collections.deque.__doc__)
```

## 正则表达式

<https://www.runoob.com/python/python-reg-expressions.html>

```
"""
import re
re.findall(r'xxxx',str)

*：0个或多个，+：1个或多个，？：0个或1个

re.findall(r'[A-Z]+|[a-z]+','HaHH')
['H', 'a', 'HH']
"""

# 找括号\( and \)

# 无括号返回list，list里面是str
# 有括号返回list，list里面是tuple，tuple里面是str
# 有括号则返回括号的内容，不返回括号外的内容
# 括号外面有个大括号，先返回大括号，再返回小括号，按左到右顺序

# a| b 匹配a或b
# (re) 对正则表达式分组并记住匹配的文本
# 加不加括号都是优先|，(a)(b)|(c)优先级等价于((a)(b))|(c)，后者比前者多输出一个

"""
例子：
# 或的两种写法，不等价
rst = re.findall(r'[a-z,A-Z,1,3,4]+',txt)
rst = re.findall(r'(a|b)',txt)

txt = 'aa11bb22cc33'
rst = re.findall(r'[a-z]+\d+',txt)
print(rst))

rst = re.findall(r'([a-z]+)(\d+)',txt)
print(rst))

rst = re.findall(r'(([a-z]+)(\d+))',txt)
print(rst))

运行结果：
result=['aa11', 'bb22', 'cc33']
result=[('aa', '11'), ('bb', '22'), ('cc', '33')]
result=[('aa11', 'aa', '11'), ('bb22', 'bb', '22'), ('cc33', 'cc', '33')]
"""
```

## 串匹配

```
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
11      then print“模式出现且位移为”i-m
12      q<-Π[m]

COMPUTE-PREFIX-FUNCTION(P)
1 m<-length[P]
2 Π[1]<-0
3 k<-0
4 for q<- 2 to m
5 	do while k >0 and P[k+1]!=P[q]
6   	do k<-Π[k]
7   if P[k+1] == P[q]
8       then k<-k+1
9   Π[q]<-k
10 return Π
"""
```

## Trie树 （字典树，前缀树）

- 原理

<https://zhuanlan.zhihu.com/p/340228499>

- 例题

<https://leetcode.cn/problems/implement-trie-prefix-tree/https://leetcode.cn/problems/implement-trie-prefix-tree/>

- 自写代码(python3)

```python
class Trie:

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False
    
    # 删除单词
    # 分4种情况,略

	# 插入单词
    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if node.children[ch] is None:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.is_end = True

	# 查找单词
    def search(self, word: str) -> bool:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if node.children[ch] is None:
                return False
            node = node.children[ch]
        return node.is_end
        
    # 查找单词前缀
    def startsWith(self, prefix: str) -> bool:
        node = self
        for ch in prefix:
            ch = ord(ch) - ord('a')
            if node.children[ch] is None:
                return False
            node = node.children[ch]
        return True
```

## 数论欧拉函数

欧拉函数：
$$
\phi(n)=\{(a,n)=1| \forall a<n\} \\
=n\sum_{p|n}(1-\frac{1}{p})
$$
欧拉公式：
$$
a^{\phi(n)}\equiv1 \quad (mod \   n) \\
(a,n) = 1,n可以为合数 \\
(注:\phi(n)不是最小的k， s.t.a^{k}\equiv1 \quad (mod \ n))
$$


证明：



<https://zhuanlan.zhihu.com/p/56548135>



## 调和级数求和估计

<https://wenku.baidu.com/view/0002eac0514de518964bcf84b9d528ea81c72faa.html?_wkts_=1673689166203&bdQuery=%E8%B0%83%E5%92%8C%E7%BA%A7%E6%95%B0%E6%B1%82%E5%92%8C>
$$
\frac{1}{x}<\int_{x-1}^{x}\frac{1}{t}dt<\frac{1}{x-1} \\
\frac{1}{x}<ln\frac{x}{x-1}<\frac{1}{x-1} \\
ln\frac{x+1}{x}<\frac{1}{x}<ln\frac{x}{x-1}
$$
可得，
$$
ln(n+1)<\sum^{n}_{i=1}\frac{1}{i}<1+ln(n)
$$
且调和级数$\sum^{n}_{i=1}\frac{1}{i}-ln(n)$有极限，

即
$$
\sum^{n}_{i=1}\frac{1}{i}=ln(n)+\gamma
$$
其中$\gamma$为欧拉常数，$\gamma=0.5772156\cdots$



## 数论二次剩余

* 二次剩余、勒让德符号、欧拉准则

<https://zhuanlan.zhihu.com/p/166123245>
$$
n \equiv x^2\quad (mod \ m)
$$
$m \nmid n$，如果上面方程有非零解，称$n$是模$m$的二次剩余

如果没有非零解，称$n$是模$m$的非二次剩余



勒让德符号：
$$
(\frac{a}{p})= \begin{cases}
0  & if \ a \equiv 0  \ (mod \ p) \\
1  & if 存在\ a \equiv x^2 \ (mod \ p) \\
-1 & if 不存在 \ a \equiv x^2\ (mod \ p)
\end{cases}
$$
一般讨论$p$为素数



欧拉准则：
$$
(\frac{a}{p}) \equiv a^{\frac{p-1}{2}} \quad (mod\ p)
$$


* 二次互反律

<https://zhuanlan.zhihu.com/p/240289380>

数学天书上有几种证明
$$
(\frac{p}{q}\cdot \frac{q}{p})=(-1)^{\frac{p-1}{2}
\cdot\frac{q-1}{2}} \\
其中p，q为不相等的素数
$$

* 升幂定理

<https://zhuanlan.zhihu.com/p/106900309>



## 树最大路径和

- 先求父节点到子节点的最大路径和，路径和为左最大路径+节点值+右最大路径，用dfs递归搜索

- <https://leetcode.cn/problems/binary-tree-maximum-path-sum/solution/er-cha-shu-zhong-de-zui-da-lu-jing-he-by-leetcode-/>
- <https://leetcode.cn/problems/difference-between-maximum-and-minimum-price-sum/solution/by-endlesscheng-5l70/>







