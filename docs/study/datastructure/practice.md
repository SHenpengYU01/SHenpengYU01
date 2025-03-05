# problems


## 数据结构

### 树


>For an AVL tree, the balance factors of all the non-leaf nodes are 0 iff the tree is a complete binary tree. [F] perfect

### 堆

>For a binomial queue, delete-min takes a constant time on average.[F]

amortized cost O(1)

>For a skew heap with N nodes, the worst-case running time of all operations (insert/delete min/merge) is O(N) [T]

>Skew heaps have O(logN) worst-case cost for merging [F]

worse:O(n)两棵斜树合并

>Recall that the worst-case time complexities of insertions and deletions in a heap of size N are both O(logN). Then, without changing the data structure, the amortized time complexity of insertions in a heap is also O(logN), and that of deletions is O(1). [T]

>Insert { 1, 2, 5, 3, 8, 4, -1, 10, 128, 34, 15, 63, 18, -24, 186 } into an initially empty binomial queue, the resulting roots are 186, -24, 15 and -1. [T]

8+4+2+1
1 2 5 3 8 4 -1 10|128 34 15 63|18 -24|186


### amortized analysis

>Recall the amortized analysis for Splay Tree and Leftist Heap, from which we can conclude that the amortized cost (time) is never less than the average cost (time). [T]

### Inverted index

>While accessing a term by hashing in an inverted file index, range searches are expensive. [T]

范围搜索比如找出"apple"和"banana"间所有单词对应文章，哈希表只能逐个单词查询，因为它没有表示范围的概念，它的单词是无序存储的，只是对某个词的O(1)快速访问。

## 算法

### external sort
>To merge 55 runs using 3 tapes for a 2-way merge, the original distribution (34, 21) is better than (27, 28). [T]

让run的大小为Fibonacci数

>In external sorting, a k-way merging is usually used in order to reduce the number of passes and we will take the k as large as possible as long as we have enough amount of tapes. [F]

并不是磁带越多越好，k路合并时应当将整个内存区域划分成 2k 个输入缓存区合 2 个输出缓存区，这样当 k 很大的时候，我们的输入缓存就会被划分得很细，一次能读入输入缓存的数据量就会减小（也就是 block 大小降低），那么我们的 I/O 操作就会变多。

### Greedy

>Let S be the set of activities in Activity Selection Problem.  Then the earliest finish activity a must be included in all the maximum-size subset of mutually compatible activities of S [F]

必定在某个最大活动子集中，不是所有都包含它。


### NP
>The decision problem HALTING returns TRUE, if, for a given input I and a given (deterministic) algorithm A, A terminates, otherwise it loops forever. The HALTING problem is NP-complete. [F]

HALTIING问题是不可多项式时间判定问题，即对于任意输入，它不能在有限多项式时间内通过任何算法得出结果。相反，NP-complete 问题是可判定的，所有NP问题都是可判定的。


### random

>Reviewing the randomized QuickSort in our course, we always select a central splitter as a pivot before recursions, make sure that each side contains at least n/4 elements. However, as the same as the deterministic QuickSort, the worst case running time of the randomized QuickSort is still O(N^2) [F]


### approxiamtion

>1.Suppose ALG is an α-approximation algorithm for an optimization problem Π whose approximation ratio is tight. Then for every ϵ>0 there is no (α−ϵ)-approximation algorithm for Π unless P = NP.[F]

对于一些特例还是有更进一步的近似算法的

>2.Let Aand B be optimization problems where it is known that A reduces to B in polynomial time. Additionally, suppose that there exists a polynomial-time 2-approximation for B. Then there must exist a polynomial time 2-approximation for A. [F]

approximation factor is not (necessarily) carried over in polytime reduction. See e.g. set cover vs. vertex cover.

>3.A randomized algorithm for a decision problem with one-sided-error and correctness probability 1/3 (that is, if the answer is YES, it will always outputYES, while if the answer is NO, it will output NO with probability 1/3) can alwaysbe amplified to a correctness probability of 99%. [T]


<img src="\img\study\ADS\problem\solution1.png" alt="Solution1">


>4.Suppose that you have two deterministic online algorithms, A1 andA2, with a competitive ratios(approximation ratio for online algorithm) c1 and c2 respectively. Consider the randomized algorithm A∗ that flips a fair coin once at the beginning; if the coin comes up heads, it runs A1 from then on; if the coin comes up tails, it runs A2 from then on. Then the expected competitive ratio of A∗ is at least min{c1, c2}.


<img src="\img\study\ADS\problem\solution2.png" alt="Solution2">


### parallel

>To solve the Maximum Finding problem with parallel Random Sampling method, T(n)=O(1) and W(n)=O(n) can be achieved with O(n) processors. [F]

with high probability not 100 percent sure

### Local search

>For an optimization problem, given a neighborhood, if its local optimum is also a global optimum, one can reach an optimal solution with just one step of local improvements. [F]




