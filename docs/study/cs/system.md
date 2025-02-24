# Computer System

## Quantitative approaches

$CPU Time=IC\times CPI\times Clock Pereiod$

$CPU Time=\frac{Instructions}{program}\times \frac{clock cycles}{Instruction}\times \frac{Seconds}{Clock cycle}$

IC: instruction count

- If different instruction classes take different numbers of cycles:

Clock Cycles=$\sum_{i=1}^{n}(CPI_i\times IC_i)$

CPI=$\frac{Clock Cycles}{IC}=\sum_{i=1}{n}(CPI_i\times \frac{IC_i}{IC}$

### Principles of computer design

- Use parallelism: multiple processors, disks, memmory banks, pipelining

- Principle of Locality: reuse data and instructions

- Focus on the common case: Amdahl's Law

**Amdahl's Law**:
$T_{improved}=\frac{T_{affected}{improvement factor}+T_{unaffected}$

$Fraction_{enhanced}$ :proportion of segment can be enhanced

$$
Execution time_{new}=Exe time_{can't be enhanced}+Ece time_{enhanced}
$$

$$
=Execution time_{old}((1-Fraction_{enhanced})+\frac{Fraction_{enhanced}{Speedup_{enhanced}}})
$$

$$
Speedup_{overall}=\frac{Exe time_{old}}{Exe time_{new}}=\frac{1}{(1-Fraction_{enhanced})+\frac{Fraction_{enhanced}{Speedup_{enhanced}}}}
$$

An example:

<img src="\img\study\cs\amdahlaw.png" alt="Example of Amdahlaw's Law">

Important inference:

$$
Speedup_{overall}<1/(1-Fraction_{enhanced})
$$


## Great architectures ideas

- Design for **Moore's law**

- Use **abstraction** to simplify design

- Make the common case fast

- Improve performance via **parallelism**

- Improve performance via **pipelining**

- v=Improve performance via **prediction**

- Use a **hierarchy of memories**.

- Improve dependability via **redudancy**


