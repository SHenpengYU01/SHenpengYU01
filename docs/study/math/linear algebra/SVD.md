---
comments: true
tags :
  - Math
  - Linear Algebra
---
# SVD

## Introduction

SVD(singular value decomposition) is a mathematical method to process matrix. SVD can help extract the key traits of the number in a matrix. Apparently we can use it to process images because images are expressed as matries in computer science. This article is aimed to figure out why and how the SVD can extract the traits of the matrix. Plus I want to give several examples of its application in computere science.  

## SVD

### Start from one way to factorize matrix

Here is a matrix with $rank=1$:

$$
A=\begin{pmatrix}
  1&2&3 \\
  1&2&3
\end{pmatrix}
$$


It can be written as a column times a row:

$$
A=\begin{pmatrix}
  1&2&3 \\
  1&2&3
\end{pmatrix}=\begin{pmatrix}
  1 \\
  1
\end{pmatrix}\begin{pmatrix}
  1&2&3
\end{pmatrix}
$$

We can say the matrix is decomposed as a column times a row and more generally, for any matrix, it can be decomposed as the sum of $column \times row$ with different coefficients. A coefficient decides the weight of the specific $column \times row$ in the whole sum. Here is an example:

$$
A=\begin{pmatrix}
  a&0&0 \\
  0&b&0
\end{pmatrix}=a\begin{pmatrix}
  1 \\
  0
\end{pmatrix}\begin{pmatrix}
  1&0&0
\end{pmatrix}+b\begin{pmatrix}
  0 \\
  1
\end{pmatrix}\begin{pmatrix}
  0&1&0
\end{pmatrix}
$$

It can be formalised as

$$
A=\sigma_1{u_1}v_1^{T}+\sigma_2u_2v_2^{T}
$$

Here $a$($\sigma_1$) is the weight of the first $column \times row$ on the left and $b$($\sigma_2$) is the only other one. If $a$ is much more larger than $b$, we can neglect the second product to approximate $A$ as only one $column \times row$ with its coefficient. This is useful to store the matrix $A$ with less space.  

But where is the trait? Let's get it now:
$A$ is by $m\times n$, and suppose it has been decomposed as follow:

$$
A=\sigma_1{u_1}v_1^{T}+\sigma_2u_2v_2^{T}+\cdots+\sigma_n u_n v_n^{T} \tag{1}
$$

where $\sigma_1>\sigma_2>\cdots>\sigma_n$.

We can take in equation (1) in this way:
$\sigma_i$ is the weight, $u_i$ is the trait vector and $v_i^{T}$ is the combination vector who gives a matrix $A_i$ of $m \times n$ by $u_i v_i^{T}$, whose columns are the multiple of $u_i$ with their coefficients in $v_i^{T}$.

### SVD form

In matrix notation and more formalised, the former example could be written

$$
A=\begin{pmatrix}
  a&0&0 \\
  0&b&0
\end{pmatrix}=\begin{pmatrix}
  1&0 \\
  0&1
\end{pmatrix}\begin{pmatrix}
   a&0&0 \\
  0&b&0
\end{pmatrix}\begin{pmatrix}
  1&0&0 \\
  0&1&0 \\
  0&0&1
\end{pmatrix}
$$

In a general form of $A_{m\times n}$, the SVD wants to write $A$ as

$$
A=U\Sigma V^T \tag{2}
$$

$U_{m\times m}$ is called the left singular matrix with left singular vectors as its colomns and $V^{T}_{n\times n}$ is the right one. $\Sigma_{m\times n}$ has singular values $\sigma_i$ arranged in descending order in position $\Sigma_{ii}$  and zeros in other positions.  

Usually, $U$ and $V$ are orthogonal matrix. Therefore, $V^{-1}=V^{T}$, and multiply $V$ in both side of equation (2) we can get another form of it and it is where equation (2) comes from:

$$
AV=U\Sigma \tag{3}
$$

The idea is the same as that of diagonalising a real and symmetric square matrix with orthogonal matrix:

$$
A=Q\Lambda Q^T \Leftrightarrow AQ=Q\Lambda
$$

where $\Lambda$ is a diagonal matrix with eigen values of $A$ and $Q$ is the orthogonal matrix with corresponding orthonormal eigen vectors.  

Back to equation (3), rewrite it with specific vectors:

$$
A\begin{pmatrix}
v_1&v_2&\cdots &v_n
\end{pmatrix}=\begin{pmatrix}
u_1&u_2&\cdots &u_m
\end{pmatrix}\begin{pmatrix}
\sigma_1&0&\cdots &0 \\
0       &\sigma_2 &\cdots&0\\
\vdots &\vdots&\cdots&0
\end{pmatrix}_{m\times n}
$$

Suppose there are $\sigma_1$ to $\sigma_r$. Then we have

$$
Av_i=\sigma_i u_i, i=1,2,\cdots,r \tag{4}
$$

What we need to do is find these singular values $\sigma_i$ and corresponding sigular vectors $v_i$ and $u_i$, where $u_i$ can be given by $v_i$ and $\sigma_i$ with equation (4).  

Transpose both sides of equation (2):

$$
A^T=V\Sigma^T U^T
$$

Then multiply with $A$:

$$
AA^T=(U\Sigma V^T)(V\Sigma^T U^T)=U(\Sigma\Sigma^T)U^T \tag{5}
$$

$(\Sigma\Sigma^T)$ is a ${m\times m}$ matrix with $\sigma_1^2,\sigma_2^2,\cdots,\sigma_r^2$ and zeros on $(\Sigma\Sigma^T)_{ii}$ and zero otherwise. Therefore, $\sigma_i^2(i=1,2,...,r)$ are eigenvalues of $AA^T$, with $u_i$ being their corresponding eigenvectors.  
Similarly, we can also get $\sigma_i^2(i=1,2,...,r)$ are eigenvalues of $A^TA$, with $v_i$ being their corresponding eigenvectors.

- Conclusion:
Now let's summarize the whole process of SVD.  
Our aim is to write $A$ as $U\Sigma V^T$

## SVD application——PCA

PCA(principal component analysis) is a **dimensionality reduction** technique used in statistics and machine learning. It transforms a dataset with many correlated variables into a smaller set of uncorrelated variables called principal components, while preserving as much **variance** as possible.  
SVD is an effective way to implement PCA.

### A visulized example

Take $A_{m\times n}$ in this way: A set of $n$ **samples** with $m$ variables of **measurement**.
Here is an example from reference[1] listed last.  

Suppose we have $n$ different points in a 2-D plane and we want to find out the principal direction of these points, namely a line that will be as close as possible to the points.  

First, we center each of the measurement: $x,y$ in this example. Substract $\bar{x}$ and $\bar{y}$ for each $x_i$ and $y_i$. We can get a matrix $A_{2\times n}$ with each of its row having average of $0$.

We can draw these centered points in a coordinate. The center of these points is the origin. It helps a lot when we try to find the direction formed by these points.

<img src="\img\study\math\linear algebra\dian.png" alt=dian title="Data points in A are often close to a line in $R^2$ or a subspace in $R^m$">

Now consider doing SVD on $A$:

$$
A=U\Sigma V^T=\begin{pmatrix}
u_1&u_2
\end{pmatrix}\Sigma \begin{pmatrix}
v_1&v_2&\cdots&v_n
\end{pmatrix}^T
$$

The leading sigular vector with bigger sigular value shows the direction in the former scatter graph for the reasons we talk about above.  

#### Least perpendicular squares

Also this direction is the direction with **least perpendicular squares**.
>Namely, the sum of squared distances from the points to the line is a minimum.  

Proof: Consider a triangle formed by the origin, the line and the point $a_i$(a vector with$(x_i,y_i)$).  
Using Pythagorean theorem:
$$
||a_i||^2=|a_i^Tu_1|^2+|a_i^Tu_2|^2
$$

The first term on the right is the projection of $a_i$ on the direction of $u_1$(unit vector), namely the principal direction and the second term is the distance square we want. Sum all the distance squares:

$$
d_{sum}=\sum_{i=1}^{n}|a_i^Tu_2|^2=\sum_{i=1}^{n}||a_i||^2-\sum_{i=1}^{n}|a_i^Tu_1|^2
$$

The first term on the right is a constant for given points and the second term can be written as

$$
\sum_{i=1}^{n}|a_i^Tu_1|^2=\begin{pmatrix}
a_1^Tu_1&a_2^Tu_1\cdots&a_n^Tu_1
\end{pmatrix}\begin{pmatrix}
a_1^Tu_1\\
a_2^Tu_1\\
\vdots\\
a_n^Tu_1
\end{pmatrix}=u_1^TAA^Tu_1
$$

Minimise $d_{sum}$ means maximise $u_1^TAA^Tu_1$. Of course it arrives it maximum when $u_1$ is the singular vector for the maximum singular value. This cooresponds with the PCA by SVD.

### The general form


### Application in computer science

### Face recognition




## SVD——from the operator perspective

### Polar decomposition

$A=U\Sigma V^T=(UV^T) (V\Sigma V^T)=QS$

## References

- [1] Chapter 7 ***Introduction to linear algebra 5th*** by Gilbert Strang  
- [2] [Eigenface Wiki](https://en.wikipedia.org/wiki/Eigenface)
- [3] Chapter 7 ***Linear algebra done right 4th*** by Sheldon Axler
