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





