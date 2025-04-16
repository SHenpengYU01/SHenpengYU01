# Cache

## Different Types of Memory

- Mechanical memory: Magnetic Drum/core memory

- Electronic memory:
  - SRAM(static random access memory)
  - DRAM(dynamic random access memory)
    - SDRAM, DDR
  - ROM
    - EPROM,EEPROM(electrically erasable, programmable)
  - Flash: NAND, NOR

Here’s a breakdown of those different types of memory:

1. **SRAM (Static RAM)**
   - **Type**: Volatile
   - **Speed**: Fast
   - **Use**: Often used for cache memory in CPUs, GPUs, and other performance-critical applications.
   - **Why It's Fast**: Doesn’t need to be refreshed like DRAM.
   - **Drawback**: More expensive and takes up more space than DRAM.
   - **How It Works**: Stores data in flip-flops, meaning each bit of data is stored in a set of transistors that don’t require constant refreshing.

2. **DRAM (Dynamic RAM)**
   - **Type**: Volatile
   - **Speed**: Slower than SRAM
   - **Use**: Main memory in computers (RAM).
   - **Why It's Slower**: Requires constant refreshing because it stores data in capacitors, which leak charge over time.
   - **Drawback**: More power-hungry and slower than SRAM, but much cheaper and denser, allowing for larger amounts of memory.

3. **HBM (High Bandwidth Memory)**
   - **Type**: Volatile
   - **Speed**: Very high speed
   - **Use**: Used in high-performance computing applications like GPUs and AI processing.
   - **Why It's Fast**: Has a very wide memory interface and stacks chips vertically, reducing latency and increasing throughput.
   - **Drawback**: Expensive and not as widely used in consumer products.

4. **Flash**(EEPROM)
   - **Type**: Non-volatile
   - **Speed**: Slower than DRAM but faster than traditional hard drives.
   - **Use**: Solid-state drives (SSDs), USB drives, memory cards, etc.
   - **Why It's Non-volatile**: Retains data even when power is off.
   - **Drawback**: Limited write endurance over time, but more durable and faster than HDDs.



### Key Differences

- **Volatile vs. Non-volatile**: SRAM, DRAM, HBM, and DDR are all volatile, meaning they lose data when power is off. Flash is non-volatile, meaning it keeps data even when powered down.
- **Speed**: HBM > SRAM > DRAM > Flash.
- **Cost**: SRAM is the most expensive per bit, followed by HBM. DRAM,  and ROM(Flash) are more affordable for larger capacities.




## Memory Hierarchy

Performance of high-speed computers is usually limited by memory bandwidth and latency.

- Latency :time for a single access
- Bandwidth: number of accesses per unit time

**Locality** in Memory Hierarchy:

- Temporal locality:if an item is referenced, it will tend to be referenced again soon.  

- Spatial locality: if an item is referenced, items whose addresses are close by will tend to be referenced soon.

<img src="\img\study\cs\sys3\memory1.png" alt="Memory hierarchy: Laptop/Desktop">

<img src="\img\study\cs\sys3\memory2.png" alt="Memory hierarchy: Laptop/Desktop">

## Cache

Cache: The highest or first level of the memory hierarchy encountered once the address leaves the processor. It employs buffering to reuse commonly occurring items.  

Cache can be a relevant concept: the lower one is always the cache of the upper one:

<img src="\img\study\cs\sys3\cache1.png" alt="Storage Hierarchy">



## How cache workds

Concepts:  

- Cache hit/miss: when the processor can/cannot find a requested data item in the cache.
- Block/Line Run: A fixed-size collection of data containing the requested word, retrieved from the main memory and placed into the cache
- Cache Locality:  
  - Temporal locality: Need the requested word again soon
  - Spatial locality: Likely need other data in the block soon
- Cache miss:
  - Time depends on:
    1. Lantency: the time to retrieve the first word of the block
    2. Bandwidth: the time to retrieve the rest of this block
  - causes:
    1. Compulsory miss: first reference to a block
    2. Capacity miss: blocks discarded and later retrieved
    3. Conflict miss: program makes repeated references to multiple addresses from different blocks that map to the same location in the cache


**Cache terms**:
<img src="\img\study\cs\sys3\cache_terms.png" alt="Cache terms">

