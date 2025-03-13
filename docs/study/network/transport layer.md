# The transport layer

## Transport-layer services

**Services**: provide logical communication between application processes running on different hosts.

**Protocols:** TCP and UDP

## Multiplexing and demultiplexing

**Multiplexing:** Taking data from one socket (one of possibly many sockets), encapsulating a data chuck with header information – thereby creating a transport layer segment – and eventually passing this segment to the network layer.

**Demultiplexing:** Receiving a transport-layer segment from the network layer, extracting the payload (data) and delivering the data to the correct socket by using the IP address(only TCP) and port numbers in the segment.

**Summary:**  

- Multiplexing, demultiplexing: based on segment, datagram header field values
- UDP: demultiplexing using destination port number (only)
- TCP: demultiplexing using 4-tuple: source and destination IP addresses, and port numbers
- Multiplexing/demultiplexing happen at all layers



## Connetionless transport: UDP

UDP: user datagram protocol

- UDP segments may be lost or delivered out-of-order to app
- connectionless:
  - no handshaking between UDP sender and reciever
  - each UDP segment handled independently of others

**Where is there UDP:**

- no connection estabishment(this can reduce RTT delay)
- simple: no connection state at sender, receiver
- small header size
- no congestion control
  - can blast away as fast as desired
  - can function in the face of congestion

**UDP segment**:

<img src="\img\study\network\ch3\udpsegment.png" alt="UDP segment">

### UDP checksum

To detect errors in transmitted segment.

Sender:

- treat contents of UDP segment (including UDP header fields and IP addresses) as sequence of 16-bit integers
- compute checksum: addition (one’s complement sum) of segment content
- checksum value put into UDP checksum field

Receiver:

- compute checksum of received segment
- check if computed checksum equals checksum field value

An example:

<img src="\img\study\network\ch3\UDPchecksum.png" alt="UDP checksum">

!!! note
    When adding numbers, a carryout from the most significant bit needs to be added to the result.
    This kind of checksum is weak because if the above two number change at the same time, their sum may not change.


## Principles of reliable data transfer(RDT)





## Connection-oriented transport: TCP



