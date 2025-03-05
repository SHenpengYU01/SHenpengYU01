# review of sys2

## 硬件

### ISA

**Arch**:

1. Stack architecture:
2. Accumulator
3. GPR
4. Register-Memory
5. load-store


**addressing mode**:


### pipeline

![alt text](/img/study/cs/sys2/image-17.png)

**class**:
![alt text](/img/study/cs/sys2/image-16.png)

#### Performance

1. TP(throughput):$TP=\frac{n}{T}$
![alt text](/img/study/cs/sys2/image-18.png)
2. Speedup
![alt text](/img/study/cs/sys2/image-19.png)
3. Efficiency
![alt text](/img/study/cs/sys2/image-20.png)
举例：
![alt text](/img/study/cs/sys2/image-21.png)
![alt text](/img/study/cs/sys2/image-22.png)


### hazard

#### structural

1. Df: A required resource is busy
2. Sotution: Stall: insert bubble:addi x0, x0, 0

#### data

1. Df:
    1. Data dependency between instructions
    2. Need to wait for previous instruction to complete its data read/write
2. Solution:
![alt text](/img/study/cs/sys2/image-23.png)

![alt text](/img/study/cs/sys2/image-24.png)

- detect and forwarding
![alt text](/img/study/cs/sys2/image-25.png)
![alt text](/img/study/cs/sys2/image-26.png)
![alt text](/img/study/cs/sys2/image-27.png)
- Load-Use Hazard Detection:
detect and insert bubble
![alt text](/img/study/cs/sys2/image-28.png)

#### control
![alt text](/img/study/cs/sys2/image-29.png)


### Scheduling
#### Prohibit table


#### initial confict vector
二进制数字串，prohibit table中对应数字的位为1，其余为0

#### state transition graph

### Multiple issue


#### multiple-issue processor type

##### Superscalar

##### VLIW(Very Long Instruction Word)

![alt text](/img/study/cs/sys2/image-30.png)

### Exception& Hardware-S interface





## 软件
基本脉络：
process
->process scheduling
->IPC
->thread
->sychronization
->deadlock

进程：资源分配和保护单元
线程：资源执行单元




### 神图

![alt text](/img/study/cs/sys2/image.png)



### process

#### PCB
![alt text](/img/study/cs/sys2/image-31.png)


#### Process State

![alt text](/img/study/cs/sys2/image-32.png)

1. new:
  :star:forK(syscall):返回两值（对父进程：子进程PID；子进程：0），copy两份user space context(pt regs) 重点：fork 出的进程处

2. context_switch:切换stack,pc(涉及硬件资源，发生在kernel)
![alt text](/img/study/cs/sys2/image-33.png)


### Process scheduling:star:

![alt text](/img/study/cs/sys2/image-34.png)

![alt text](/img/study/cs/sys2/image-35.png)

![alt text](/img/study/cs/sys2/image-36.png)

![alt text](/img/study/cs/sys2/image-37.png)

### IPC


### Thread

进程的执行单元：

![alt text](/img/study/cs/sys2/image-39.png)

进程执行顺序图
进程fork后进入ready队列等待

1个进程中有n个线程：n个task struct
进程无task struct,它用leader thread的task_struct

thread node thread group遍历thread

user space code与kernel space code 不同
thread:user kernel一对一

每个线程的pt regs，是thread kernel stack一部分



### synchronization

#### critical section

Critical section(临界区):指在并发编程中，多个进程或线程共享的资源（例如共享内存、文件、设备等）需要被访问的那段代码。临界区中的代码部分只能由一个进程或线程在同一时间访问，以避免竞争条件（race condition）和数据不一致的情况。

solution to critical section 条件：

  1. Mutual exclusion(互斥访问): critical section中只能有一个进程在执行
  2. Progress(空闲让进):如果没有进程在临界区，且有进程等待进入临界区时，必定有进程能够进入临界区
  3. Bounded waiting(有限等待时间):防止starvation


#### peterson's solution:只能解决两个进程间冲突

Peterson的算法通过使用两个共享变量来控制两个进程的行为：

- flag[0] 和 flag[1]：这两个变量表示这两个进程是否希望进入临界区。
- turn：这个变量表示当前轮到哪个进程进入临界区。

![alt text](/img/study/cs/sys2/image-1.png)

可以满足上面三个条件，但有如下问题：

- Only works for two processes case
- It assumes that LOAD and STORE are atomic
- 没考虑Instruction reorder：编译器可能会对指令重排


#### Hardware solution

1. Memory barriers(一种处理器指令)：内存屏障作为同步原语被用来强制指令按特定顺序执行，确保对共享数据的访问按预期发生。
![alt text](/img/study/cs/sys2/image-2.png)

2. 原子操作指令：
   1. test and set(TAS):先读取内存位置的值，然后将其设置为特定值（如1），并返回原值。该操作是原子的，因此能够确保只有一个线程能成功获取锁。
  ![alt text](/img/study/cs/sys2/image-5.png)
  ![alt text](/img/study/cs/sys2/image-6.png)
   2. compare and swap(CAS):CAS操作读取内存位置的值，并与提供的预期值进行比较。如果两者匹配，则将该位置的值替换为新值；如果不匹配，则不执行任何操作并返回当前值。CAS操作是原子的，因此可以确保多线程之间不会发生冲突。
  ![alt text](/img/study/cs/sys2/image-3.png)
  ![alt text](/img/study/cs/sys2/image-4.png)

