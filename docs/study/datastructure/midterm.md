# Review of midterm exam

> No reflection, no progress.


## Datastructure

### AVL Tree

平衡因子：$ BF=|h(T\rightarrow l)-h(T\rightarrow r)|<2 $

高度为h的AVL树最小节点数关于h成Fib数列：

$ N(h) = N(h-1)+N(h-2)+1 ,N(0)=1,N(1)=2$

| 0 | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| 1 |2|3|5|8|

### Splay Tree

删除：先将要删除的节点splay到根节点，删除然后找接替节点，将接替节点splay到根节点。

### Amortized analysis

#### Aggregate

#### Credit

#### Potential function

### B+
#### 定义

A B+ tree of order M is a tree with the following structural properties:
(1)  The root is either a leaf or has between 2 and M children.
(2)  All nonleaf nodes (except the root) have between $\lceil M/2\rceil$ and M children.
(3)  All leaves are at the same depth.
Assume each nonroot leaf also has between $\lceil M/2 \rceil$ and M keys

<img src="\img\study\ADS\ds\Btorder3.png"  alt="">

<img src="\img\study\ADS\ds\Btorder4.png"  alt="">

#### 性质

设序为B的B+树有N个不同元素：

#### 操作

1. findkey: $O(Blog_BN)$节点内二分查找->$O(log_2B\cdot log_BN)=O(log_2N)$

2. insert: 叶子超标（多于B,也就是B+1）则分裂为$1到\lceil B/2 \rceil$和$\lceil B/2 \rceil+1到B+1$两部分
$O(Blog_BN)$

3. delete:
    - 若待删除键值所处节点内的键值数目多余 $\lceil B/2 \rceil$，直接删掉
    - 若待删除键值所处节点内的键值数目不超过 $ \lceil B/2 \rceil$，且相邻（左右）节点内键值超过$\lceil B/2 \rceil$，则直接从它拿一个
    - 若删除键值所处的节点内键值数目不超过$\lceil B/2 \rceil$，且相邻节点内键值不超过$\lceil B/2 \rceil$，则合并两节点：$\lceil B/2 \rceil-1 + \lceil B/2\rceil+ 1\leq B$
$O(Blog_BN)$


### Red and black tree

#### 定义

一棵红黑树是满足下面性质的二叉搜索树：

1. 每个结点或者是红色的，或者是黑色的；
2. 根结点是黑色的；
3. 每个叶结点（NIL）是黑色的；
4. 如果一个结点是红色的，那么它的两个子结点都是黑色的；
5. 对每个结点，从该结点到其所有

- 定义1：称 NIL 为外部结点，其余有键值的结点为内部结点。
- 定义2：从某个结点 X 出发到达一个叶子结点（NIL）的任意一条简单路径上的黑色结点个数（不含 X
本身）称为 X 的黑高，记为 bh(X)。根据定义第五条，这一定义是合理的，因为从 X 出发出发
到达一个叶子结点的任意一条简单路径上的黑色结点个数相同。除此之外，我们定义整棵红黑树
的黑高为其根结点的黑高。

- 性质：一棵有 n 个内部结点的红黑树的高度至多为 2 log(n + 1)

#### 插入
我们规定插入的节点一定是红色的（红黑对数据来说没有任何影响，只是维持平衡的一种方式）。

一共四种情况：

- 父节点是黑色直接插入
- 父、叔叔为红：把它们变黑，祖父变红，即把红色上推给上面节点，让它们来解决
![alt text](\img\study\ADS\ds\rbt1.png)
- 叔黑，插入为右孩子：
- 叔黑，插入为左孩子：
![alt text](\img\study\ADS\ds\rbt2.png)
<!-- 先把X旋转到夫亲或祖父位置，再染成黑色，X两个儿子染红色。 -->

#### 删除



## Leftist Heap

左式堆仍然满足堆序要求，这里以最小堆为例：每个节点父节点都比它自己大。

- leftist property: $ npl(u\rightarrow r)\leq npl(n\rightarrow l), npl(null)=-1 $ 一般的binary heap（二叉堆）天然满足左式性质，所以是左式堆。
- Lemma: 共有 N 个结点的左式堆的右路径最多含有$log(N + 1) $ 个结点。

### 基本操作

- Merge: $ O(logN) $
合并可以找两个堆中较小的那个然后分情况讨论，也可以让H1总是较小的那个（当它较大时就交换H1，H2）

