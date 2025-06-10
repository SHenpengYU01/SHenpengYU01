# 知识图谱与描述逻辑

## 语义网络与知识图谱


!!! info "语义网络"
    语义网络是一个图，其节点表示对象或概念，边表示这些对象或概念之间的关系。


知识图谱是一种语义网络，用于描述现实世界中的各种实体及其关系。与语义网络一样，知识图谱由如下三种成分构成：节点、边和标签。


## 本体与描述逻辑

TBOX（术语框）：含用于描述概念层次的句子，
ABOX（断言框）：含基句子，阐述个体属于层次的哪个地方。
例如：“每个员工都是人”属于 Tbox，而“Bob 是一位员工”属于 ABox。

本体是一种统一的术语体系，可支持知识共享，通常有三部分组成：关于事物分类的词汇表，分类的组织，一组公理集合。（用于限制一些符号的定义）

- 描述逻辑中的三种实体：
  - 概念：个体的集合，可视为一元谓词
  - 角色：个体之间的二元关系，可视为二元谓词
  - 个体名称：一个领域中的单个个体，可视为常元。


本体不能完全描述特定的 “情况” 或 “世界的状态”，而是由一系列句子（称为公理）组成。每个公理都必须在所描述的情况下为真。公理分为三类：断言型（ABox）公理，术语型（TBox）公理和关系型（RBox）公理。

- 用 ABox 公理断言事实： ABox 公理可以刻画关于命名个体的知识，即它们所属的概念以及它们相互之间的关系。
最常见的 ABox 公理是概念断言，如 Mother(julia)，角色断言：parentOf(julia, john)
- 用 TBox 公理表达术语知识： TBox 公理描述概念之间的关系。例如，“所有母亲都是父母”这个事实可以用概念包含表示如下：
Mother $\sqsubseteq$ Parent
- 用 RBox 公理建模角色之间的关系： RBox 公理是关于角色的特性的。关于概念，描述逻辑支持决策包含公理和角色等价公理。
parentOf $\sqsubseteq$ ancestorOf 公理表示parentOf 是 ancestorOf 的子角色，
即由parentOf 关联的每队个体也是由 ancestorOf 关联的个体。


### 概念和角色的构造算子

- **布尔概念构造算子**： 布尔概念构造算子提供了基本的布尔运算，这些运算与人们熟悉的集合的交集、并集和补集运算，或者与逻辑表达式的合取、析取和否定运算密切相关。

Female ⊓ Parent，Mother ≡ Female ⊓ Parent，Parent ≡ Father ⊔ Mother

- **角色限制**：

父母是至少一个人的父母：Parent ≡ ∃parentOf.⊤
它描述了这样的个体集合：其中的每个个体都是至少一位个体（⊤ 的实例）的父母。
∃parentOf.Female 这个概念描述了那些至少有一个女性的父母，即那些有女儿的人
(∃parentOf.⊤) ⊓ (∀parentOf.Female) ：描述至少有一个孩子并且所有孩子都是女性的个体。


### 描述逻辑的语法

形式上，每个描述逻辑本体都基于三组有穷的符号集合：$N_C, N_R, N_O$，它们分别表示概念名集合、角色名集合和个体名集合。
这样，三元组 $(N_C, N_R, N_O)$ 构成描述逻辑的名字表。

描述逻辑 ALC (ABox Logic)的概念定义如下：

!!! info "$mathcal{ALC}$"
    $\mathcal{ALC}$ 概念集合是满足如下条件的极小集合：

    - $\top, \bot$ 是概念
    
    - $A\in N_C$：每个原子概念是概念
    
    - 如果C和D是概念，且 $R\in N_R$ 是角色名，那么如下是概念：
      
      - $C\sqcap D, C\sqcup D, \neg C$ ：概念的交并补是概念
      
      - $\forall R.C$：一个角色对一个概念的全称约束是一个概念
      
      - $\exist R.C$：由一个角色对一个概念的存在约束是一个概念


!!! info "术语公理"
    普通概念包含形如 𝐶 ⊑ 𝐷，其中 𝐶 和 𝐷 是概念。当 𝐶 ⊑ 𝐷 且 𝐷 ⊑ 𝐶 时，记作 𝐶 ≡ 𝐷。

TBox是一组术语公理的有穷集合。TBox $ \mathcal{T}$ 和它的扩张 $ \mathcal{T}'$ 是等价的。 $\mathcal{T}$ 的扩张是将其定义中的的每个名称替换为该名称所代表的概念。相当于是做代换直到不能代换为止。

!!! info "断言公理"

    - 概念断言是一个形如 $a: C$ 的句子，其中 $a\in N_O$, C是一个概念。

    - 角色断言是一个形如 $(a,b) : R$ 的句子，其中 $a, b\in N_O$，R是一个角色。

    - ABox 是一组断言公理的有穷集合。