3. Atomic variables:

#### Mutex locks（互斥锁）
保证在任何时刻，只有一个线程能够持有该锁并进入临界区（critical section），其他线程必须等待，直到该锁被释放。
过程如下：

```c
while(true){
    acquire lock(atomic)
    critical section
    release lock(atomic)
    remainder section
}
```

1. 自旋锁：自旋锁是一种轻量级的锁实现，它的基本思想是当线程无法获得锁时，它会不断循环（自旋），检查锁的状态是否变为可用。这种方法适用于锁争用不频繁的场景，因为自旋会消耗CPU资源。
实现：
![alt text](/img/study/cs/sys2/image-8.png)
acquire 到release之间其他进程在busy waiting——too much spinning，浪费CPU time
2. 基于队列的锁（Queue-based Locks）：线程会按照请求锁的顺序进入队列，等到锁释放时按照顺序被唤醒。操作系统的调度机制可以确保线程按照公平的顺序获得锁。

#### Semaphore（信号量）

信号量是一个整数，用于表示系统中可用资源的数量。它的值可以增加或减少，通常通过两种操作来控制：

- P操作（尝试）：通常也称为 wait操作，它试图减少信号量的值。若信号量大于0，操作成功，信号量减1；若信号量为0，则进程或线程会被阻塞，直到信号量大于0为止。

- V操作（增加）：通常也称为 signal操作，它试图增加信号量的值。信号量加1，如果有进程或线程因为信号量为0而被阻塞，它们中的一个会被唤醒继续执行。
![alt text](/img/study/cs/sys2/image-9.png)

实现：
![alt text](/img/study/cs/sys2/image-10.png)
实现使用了spinning lock会有

#### Deadlock and starvation

Deadlock:

- 条件：
  - 互斥条件（Mutual Exclusion）：系统中的某些资源只能由一个进程占用，且在占用资源时，该资源不能同时被其他进程访问。
  - 占有并等待（Hold and Wait）：一个进程持有至少一个资源，同时等待其他被占用的资源。
  - 不剥夺条件（No Preemption）：资源不能被强制从进程中剥夺，只能由进程自行释放。
  - 循环等待（Circular Wait）：存在一个进程等待的循环链，每个进程等待下一个进程释放资源。
示例：
假设两个进程 A 和 B 各自持有一个资源，并等待对方释放另一个资源：
进程 A 持有资源 1，等待资源 2。
进程 B 持有资源 2，等待资源 1。
A,B相互等待导致死锁。

Starvation：

#### Atomic variable
支持原子操作的变量，对变量的所有操作都是原子的，不会出现数据竞争。


#### 三个问题:star:



1. Bounded buffer problem:
有界缓冲区问题，又称为生产者-消费者问题，是并发编程中的经典同步问题。它描述了两个或多个进程或线程在共享有限缓冲区时如何安全有效地交换数据的场景。

![alt text](/img/study/cs/sys2/image-14.png)
![alt text](/img/study/cs/sys2/image-11.png)

![alt text](/img/study/cs/sys2/image-12.png)
2. Readers-Writers Problem:




### Deadlock

#### 四个条件

死锁的四个必要条件：

1. 互斥条件：每个资源只能由一个进程占用，且该资源在被占用时不能被其他进程使用。
2. 请求与保持条件：进程至少持有一个资源，并且等待获取其他被其他进程持有的资源。
3. 不剥夺条件：进程持有的资源不能被强制剥夺，只能等进程释放。
4. 循环等待条件：存在进程循环等待资源的情况。

#### 解决方案

##### Deadlock prevention
打破死锁四个条件

##### Deadlock aviodance

Banker's algorithm:在每次资源分配前，系统通过模拟是否会导致死锁来判断是否分配该资源。这个算法的关键目标是确保系统处于一个“安全状态”，即可以避免死锁的发生。

![alt text](/img/study/cs/sys2/image-15.png)

##### Deadlock detection
寻找环
问题：starvation

##### Deadlock recovery

kill deadlock process


## Software

内存不存数据类型

1. OS：resource allocator abstractor, in kernel mode

2. events type in OS:interrupts(hardware) and exception(software)
   - :star:syscall(unprivileged):interface between user and kernel mode
   - U->K: context is stored in kernel stack(kernel entry does this)
   - signals,timers and timeouts, user input events,process events, faults and exceptions

3. Sys call:

4. system service:
   - static linker:移植性更强，需内存大
   - dynamic linker:
   - loaders: a part of the operating system responsible for loading executable programs (or shared libraries) into memory for execution.  

heap可共享：
stack(per-thread)：不可共享：栈内存是与函数调用紧密绑定的，并且在函数返回时会被释放，所以它的生命周期是短暂的、局部的。因此，栈不适合在不同线程间共享。每个线程有自己的栈，栈的内容不能在多个线程间传递。

5. Process(resource allocation and protection):
   - PCB:包含PID,pstate,PC