```C
Merge(Lheap H1, H2):
    if(H1==NULL||H2==NULL){
        return Notnull(H1, H2)
    }else if(H1->val < H2->val){
        H1->r = Merge(H1->r, H2)
        if( npl(H->r) > npl(H->l) ){
            swap(H->r, H->l)
        }
            npl_update(H1)
            return H1
    }else{
        H2->r = Merge(H1, H2->r)
        if( npl(H2->r) > npl(H2->l) ){
            swap(H2->r, H2->l)
            npl_update(H2)
            return H2
        }
    }
```

- insert: $ O(logN) $
- deletemin: $ O(logN) $
- delete: $O (logN) $

## Skew heap

它是左式堆的自调整版本，不支持delete，decreasekey
区别在于合并部分:
base case: 当其中一个为空时，不直接返回另一个堆（我们这里不这样），而是将另一个堆中每个节点的左右孩子交换（除了最大节点，它没有子节点）。
other: H1->r = Merge(H1->r, H2) Swap(H1->r, H1->l)总是将合并好的右子树交换到左子树上。


Df: 定义堆中节点的轻重：
重：右子树节点个数大于等于左子树节点个数
轻：右子树节点个数小于左子树节点个数

>例：When merging two skew heaps H1 and H2, the number of light nodes along the right path of the resulting heap is not less than the sum of the number of heavy nodes along the right path of H1 and that of H2 [x]

### 均摊分析

Lemma:对于右路径上有 $l$ 个轻结点的斜堆，整个斜堆至少有 $2^l-1 $ 个结点，这意味着一个n 个结点的斜堆右路径上的轻结点个数为$ O(log n) $。
Theorem: 若我们有两个斜堆H1 和H2，它们分别有n1 和n2 个结点，则合并H1 和H2 的摊还时间复杂度为O(log n)，其中n = n1 + n2。

## Binomial heap

>二项堆的引入来源于我们希望**插入建堆**的操作有常数的平均时间，这一想法来源于二叉堆可以在O(n)时间内实现n 个结点的插入建堆操作，而之前讨论的左式堆和斜堆不可以。因此我们希望在保持合并的对数时间的条件下优化插入的时间复杂度。

### 定义

1. 结构性质：
    - a. 二项堆是由多棵二项树构成的森林
    - b. 二项堆中每棵二项树都有不同高度,$0,1,2,...,\lceil log_2(n+1)\rceil-1$，n为所有节点个数
    - c. 高度为0 的二项树是一棵单节点树；高度为k 的二项树 $B_k$ 通过将一棵二项树$B_{k−1}$ 附接到另一棵二项树$ B_{k−1} $的根上而构成。

2. 序性质：每棵二项数都保持堆序性。

示意图：

<img src="\img\study\ADS\ds\BinoTree.png"  alt="">

### 性质

- 1.高度为h的二项树节点数为 $2^{h} $。单节点高度定义为0；
- 2.高度为h的二项树在深度为d的节点数为 $ \binom{h}{d} $,数学归纳法：$ \binom{h}{d}+\binom{h}{d-1}=\binom{h+1}{d} $
- 由性质1及二项堆的定义b知，若一个二项堆有n个节点，那么n的二进制表示就可以说明这个二项堆里二项树的分布情况。


### 操作

1. FindMin: 若记录最小值$O(1)$，否则遍$O(log_2n)$棵树的根节点（这里用最小堆序）。
2. Merge: 整体结果可由二项堆的二进制表示相加得到，$O(logn)$
3. DeleteMin: $O(logn)$找到最小值，$O(1)$删除，删除后得到若干高度不同的子树，$O(logn)$合并
4. Insert: 等同于合并，最坏$O(logn)$(如二进制1+111每次都进位)，均摊$O(1)$

### 实现

Leftchild, next-sibling表示二项树，将不同高度的二项树的根节点储存在数组中，数组索引对应高度。