!!! info "知识库"
    在描述逻辑中，一个知识库是一个有序对 $(\mathcal{T}, \mathcal{A})$。其中 $\mathcal{T}, \mathcal{A}$
    分别是 TBox 和 ABox

### 描述逻辑的语义

描述逻辑的语义通过如下方式定义：把概念解释为个体的集合，而把角色解释为个体有序对的集合。

一个解释 $\mathcal{I}$ 由一个称为 $\mathcal{I}$ 的域的集合 $\Delta^\mathcal{I}$ 和一个解释函数
$·^\mathcal{I}$ 组成，该函数将每个原子概念映射到一个集合 $A^\mathcal{I} \subset \Delta^\mathcal{I}$，
将每个原子角色R映射到二元关系 $R^\mathcal{I}\subset \Delta^\mathcal{I} \times \Delta^\mathcal{I}$，
将每个个体名称映射到一个元素 $a^\mathcal{I} \in \Delta^\mathcal{I}$

!!! info "概念的解释"
    给定名字表 $(𝑁_𝐶, 𝑁_𝑅, 𝑁_𝑂)$，相应的术语解释定义为 $I = (\Delta^\mathcal{I}, ·^\mathcal{I})$。其中，

    - 非空集合 $\Delta^\mathcal{I}$ 称为论域。

    - 解释函数 $·^I$ 包括如下映射：

      - 把每个个体a映射为元素 $a^\mathcal{I} \in \Delta^\mathcal{I}$

      - 把每个概念映射为 $\Delta^\mathcal{I}$ 的子集

      - 把每个原子角色映射为 $\Delta^\mathcal{I} \times \Delta^\mathcal{I}$ 子集，使得

      - $\top^I=\Delta^\mathcal{I}$

      - $\bot^I=\emptyset$

      - $(C\sqcup D)^I = C^I\cup D^I$

      - $(C\sqcap D)^I = C^I\cap D^I$

      - $(\neg C)^I = \Delta^\mathcal{I}\backslash C^I$

      - $(\forall R.C)^I = \{x\in \Delta^\mathcal{I} | \forall y \text{,如果} (x,y)\in R^I，\text{则} y\in C^I\}$

      - $(\exist R.C)^I = \{x\in \Delta^\mathcal{I} | \exist y\in \Delta^I : (x,y)\in R^I，y\in C^I\}$

## 描述逻辑的推理

设 $\mathcal{T}$ 是一个 TBox。形式化地，有如下定义：

!!! info "可满足"
    概念C是关于 $\mathcal{T}$ 可满足的，如果存在 $\mathcal{T}$ 的一个解释 $\mathcal{I}$ ，使得 $C^I$ 非空。

!!! info "包含"
    关于 $\mathcal{T}$ ，我们说概念C是被包含于D，如果对于$\mathcal{T}$ 的每个解释 $\mathcal{I}，C^I \subseteq D^I$ 成立，
    记作 $\mathcal{T} \models C\sqsubseteq D$。

!!! info "等价"
    我们说概念C与D关于 $\mathcal{T}$ 等价，如果对于 $\mathcal{T}$ 的每个解释 $\mathcal{I}，C^I=D^I$，记作 $\mathcal{T}\models C\equiv D$

!!! info "不相交"
    我们说概念C与D关于 $\mathcal{T}$ 不相交，如果对于 $\mathcal{T}$ 的每个解释 $\mathcal{I} ，C^I\cap D^I=\emptyset$

包含、等价和不相交三种概念可以被规约到可满足问题。

!!! note "定理"
    对于概念C和D，我们有：

    (1) C 被 D 包含，当且仅当 $C\sqcap \neg D$ 不可满足。

    (2) C 与 D 等价，当且仅当 $C\sqcap \neg D, \neg C \sqcap D$ 都不可满足

    (3) C与 D 不相交，当且仅当 $C\sqcup D$ 不可满足


### ALC表算法

#### 关于判断ALC概念可满足性的算法

<img src="\img\study\ai\ailogic\NNF.png" alt="ALC表算法">

!!! info "ABox的冲突性和完全性"
    我们称一个ABox $\mathcal{A}$ 包含冲突，如果存在个体名 a 以及概念C使得 $\{a:C,a:\neg C\} \subseteq \mathcal{A}$，或者 $\bot\subseteq \mathcal{A}$。
    如果 $\mathcal{A}$ 不包含冲突，我们就称其为无冲突的。我们称 $\mathcal{A}$ 是完全的，如果它包含冲突，或者没有一个扩张是可应用的。



