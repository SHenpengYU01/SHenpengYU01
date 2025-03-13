# The application layer

## Principles of Network Applications

### Communication paradigm

**Client-server paradigm**:
server:

- always-on host
- permanent IP address
- often in data centers, for scaling
clients:
- contact, communicate with server
- may be intermittently connected
- may have dynamic IP addresses
- do not communicate directly with each other
examples: HTTP, IMAP, FTP

**Peer-peer architecture**:

- no always-on server
- arbitrary end systems directly communicate
- peers request service from other peers, provide service in return to other peers
- peers are intermittently connected and change IP addresses
example: P2P file sharing [BitTorrent]

### Sockets

Process: program running within a host(resources management and allocation)

- Addressing: IP address + port
- Communication:
  - within same host: IPC(inter-process communication)
  - different host: exchanging messages

<img src="\img\study\network\ch2\sockets.png" alt="Sockets">

### Protocols

<img src="\img\study\network\ch2\protocoldefine.png" alt="What a protocol defines">


<img src="\img\study\network\ch2\transportp.png" alt="Transport protocol">

<img src="\img\study\network\ch2\transreq.png" alt="Transport requirement of different apps">

<img src="\img\study\network\ch2\sockets.png" alt="Sockets">

**Securing TCP**:

Vanilla TCP & UDP sockets:

- no encryption
- cleartext passwords sent into socket traverse Internet  in cleartext (!)

Transport Layer Security (TLS):

- provides encrypted TCP connections
- data integrity
- end-point authentication


## Web and HTTP

### HTTP

HTTP: hypertext transfer protocol

- Web's application-layer protocol
- client/server model
- stateless: **server** maintains no infomation about past client requests(so we need cookie)
- HTTP uses TCP in the transport-layer

There are two types of HTTP connections:

- **Non-persistent** HTTP: at most one object sent over TCP connection. It is used by HTTP/1.0 by default.
- **Persistent HTTP**: multiple objects can be sent over single TCP connection between client, and that server. Used by HTTP/1.1 by default.

Non-persistent HTTP example:

<img src="\img\study\network\ch2\nonperhttp.png" alt="Non-persistent HTTP example">

But it is bothering to initiate TCP every time we want to sent a request because it takes time and gets OS overhead:

<img src="\img\study\network\ch2\httptime.png" alt="Response time for Non-persistent HTTP">

!!! info "RTT"
    RTT is short for roundtrip time

Therefore, we use persistent HTTP(HTTP1.1) more.
Property of persistent  HTTP (HTTP1.1):

- server leaves connection open after sending response
- subsequent HTTP messages  between same client/server sent over open connection
- client sends requests as soon as it encounters a referenced object
- as little as one RTT for all the referenced objects (cutting response time in half)

### HTTP message

**Request message**
HTTP request message general format:

<img src="\img\study\network\ch2\httpmsg.png" alt="HTTP request message general format">

Other HTTP request messages:

- GET method: include user data in URL field of HTTP GET request message (following a ‘?’)
- POST method: for web page including form input
- PUT method: uploads new file (object) to server, and completely replaces file that exists at specified URL with content in entity body of POST HTTP request message
- HEAD method: request the headers of a resource, but without the actual content (body) of the resource, similar to the GET method but without getting response body

**Response message**:

- Format:
  - Status line: HTTP version  Status code Status message
  - Headers: Content-type etc
  - Body(optional): html, jpeg, etc

### Cookies

**Why we need cookies**:

HTTP GET/response interaction is stateless:  

- no need for client/server to track “state” of multi-step exchange
- all HTTP requests are independent of each other
- no need for client/server to “recover” from a partially-completed-but-never-completely-completed transaction

Considering stateful one protocol:  

<img src="\img\study\network\ch2\statefulp.png" alt="A stateful protocol">

!!! info "What is Cookie"
    Cookie is a small piece of data sent from a server to a client's web browser when client requests server for the first time and it is stored on the client side.
    Format: `Set-Cookie: <cookie-name>=<cookie-value>; <attributes>`

**What it can do**:

- track user behavior on a given website (first party cookies)
- track user behavior across multiple websites (third party cookies) without user ever choosing to visit tracker site (!)


