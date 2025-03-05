# 命题逻辑

## 命题与联结词

联结词：否定词（并非）、合取词（并且）、析取词（或）、蕴涵词（如果 . . . 那么 . . . ）
和等值词（当且仅当）
其中仅否定词为一元联结词，其他都是二元。


## 命题语言$\mathcal{L}^p$

1. 命题符号：
    - 永真命题：$\top$
    - 永假命题：$\bot$
2. 联结符号：$\neg, \lor, \land, \rightarrow, \leftrightarrow$
3. 标点符号：左、右括号

!!! info "定义：命题公式"
    命题公式，简称公式，可定义如下：
    (1) 命题符号是公式，称为原子公式。
    (2) 如果 𝜙 和 𝜓 是公式，那么 (¬𝜙), (𝜙 ∧ 𝜓), (𝜙 ∨ 𝜓), (𝜙 → 𝜓), (𝜙 ↔ 𝜓) 也是公式。
    (3) 只有有限次使用 (1) (2) 条款所组成的符号串是公式。
    或可用BNF形式表示如下：
    $$
    \phi::=p|(\neg \phi)|(\phi\land \phi)|(\phi\lor \phi)|(\phi\rightarrow \phi)|(\phi\leftrightarrow \phi)
    $$

任意的命题公式有且只有如下形式之一：𝑝，(¬𝜙)，(𝜙∧𝜓)，(𝜙∨𝜓)，(𝜙 → 𝜓)，(𝜙 ↔ 𝜓)。


## 语义
!!! info "定义：真假赋值"
    真假赋值是以所有命题符号的集为定义域，以真假值 ${1, 0}$ 为值域的函数。
    真假赋值 $v$ 给公式 $p$ 记为 $p^v$.

!!! info "定义：公式的真值"
    真假赋值 𝑣 给公式指派的真值递归地定义如下：
    - $p^v\in{1,0}$
    - $(\neg \phi)^v=\begin{cases}
    1, & \text{if}\phi^v=0\\
    0, & \text{otherwise}
    \end{cases}$

    - $(\phi \land \psi)^v =
    \begin{cases}
    1, & \text{if } \phi^v = \psi^v = 1 \\
    0, & \text{otherwise}
    \end{cases}$

    - $(\phi \lor \psi)^v =
    \begin{cases}
    1, & \text{if } \phi^v = 1 \text{ or } \psi^v = 1 \\
    0, & \text{otherwise}
    \end{cases}$

    - $(\phi \rightarrow \psi)^v =
    \begin{cases}
    1, & \text{if } \phi^v = 0 \text{ or } \psi^v = 1 \\
    0, & \text{otherwise}
    \end{cases}$

    - $(\phi \leftrightarrow \psi)^v =
    \begin{cases}
    1, & \text{if } \phi^v =\psi^v\\
    0, & \text{otherwise}
    \end{cases}$
    - $\top^v=1$
    - $\bot^v=0$

一个命题公式在任何真假赋值下均为真，称为重言式；一个命题公式在任何真假赋值下均为假，称为矛盾式；一个命题公式在某个真假赋值为真，称为可满足式。

## 逻辑推论

给定一组公式集合 $\Phi$ 作为前提，我们希望知道 $\Phi$ 是否在逻辑上蕴涵某个结论 $\phi$。如果对
于任何真假赋值 $v$, $\Phi^v=1$  总是蕴涵 $\phi^v=1$，那么我们说 $\phi$ 是 $\Phi$ 的逻辑推论，记作 $\Phi\models \phi$

则可进行如下定义：
给定一组命题公式集合 $\Phi$ 和一个命题公式 $\phi$，$\Phi\models\phi$ 当且仅当对于任意 $v$，如果 $\Phi^v=1$ ，那么 $\phi^v=1$

!!! info "定义：有效性"
    给定命题逻辑公式 𝜙，如果 $\models\phi$，我们说 𝜙 是有效的。

!!! note "定理1"
    ${\phi_1,\phi_2,\dots,\phi_n}\models\phi$ 当且仅当 $\models\phi_1\land\phi_2\land\cdots\phi_n\rightarrow\phi$

!!! note "定理2：有效性与可满足性"
    设 𝜙 是命题公式。那么，𝜙 是可满足的，当且仅当 ¬𝜙 不是有效的；𝜙 是有效的，当且仅当 ¬𝜙 不是可满足的。

!!! note "定理"
    Φ |= 𝜙，当且仅当：Φ ∪ {¬𝜙} 是不可满足的，即 Φ ∪ {¬𝜙} |= ⊥。

!!! info "定义：语义等价性"
    设 𝜙 和 𝜓 是命题公式。我们说 𝜙 和 𝜓 语义等价，记作 𝜙 |=| 𝜓，当且仅当 𝜙 |= 𝜓 并且𝜓 |= 𝜙。

!!! note "定理：等值替换"
    给定 𝜙 |=| 𝜓, 且 𝜙 是 𝜑 的一部分。把 𝜑 中的 𝜙 替换成 𝜓 到 𝜑′。我们有 𝜑 |=| 𝜑′。

语义等价关系满足自反性、对称性和传递性，即命题公式的语义等价关系是一种等价关系。

## 范式

!!! info "定义：合取范式"
    命题公式 𝜙 称为命题公式 𝜓 的合取范式，如果 𝜙 |=| 𝜓，且 𝜙 呈如下形式：
    $D_1\land\D_2\land\cdots\land D_m$
    其中，$D_i(i=1,2,\dots,m)$ 称为 $\phi$ 的子句，形如 $L_1\lor L_2\lor\codts\lor L_n。L_j$ 为原子公式或原子公式否定，称 $L_i$ 为子句的**文字**。

## 形式推演

## 消解原理

## 霍恩字句逻辑