!!! info "表转换规则"
    \mathcal{A} 是一个ABox。表转换规则包括：

    - ⊓ 规则：如果 𝑥:(𝐶⊓𝐷) ∈ A，而且 {𝑥:𝐶, 𝑥:𝐷} ⊈ A，那么 A′ = A∪{𝑥 : 𝐶, 𝑥 : 𝐷}

    - ⊔ 规则：如果 𝑥 : (𝐶 ⊔ 𝐷) ∈ A，而且 {𝑥:𝐶, 𝑥:𝐷}∩A = ∅，那么 A′ = A ∪ {𝑥 : 𝐶)},A′′= A ∪ {𝑥 : 𝐷}。
    
    - ∃ 规则：如果 𝑥 : ∃𝑅.𝐶 ∈ A，而且不存在 𝑧 使得 𝑧 : 𝐶 ∈ A 且 (𝑥, 𝑧) : 𝑅 ∈ A，则对于一个新的个体 𝑦 ∉ A, A′ = A ∪ {𝑦 : 𝐶, (𝑥, 𝑦) : 𝑅}

    - ∀ 规则：如果 𝑥 : ∀𝑅.𝐶 ∈ A 而且 (𝑥, 𝑦) : 𝑅 ∈ A，但 𝑦 : 𝐶 ∉ A，则 A′ = A ∪ {𝑦 : 𝐶}

例：判断 (Professor ⊑ (Person⊓UniversityEmployee) ⊔ (Person⊓ ¬Student)) ⊓ (¬(Professor ⊑ Person)) 的可满足性。

令 \(\mathcal{A}_0 = \{x : ((\neg\text{Professor} \sqcup (\text{Person} \sqcap \text{UniversityEmployee}) \sqcup (\text{Person} \sqcap \neg\text{Student})) \sqcap \text{Professor} \sqcap \neg\text{Person}\}\)。  
证明过程如下：

1. 由 \(\mathcal{A}_0\) 和 \(\sqcap\) 规则，\(x : \text{Professor}\)  
2. 由 \(\mathcal{A}_0\) 和 \(\sqcap\) 规则，\(x : \neg\text{Person}\)  
3. 由 \(\mathcal{A}_0\) 和 \(\sqcap\) 规则，\(x : (\neg\text{Professor} \sqcup (\text{Person} \sqcap \text{UniversityEmployee}) \sqcup (\text{Person} \sqcap \neg\text{Student}))\)  
   3.1. 由 3 和 \(\sqcup\) 规则，\(x : \neg\text{Professor}\)（包含冲突）  
   3.2. 由 3 和 \(\sqcup\) 规则，\(x : ((\text{Person} \sqcap \text{UniversityEmployee}) \sqcup (\text{Person} \sqcap \neg\text{Student}))\)  
      - 3.2.1. 由 3.2 和 \(\sqcup\) 规则，\(x : (\text{Person} \sqcap \text{UniversityEmployee})\)  
          - 3.2.1.1. 由 3.2.1 和 \(\sqcap\) 规则，\(x : \text{Person}\)（包含冲突）  
          - 3.2.1.2. 由 3.2.1 和 \(\sqcap\) 规则，\(x : \text{UniversityEmployee}\)  
      - 3.2.2. 由 3.2 和 \(\sqcup\) 规则，\(x : (\text{Person} \sqcap \neg\text{Student})\)  
          - 3.2.2.1. 由 3.2.2 和 \(\sqcap\) 规则，\(x : \text{Person}\)（包含冲突）  
          - 3.2.2.2. 由 3.2.2 和 \(\sqcap\) 规则，\(x : \neg\text{Student}\)  

由于所有分支都包含冲突，因此 \(\mathcal{A}_0\) 不可满足。

#### 涉及普通包含公理的ABox一致性检查算法

上一节介绍的算法适合于 TBox 为空的情况。当 TBox 为非空的时，如果该 TBox 是无环的，那么可以通过扩张去掉 TBox。
然而，当 TBox 包含形如 𝐶 ⊆ 𝐷 的普通包含公理时，这种扩张变得不再可行。对于存在多条普通包含公理（𝐶1 ⊑ 𝐷1,..., 𝐶𝑛 ⊑ 𝐷𝑛）的情况，
只要考虑一条公理 ⊤ ⊑ E，其中

$$
E=(\neg C_1 \sqcup D_1)\sqcap \dots \sqcap (\neg C_n\sqcup D_n)
$$

公理 ⊤ ⊑ E 意指任何个体都必须属于 E。
可以通过简单修改上述表算法来纳入这个公理：所有个体（包括原有的个体义记由存在
规则和全称规则新产生的个体）都被断言属于 E。但是会导致算法不可终止：通过检测循环阻止**存在规则**的实施。