### Four questions for cache designers

<img src="\img\study\cs\sys3\cache_design.png" alt="Questions for cache design">

### 1. Q1: Block Placement
    - Direct mapped: A cache structure in which each memorylocation is mapped to exactly one locationin the cache.
    - 2-way set-associative: A cache that has a fixed number oflocations (at least two) where each blockcan be placed.
    <img src="\img\study\cs\sys3\2way_assosiative.png" alt="2-Way Set-associative">
    - Fully-associative: A cache structure in which a block can beplaced in any location in the cache.

### 2. Block Identification:
<img src="\img\study\cs\sys3\cache_block.png" alt="Cache Block Identification">

### 3. Block replacement

Which block should be replaced on a Cache/main memory miss?

- Random replacement: randomly pick any block
- Least-Recently Used(LRU): pick the block in the set which was least recently accessed
- First in, first out: Choose a block from the set which was first came into the cache

### 4. Write strategy

When data is written into the cache (on a store), is the data also written to main memory?

- Written to memory, the cache is called a write-through cache
  - Can always discard cached data - most up-to-date data is in memory
  - Cache control bit: only a valid bit
  - Memory (or other processors) always have latest data
- NOT written to memory, the cache is called a write-back cache
  - Can’t just discard cached data - may have to write it back to memory
  - Cache control bits: both valid and dirty bits
  - Much lower bandwidth, since data often overwritten multiple times


- Advantage of Write-through: Read misses don't result in writes, memory hierarchy is consistent and it is simple to implement.
- Advantage of Write back: Writes occur at speed of cache and main memory bandwidth is smaller when multiple writes occur to the same block.

**Write stall**: When the CPU must wait for writes to complete during write through

**Write buffer**: A small cache that can hold a few values waiting to go to main memory. This buffer helps when writes are clustered. It does not entirely eliminate stalls since it is possible for the buffer to fill if the burst is larger than the buffer.  

#### Write misses

If a miss occurs on a write (the block is not present), there are two options:

- Write allocate: The block is loaded into the cache on a miss before anything else occurs.
- No-write allocate (Write around)
  - The block is only written to main memory
  - It is not stored in the cache.

In general, write-back caches use write allocate, and write-throughcaches use no-write allocate.




## Advanced optimizations of cache performance

### Reducing the miss penalty or miss rate via parallelism

Using HBM to extend the memory hierarchy:

**什么是 HBM**:  
HBM（High Bandwidth Memory），也就是高带宽内存，通常以3D堆叠的形式与CPU或GPU封装在一起，提供比传统GDDR显存更高的带宽和更低的功耗。


### HBM的技术优势
HBM是一种基于3D堆叠技术的高性能内存，其核心特点包括：

- **高带宽**：通过宽总线（1024位或更高）和高速接口（如2.4 Gbps/引脚），带宽可达数百GB/s至TB/s。
- **低延迟**：通过硅通孔（TSV）缩短数据传输路径，减少物理距离带来的延迟。
- **高密度**：垂直堆叠多层DRAM芯片，节省空间并提升容量。
- **低功耗**：相比传统GDDR，单位带宽的功耗更低。


### **2. 利用HBM提升缓存性能的具体方法**

#### **(1) 扩展末级缓存（LLC）容量**

- **原理**：将HBM作为CPU或GPU的末级缓存（L3/L4），直接存储高频访问数据。
- **效果**：
  - 减少主存访问次数，降低缓存缺失率（Miss Rate）。
  - 缓解传统DRAM带宽瓶颈，尤其适合数据密集型任务（如机器学习、科学计算）。
- **示例**：
  - AMD的Instinct MI系列加速器使用HBM作为显存，同时充当GPU的末级缓存。
  - Intel的Xeon Phi（Knights Landing）曾集成HBM作为“MCDRAM”，支持缓存模式或直接内存模式。

#### **(2) 分层缓存架构（Cache Hierarchy Optimization）**

- **原理**：在传统缓存层次（L1/L2/L3）之外，引入HBM作为专用缓存层。
- **设计**：
  - **HBM与SRAM缓存协同**：SRAM负责低延迟快速访问，HBM负责大容量数据暂存。
  - **动态数据迁移**：根据局部性将热数据保留在SRAM，冷数据移至HBM。
