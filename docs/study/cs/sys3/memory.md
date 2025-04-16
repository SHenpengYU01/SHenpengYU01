# Memory

## DMA

DMA(Direct Memory Access) is a feature in computer systems that allows peripherals or external devices to directly transfer data to and from system memory (RAM) without involving the CPU for each individual transfer. This improves the overall system efficiency, as it frees up the CPU to perform other tasks while data is being transferred in the background.

### Key Concepts of DMA

- **Bypass the CPU**: With DMA, data can be transferred between memory and peripherals like hard drives, network interfaces, and sound cards, without the need for the CPU to be directly involved in every single byte transfer. This speeds up data movement and reduces the CPU's workload.
  
- **DMA Controller**: A special hardware component called the **DMA controller (DMAC)** manages the DMA process. The controller coordinates the data transfer, ensuring that data is moved correctly and that system resources are not overtaxed.

- **Efficient Data Transfer**: DMA is commonly used for tasks like disk I/O, audio/video streaming, and networking, where large amounts of data need to be transferred quickly.

- **Interrupts**: Once the DMA transfer is complete, the DMA controller usually triggers an interrupt to inform the CPU that the data transfer has finished.


## MMIO(Memory-Mapped I/O)

MMIO is used for communication between the CPU and I/O devices (such as graphics cards, network adapters, or storage devices) by mapping the device's control registers into the system's memory space. The primary purpose of MMIO is to provide a means for the CPU to read and write to device registers, enabling direct interaction with hardware peripherals. The CPU accesses I/O devices as if they were part of the system's memory, using regular memory access instructions.  

## VMM(virtual machine monitor)

A VMM allows one physical machine (also known as the host machine) to run multiple isolated operating systems (known as guest OSes) simultaneously. Each guest OS operates as if it were running on its own dedicated hardware, even though it's sharing the underlying physical resources of the host system.

The VMM manages the allocation of system resources (like CPU time, memory, and storage) to each guest OS to ensure isolation and efficient operation.

### Types

1. Type1 Hypervisor(bare-metal)
VMM runs directly on the physical hardware of the host machine without needing an underlying operating system. More efficient.

2. Type 2 Hypervisor(Hosted)
A Type 2 hypervisor runs on top of an existing host operating system (like Windows, Linux, or macOS). Less efficient but easier to set up.  

Popular VMMs:

- VMware ESXi (Type 1 Hypervisor)
- Microsoft Hyper-V (Type 1 Hypervisor)
- KVM (Kernel-based Virtual Machine) (Type 1 Hypervisor)
- Xen (Type 1 Hypervisor)
- Oracle VirtualBox (Type 2 Hypervisor)
- VMware Workstation (Type 2 Hypervisor)

### Funcitons

- Resource Allocation:
- Isolation:
- Hardware Abstraction:


