# ILP(Instruction level parallelism)

## Dynamic scheduling

### Why need this

Simple piplining techneques has limitation: they use **in-order instruction issue** and execution and need to stall for data dependency. The later instructions all have to wait.  

Therefore we need **out-of-order** execution to speed up.

### Basic idea

Break ID pipe stage into two stages:

- IS(issue):
  - decode the instruction and check structural hazard
  - in-order issue
- RO(read operands):
  - wait until no data hazard and then read the operands
  - out of order execution

Out-of-order execution introduces the possibility of **WAR**(write after read) and **WAW**(write after write).

```ricsv
1. FDIV.D F10, F0, F2
2. FSUB.D F10, F4, F6
3. FADD.D F6, F8, F14
```

WAW:1,2
WAR:2,3



### Scoreboard Algorithm

In-order issue and out-of-order execution.

**Main Components of the Scoreboard**:

1. Functional Units (FU): These are the execution units that perform operations (e.g., ALUs, floating-point units). The scoreboard keeps track of which units are busy and which are free.

2. Registers: The scoreboard also monitors the status of registers to ensure that data is not overwritten prematurely, which could lead to incorrect results.

3. Instruction Queue: Instructions waiting for operands or a free functional unit are stored in an instruction queue, where they wait for the necessary resources.

4. Control Logic: This component tracks when each instruction can be dispatched for execution, based on the availability of its operands and functional units.

**Summary**:

- Hazards limit performance
  - Structural: need more HW resources
  - Data: need forwarding, compiler scheduling
  - Control: early evaluation & PC, delayed branch, prediction
- Increasing length of pipe increases impact of hazards
  - Pipelining helps instruction bandwidth, not latency!
- Instruction Level Parallelism (ILP) found either by compiler or hardware.

### Tomasulo Algorithm

<img src="\img\study\cs\sys3\tom.png" alt="Tomasulo's hardware structure">

**Main idea**:

- three steps an instruction goes through: Issue, Execute, Write result
- Rename register in hardware to minimize WAW and WAR hazards

**Process**:

1. **Issue**: Get the next instruction from the head of the instruction queue (FIFO)
    - If there is a matching reservation station that is empty, issuethe instruction to the station with the operand values, if they are currently in the registers.
    - If there is not an empty reservation station, then there is a structural hazardand the instruction stalls until a station or buffer is freed.
    - If the operands are not in the registers, keep track of the functional units that will produce the operands.

2. **Execute**:
    - When all the operands are available, the operation can be executed at the corresponding functional unit.
    - Loadand storerequire a two-step execution process：
      - It computes the effective address when the base register is available.
      - The effective address is then placed in the loador storebuffer.

3. **Write Results**:

    - When the result is available, write it on the CDBand from there into the registersand into any reservation stations (including storebuffers).
    - Storesare buffered in the store buffer until both the value to be stored and the store address are available, then the result is written as soon as the memory unit is free.