```C
typedef struct BinNode *Position;
typedef struct Collection *BinQueue;
typedef struct BinNode *BinTree;  /* missing from p.176 */
struct BinNode 
{ 
    ElementType  Element;
    Position    LeftChild;
    Position    NextSibling;
};
struct Collection 
{ 
    int CurrentSize;  /* total number of nodes */
    BinTree TheTrees[ MaxTrees ];
};

BinTree
CombineTrees( BinTree T1, BinTree T2 )
{  /* merge equal-sized T1 and T2 */
    if ( T1->Element > T2->Element )
        /* attach the larger one to the smaller one */
        return CombineTrees( T2, T1 );
    /* insert T2 to the front of the children list of T1 */
    T2->NextSibling = T1->LeftChild;
    T1->LeftChild = T2;
    return T1;
}

BinQueue  Merge( BinQueue H1, BinQueue H2 )
{   BinTree T1, T2, Carry = NULL;
    int i, j;
    if ( H1->CurrentSize + H2-> CurrentSize > Capacity )  ErrorMessage();
    H1->CurrentSize += H2-> CurrentSize;
    for ( i=0, j=1; j<= H1->CurrentSize; i++, j*=2 ) {
        T1 = H1->TheTrees[i]; T2 = H2->TheTrees[i]; /*current trees */
        switch( 4*!!Carry + 2*!!T2 + !!T1 ) { 
        case 0: /* 000 */
        case 1: /* 001 */  break;
        case 2: /* 010 */  H1->TheTrees[i] = T2; H2->TheTrees[i] = NULL; break;
        case 4: /* 100 */  H1->TheTrees[i] = Carry; Carry = NULL; break;
        case 3: /* 011 */  Carry = CombineTrees( T1, T2 );
                        H1->TheTrees[i] = H2->TheTrees[i] = NULL; break;
        case 5: /* 101 */  Carry = CombineTrees( T1, Carry );
                        H1->TheTrees[i] = NULL; break;
        case 6: /* 110 */  Carry = CombineTrees( T2, Carry );
                        H2->TheTrees[i] = NULL; break;
        case 7: /* 111 */  H1->TheTrees[i] = Carry; 
                        Carry = CombineTrees( T1, T2 ); 
                        H2->TheTrees[i] = NULL; break;
        } /* end switch */
    } /* end for-loop */
    return H1;
}

ElementType  DeleteMin( BinQueue H )
{   BinQueue DeletedQueue; 
    Position DeletedTree, OldRoot;
    ElementType MinItem = Infinity;  /* the minimum item to be returned */
    int i, j, MinTree; /* MinTree is the index of the tree with the minimum item */

    if ( IsEmpty( H ) )  {  PrintErrorMessage();  return –Infinity; }

    for ( i = 0; i < MaxTrees; i++) {  /* Step 1: find the minimum item */
        if( H->TheTrees[i] && H->TheTrees[i]->Element < MinItem ) { 
        MinItem = H->TheTrees[i]->Element;  MinTree = i;    } /* end if */
    }/* end for-i-loop */
    DeletedTree = H->TheTrees[ MinTree ];  
    H->TheTrees[ MinTree ] = NULL;   /* Step 2: remove the MinTree from H => H’ */ 
    OldRoot = DeletedTree;   /* Step 3.1: remove the root */ 
    DeletedTree = DeletedTree->LeftChild;   free(OldRoot);
    DeletedQueue = Initialize();   /* Step 3.2: create H” */ 
    DeletedQueue->CurrentSize = ( 1<<MinTree ) – 1;  /* 2MinTree – 1 */
    for ( j = MinTree – 1; j >= 0; j – – ) {  
        DeletedQueue->TheTrees[j] = DeletedTree;
        DeletedTree = DeletedTree->NextSibling;
        DeletedQueue->TheTrees[j]->NextSibling = NULL;
    } /* end for-j-loop */
    H->CurrentSize  – = DeletedQueue->CurrentSize + 1;
    H = Merge( H, DeletedQueue ); /* Step 4: merge H’ and H” */ 
    return MinItem;
}

```

## Fib heap


## 各种堆的时间复杂度

<img src="\img\study\ADS\ds\heaptime1.png"  alt=>

<img src="\img\study\ADS\ds\heaptime.png"  alt=>

<img src="\img\study\ADS\ds\heaptime2.png"  alt=>

<img src="\img\study\ADS\ds\heaptime3.png"  alt=>


## Reversed index(倒排索引)

 |  | relevant | irrelevant |
 |--| -------- | ---------- |
 | retrieved | a | b |
 | not retrieved| c |d |

Precision: $ \frac{a}{a+b}$
Recall: $ \frac{a}{a+c}$

什么是倒排索引：将词term映射到词所出现的文章。
For each term in the index, there is an associated list of documents (often called a posting list) where that term appears. This structure allows for efficient exact match queries (e.g., "Find all documents containing 'term1'").