- **应用**：适用于需要大容量缓存的场景（如数据库、实时分析）。

#### **(3) 高带宽并行数据预取**

- **原理**：利用HBM的高带宽特性，支持大规模并行数据预取。
- **实现**：
  - 硬件预取器可同时加载多个缓存行到HBM，覆盖更长的访问跨度。
  - 结合非阻塞缓存（Non-Blocking Cache），隐藏预取延迟。
- **效果**：显著减少因缓存缺失导致的处理器停顿。

#### **(4) 近内存计算（Near-Memory Computing）**

- **原理**：在HBM附近集成计算单元（如存内计算PIM），减少数据搬运开销。
- **技术**：
  - **HBM-PIM**（三星）：在HBM中嵌入AI计算单元，直接处理存储中的数据。
  - **缓存过滤**：在HBM控制器中实现数据过滤逻辑，仅将必要数据传回处理器。
- **应用**：AI推理、图计算等内存密集型任务。

#### **(5) 异构缓存系统**

- **原理**：混合HBM与传统DRAM（如DDR4/DDR5），构建异构缓存/内存系统。
- **策略**：
  - **热数据分配**：高频访问数据存储在HBM，低频数据存储在传统DRAM。
  - **操作系统/驱动支持**：通过NUMA（非统一内存访问）策略优化数据分布。
- **示例**：NVIDIA的Grace Hopper超级芯片结合HBM与LPDDR5，优化AI负载。

---

### **3. 实际应用案例**
#### **(1) GPU显存与缓存融合**

- **场景**：NVIDIA H100 GPU使用HBM3作为显存，带宽达3 TB/s。
- **优化**：
  - HBM直接作为GPU的全局缓存，支持大规模并行线程（如CUDA核）的数据访问。
  - 通过L2缓存与HBM的紧密耦合，减少显存访问延迟。

#### **(2) 高性能计算（HPC）**

- **场景**：气象模拟、分子动力学等需要TB级数据吞吐的应用。
- **优化**：
  - 使用HBM作为节点本地缓存，加速分布式计算中的数据交换。
  - 结合RDMA（远程直接内存访问）技术，实现跨节点低延迟通信。

#### **(3) 机器学习训练与推理**

- **场景**：训练大型语言模型（如GPT-4）时，需频繁访问参数和梯度数据。
- **优化**：
  - 将模型参数缓存在HBM中，利用高带宽快速更新权重。
  - 使用HBM-PIM技术，在内存中直接执行部分计算（如矩阵乘加）。

---

### **4. 挑战与解决方案**
#### **(1) 成本与制造复杂性**

- **挑战**：HBM的3D堆叠工艺复杂，良率低，成本远高于传统DRAM。
- **解决方案**：针对高端市场（HPC、AI芯片）优化设计，通过规模化生产降低成本。

#### **(2) 散热与功耗**

- **挑战**：3D堆叠结构导致热密度高，可能引发散热问题。
- **解决方案**：
  - 采用先进封装技术（如CoWoS-S）优化散热路径。
  - 动态电压频率调整（DVFS）降低功耗。

#### **(3) 软件与生态支持**

- **挑战**：需操作系统、驱动和应用程序协同优化以发挥HBM性能。
- **解决方案**：
  - 提供HBM-aware的内存分配API（如CUDA Unified Memory）。
  - 编译器优化数据布局（如优先将数组分配到HBM）。

---

### **5. 未来发展方向**

- **HBM4**：进一步提升堆叠层数（12层以上）和带宽（>6.4 Gbps/引脚）。
- **存算一体**：将计算单元更深度集成到HBM中，实现“内存即计算”。
- **异构集成**：HBM与Chiplet（小芯片）技术结合，构建灵活的多核系统。

---

### **总结**
通过HBM提升缓存性能的核心在于**利用其高带宽和低延迟特性，扩展缓存容量、优化数据预取、减少主存访问**。具体实现需结合硬件架构设计（如分层缓存、近内存计算）、软件优化（数据布局、预取策略）以及应用场景适配。尽管面临成本与散热挑战，HBM仍是高性能计算、AI和大数据领域的关键技术，未来随着3D堆叠和存算一体技术的演进，其潜力将进一步释放。





