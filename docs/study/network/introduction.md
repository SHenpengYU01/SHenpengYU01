# Chapter1 Computer network and the Internet

## Network edge

1. hosts: clients and servers

host sends packets of data. Packet transmission delay is defined as time needed to transmit L-bit packet into link. Suppose the transmission rate is $R$, then delay= $L(bits)/R(bits/sec)$ .


2. access network:
  - cable based access: frequency division multiplexing (FDM): different channels transmitted in different frequency bands
  - DSL(digital subscriber line): use existing telephone line to central office DSLAM
  - wireless:
    - Wireless local area networks(WLANS)
    - Wide-area cellular access networks

3. physical meadia:

  - coaxial cable
  - fiber optic cable
  - wireless radio
  - radio link types:
    - wireless LAN
    - Bluetooth
    - terrestrial microwave
    - satellite


## Network core

<img src="\img\study\network\ch1\networkcore.png" alt="network core">

Packet-switching: hosts break application-layer messages into packets. Then, network forwards packets from one router to the next, across links on path from source to destination.

Entire packet must arrive at router before it can be transmitted on next link, so we need to store and forward.  

Packet switching has the problem of queuing.

<img src="\img\study\network\ch1\queue.png" alt="packet queuing">

There is another way of switching: circuit switching.

<img src="\img\study\network\ch1\circuit_switching.png" alt="circuit switching">


## Performance

### Packet delay

Happens when packets queue in router buffers, waiting for ture for transmission.

<img src="\img\study\network\ch1\delay1.png" alt="packet delay1">

<img src="\img\study\network\ch1\delay2.png" alt="packet delay2">

### Packet loss

Happens when memeory to hold queued packets fills up

### Throughut

**Throughput**: rate (bits/time unit) at which bits are being sent from sender to receiver
**Bottleneck link**: link on end-end path that constrains end-end throughput.

## Protocol layers

There are different ways to represent protocol layers, like the OSI(Open Systems Interconnection) model(7 layers) and TCP/IP model(4 layers). Here we use the 5-layer model.

1. **application**: supporting network applications
  - HTTP, IMAP, SMTP, DNS

2. **transport**: process-process data transfer
  - TCP, UDP

3. **network**: routing of datagrams from source to destination
  - IP, routing protocols

4. **link**: data transfer between neighboring  network elements
  - Ethernet, 802.11 (WiFi), PPP

5. **physical**: bits “on the wire”

PDU(protocol data unit) encapsulated in each layer:

Application: message
Transport: segment
Network: datagrams
Link: frame
Physical: bits

<img src="\img\study\network\ch1\protocol.png" alt="protocol layer">