How third party cookies(from websites you didn't choose to visit) track users' behavior?

The third-party: like ad.com. When you visit example.com, it returns you cookies and you store it locally. This is the first party cookie. But at the same time you will request ad.com *in some way* and they send cookies to you and store them.

When you visit example2.com, there is still ad there so you send request to ad.com and they store the cookies recording you have visited example2.com.

In this way, the ad.com know you have visited example.com, example2.com and so on. It knows more about you and could give you personalized ads on sites with ad.com resourses embedded in.

<img src="\img\study\network\ch2\cookie1.png" alt="First and third party cookies">

<img src="\img\study\network\ch2\cookie2.png" alt="Cookie tracking user's behavior">


!!! tip
    In chrome the cookie of a specific site we are visiting can be seen by using *application* in developer tools.

??? info "GDPR"
    When cookies can identify an individual, cookies are considered personal data, subject to GDPR(general data protection regulation) personal data regulations.

### Web caches

!!! info "caching's goal"
    To satisfy client requests without involving origin server. Then this can reduce response time for client request and reduce traffic on an institution's access link.

**How it works**:

- user configures browser to point to a (local) Web cache and browser sends all HTTP requests to cache
  - if object in cache: cache returns object to client
  - else cache requests object from origin server, caches received object, then returns object to client

<img src="\img\study\network\ch2\webcache.png" alt="Web caches">

??? note "Cache-Control"
    There is `Cache-Control` section in both HTTP request and response headers.

    - In request header, used to indicate how the client (usually a browser) wants to interact with caches when requesting a resource.

    - In response header: used by the server to specify caching instructions for the client (browser) and intermediate caches (like CDNs or proxy servers).
    `Cache-Control: private`: the response is specific to a single user and should not be cached by shared caches (e.g., proxy servers or CDNs). However, it can be cached in the browser's local cache.
    `Cache-Control: public`:  the response can be cached by both private and shared caches. This is typically used for resources that are meant to be publicly available, such as images or static files.

### HTTP/2

**Goal**: decrease delay in multi-object HTTP requests

Property: increased flexibility at server in sending objects to client:

  1. methods, status codes, most header fields unchanged from HTTP 1.1
  2. transmission order of requested objects based on client-specified object priority (not necessarily FCFS)
  3. push unrequested objects to client
  4. divide objects into frames, schedule frames to mitigate HOL(head-of-line) blocking(first large packets block the latter small ones)

## E-mail

3 main components: user agent(mail reader), mail severs, SMTP(simple mail transfer protocol)

## DNS(domain name system)

### Services

services:

- translate hostname to IP address
- host/mailserver aliasing

### Structure

<img src="\img\study\network\ch2\dns1.png" alt="DNS structure">

- **root** name servers: official, contact-of-last-resort by name servers that can not resolve name
- **Top-Level** domain(TLD) severs:
  - responsible for .com, .org, .net, .edu, .aero, .jobs, .museums, and all top-level country domains, e.g.: .cn, .uk, .fr, .ca, .jp
  - Network Solutions: authoritative registry for .com, .net TLD
  - Educause: .edu TLD
- **Authoritative** DNS servers: organization’s own DNS server(s), providing authoritative hostname to IP mappings for organization’s named hosts.

<img src="\img\study\network\ch2\dns2.png" alt="Iterative DNS name resolution">

<img src="\img\study\network\ch2\webcache.png" alt="Recursive DNS name resotution">

### Caching

Once (any) name server learns mapping, it caches mapping, and immediately returns a cached mapping in response to a query.

- caching improves response time
- cache entries timeout (disappear) after some time (TTL)
- TLD servers typically cached in local name servers

### DNS records

DNS: distributed database storing resource records(RR)

RR format:(name, value, type, ttl)

**Common record types**:

- A record(address record)
  - name: domain name
  - value: IPv4 address

- AAAA record(IPv6 address record)
  - name: domain name
  - value: IPv6

- NS record(name server)
  - name: domain
  - value: hostname of authoritative name server for this domain

- CNAME
  - name: alias name for some "canonical"(the real) name(another domain name who has its own records)
  - value: canonical name

- MX record(mail exchange record)
  - name: domain name
  - value: name of SMTP mail server associated with the domain name


**DNS protocol messages**:

<img src="\img\study\network\ch2\dnsmsg1.png" alt="DNS message">

<img src="\img\study\network\ch2\dnsmsg2.png" alt="DNS message">

An DNS response message in wireshark(results with display filter: dns)

<img src="\img\study\network\ch2\dnsmsg3.png" alt="DNS message in wireshark">

### Useful commands

!!! tip "commands"
    There are some useful commands about DNS:
    `nslookup –option1 –option2 host-to-find dns-server`
    nslookup is used to resolved the IP address of a specific domain.
    With options like: `nslookup –type=NS zju.edu.cn`. This gives the DNS servers and theire IP of domain `zju.edu.cn`.
    `ipconfig \display dns` will display the cached DNS records on your computer.
    `ipconfig \flushdns` will flush these DNS records.


## P2P applications

### P2P architecture

!!! note "Basic idea"
    - no always-on server
    - arbitrary end systems directly communicate
    - peers request service from other peers, provide service in return to other peers
      - self scalability – new peers bring new service capacity, and new service demands
    - peers are intermittently connected and change IP addresses
      - complex management
    - examples: P2P file sharing (BitTorrent), streaming (KanKan), VoIP (Skype)

### File distribution time

For the following discussion: F is the file size and u and v are the upload and download speed respectively.

<img src="\img\study\network\ch2\p2p2.png" alt="Client-Server model">

<img src="\img\study\network\ch2\p2p3.png" alt="P2P model">


### BitTorrent

<img src="\img\study\network\ch2\p2p1.png" alt="BitTorrent">

- A peer joining torrent:  
  - has no chunks, but will accumulate them over time from other peers
  - registers with tracker to get list of peers, connects to subset of peers (“neighbors”)

- while downloading, peer uploads chunks to other peers
- peer may change peers with whom it exchanges chunks
- **churn**: peers may come and go
- once peer has entire file, it may (selfishly) leave or (altruistically) remain in torrent

**Requesting chunks**:
At any given time, different peers have different subsets of file chunks. Periodically, Alice asks each peer for list of chunks that they have. Alice requests missing chunks from peers, rarest first


**Sending chunks**: tit-for-tat

- Alice sends chunks to those four peers currently sending her chunks at highest rate. Other peers are choked by Alice (do not receive chunks from her)
- Re-evaluate top 4 every 10 secs
- Every 30 secs: randomly select another peer, starts sending chunks, namely“optimistically unchoke” this peer and this newly chosen peer may join top 4
- For higher upload rate: find better trading partners



## Video streaming and CNDs

### Challenges

- server-to-client bandwidth will vary over time
- packet loss, delay due to congestion will delay playout

<img src="\img\study\network\ch2\streaming1.png" alt="Streaming at constant rate">

- continuous playout constraint: during client video playout, playout timig must match original timing

With client-side buffering:

<img src="\img\study\network\ch2\streaming2.png" alt="Streaming at variable rate">

### DASH

Refer to **Dynamic, Adaptive streaming over HTTP**. It is an approach that allows a client to adapt the encoding rate of retrieved video to network congestion conditions.

- server:
  - divides video file into multiple **chunks**
  - each chunk encoded at multiple different rates
  - different rate encodings stored in different files
  - files **replicated** in various CDN nodes
  - manifest file: provides URLs for different chunks

- client:
  - periodically estimates server-to-client bandwidth
  - consulting manifest, requests one chunk at a time
    - chooses maximum coding rate sustainable given current bandwidth
    - can choose different coding rates at different points in time (depending on available bandwidth at time), and from different servers

!!! note "General streaming"
    Streaming video = encoding + DASH + playout buffering

### CND(content delivery network)

**challenge:** how to stream content (selected from millions of videos) to hundreds of thousands of simultaneous users?

store/serve multiple copies of videos at multiple geographically distributed sites (CDN)

- enter deep: push CDN servers deep into many access networks
- bring home: smaller number of larger clusters in POPs near access nets

<img src="\img\study\network\ch2\netflix.png" alt="An example of netflix">


## Socket Programming with UDP and TCP



