# 一阶逻辑

## 谓词和量词


**论域**：所有被讨论对象的集合
**个体**：论域中的元素，即被讨论的对象

**常元**：用于表示确定对象的符号。例如，可
以用“ZS”表示个体“张三”。
**变元**：是用于表示给定论域上的任意一个对象的符号。例如，给定全总个体域，语句“𝑥 是学生”中，𝑥 是变元。
**函词**：给定一个论域，从一组个体到一个个体映
射关系可以用函词来描述。例如，用 𝑔(ZS) 表示“张三的哥哥”。其中，𝑔(𝑥) 是 𝑥 的函词，表示“𝑥 的哥哥”。

**项**：把个体常元和个体变元统称项。
**谓词**：用于描述个体之间的关系。


## 一阶语言

一阶语言包含七类符号：
个体常元：a b c
个体变元：x y z
函数符号：f g h
关系符号：F G H
量词符号：$\forall, \exist$
联结符号：$\lor, \land$等
标点符号：左括号，右括号，逗号

??? info "项"
    项可如下定义：
    (1) 变元和常元是项。
    (2) 如果 t1, . . . , t𝑚 是项，f 是 𝑚 元函数符号，则 f(t1, . . . , t𝑚) 是项。
    (3) 只有有限次使用 (1)(2) 条款生成的符号串才是项。


??? info "公式"
    公式可以定义如下：
    (1) F(t1, . . . , t𝑛) 是公式，称为原子公式。其中，F 是 𝑛 元关系符号，且 t1, . . . , t𝑛 是项。
    (2) 如果 t1 和 t2 是项，那么 (t1 ≡ t2) 是原子公式。
    (3) 如果 𝜙 和 𝜓 是公式，且 𝑥 是出现于 𝜙 中的自由变元，则 (¬𝜙)，(𝜙 ∧ 𝜓)，(𝜙 ∨ 𝜓)，(𝜙 → 𝜓), (𝜙 ↔ 𝜓)，(∀𝑥𝜙), (∃𝑥𝜙) 是公式。
    (4) 只有有限次使用 (1)(2)(3) 条款生成的符号串才是公式。

??? info "代换"
    代换 $\theta$ 是一个有限的对子集合 $\{x_1/t_1,\dots, x_n/t_n\}$，其中 $x_i$ 是变元，$t_i$ 是项。如果 $\phi$ 是一个公式，$\theta$ 是一个代换，则 $\phi\theta$ 是一个公式。在该公式中，所有 $x_i$ 的出现都被替换为 $t_i$。有时，我们也把 $\phi\{x/t\}$    作 $\phi^{x}_t$


## 语义

给定论域 𝐷，解释是一个映射，把个体符号映射为 𝐷 中的对象，把 𝑛 元函数符号映射为从 𝐷𝑛 到 𝐷 的函数，把 𝑛 元关系符号映射为 𝐷 上的 𝑛 元关系。
另一方面，对于每个自由变元，可以把论域中的对象指派给它。因此，指派也是一个映射。我们把解释和指派统称作赋值，记作𝑣。

??? info "解释/指派"
    给定论域 $D$，我们有：
    - 对于个体常元 a, 把它解释为的论域中的个体，记作 $v(a)\in D$。
    - 对于 𝑛 元函数符号 f, 把它解释为从 $D^n$ 到 𝐷 的函数，记作 $v(f): D^n\mapsto D$
    - 对于 𝑛 元谓词符号 F, 把它解释为 𝐷 上的 𝑛 元关系，记作 $v(F)\subset D^n$
    - 对于自由变元 x，给它指派 𝐷 中的个体，记作 𝑣(x) ∈ 𝐷。
    通常把 𝑣(a), 𝑣(f), 𝑣(F), 𝑣(x) 分别记作 $a^v,f^v, F^v,x^v$.


!!! info "项的值"
    一阶逻辑语言的项在以 $D$ 为论域的赋值 $v$ 下的值递归地定义如下：
    1. $a^v,x^v\in D$
    2. $f(t_1,\dots,t_n)=f^v(t_1^v,\dots,t_n^v)$.


为了定义公式在赋值之下的真假值，我们约定如下使用符号的规定。设 𝑣 是以 𝐷 为论域的赋值，a ∈ 𝐷, x 是自由变元符号。我们用 $v(x/a)$ 表示一个以 𝐷 为论域的赋值，它除了 $x^{v(x/a)}=a$ 之外，和 $v$ 完全相同。


!!! info "公式的真假值"
    - $F(t_1,\dots,t_n)=\begin{cases}
    1,& \text{if}(t_1^v,\cdots,t_n^v)\in F^v\\
    0, & \text{else}
    \end{cases}$
    - $(\neg \phi)^v=\begin{cases}
    1, & \text{if}\phi^v=0\\
    0, & \text{otherwise}
    \end{cases}$

    - $(t_1\equiv t_2)=\begin{cases}
    1,&\text{if}t_1^v, t_2^v \text{is the same in} D\\
    0,&\text{otherwise}
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

    - $\forall x\phi^v=\begin{cases}
    1,&\text{if}\phi^{v(x/a)}=1,\text{for any } a\in D\\
    0,&\text{otherwise}
    \end{cases}$

    - $\exist x\phi^v=\begin{cases}
    1,&\text{if exist } a\in D \text{ s.t. } \phi^{v(x/a)}=1,\\
    0,&\text{otherwise}
    \end{cases}$

### 逻辑推论

与命题逻辑对应，给定一组一阶公式集合 $\Phi$ 作为前提，我们希望知道 $\Phi$ 是否在逻辑上蕴涵某个结论 $\phi$。

!!! info "逻辑推论"
    设 $\Phi$ 是一组公式集合，$\phi$ 是一个公式。逻辑推论 $\Phi \models \phi$ 成立，当且仅当对于任意非空论域 $D$ 下的赋值 $v$，如果 $\Phi^v=1$ 则 $\phi^v=1$。

!!! info "可满足性与有效性"
    设 $\psi$ 是一个一阶公式
    - $\psi$ 是有效的，即 $\models \psi$ 当且仅当对于任意论域 $D$ 下任何赋值 $v,\psi^v=1$
    - $\psi$ 是可满足的，当且仅当存在某个论域 $D$ 下的赋值 $v$ 使 $\psi^v=1$




