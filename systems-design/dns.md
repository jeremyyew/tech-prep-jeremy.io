# DNS

## What is DNS? 
The Domain Name System (DNS) is the phonebook of the Internet. 

It is a **naming system** that maps a user-friendly **"domain name"** (or "host name", or web address, or URL) of a computer/service/resource to a numerical **IP address**, so that a client can locate and interact wih it via underlying network protocols. 

For example, the domain name `www.example.com` might translate to the IP address `93.184.216.34` (under IPv4, or it might be `2606:2800:220:1:248:1893:25c8:1946` under IPv6 - see below). 

The DNS maps names from the **domain name hierarchy** to an address in the **Internet Protocol (IP) address space**, and maintains these namespaces to avoid **naming conflicts**. It also allows address spaces to be **quickly updated**, allowing a service's location on the network to change without affecting the end users, who continue to use the same host name. 

The functionality of DNS is provided via a database service - thus, the DNS also specifies the technical functionality of its service: the **DNS protocol**, a detailed specification of the data structures and communication methods used in the DNS, as part of the Internet Protocol Suite.

Some key characteristics of the DNS are: 
- **Hierarchical**
  - For each domain, an authoritative name server is assigned. 
- **Distributed**
  - *This gives it high availability as a service across physical regions, and avoids service bottlenecks that would occur if all requests had to be directed to specific servers.*
- **Decentralized**
  - This makes it fault-tolerant; there is no central database that will 'break the internet' if it crashes. 

{% hint style="info" %}
### What is a name server?   
A DNS name server stores DNS records for a specific domain; it responds to queries looking for a specific domain name. Also known as "nameserver", "DNS server", etc. 
{% endhint %}

{% hint style="info" %}
### What is IP?  
{% endhint %}

{% hint style="info" %}
### What is IPv4 and IPv6? 
{% endhint %}

{% hint style="info" %}
### What is a name server?   
A DNS name server stores DNS records for a specific domain; it responds to queries looking for a specific domain name. 
{% endhint %}

{% hint style="info" %}
### What is the difference between URL and URI? 
{% endhint %}

## How might a typical DNS request be processed? 
The process of **DNS resolution** begins from the request made by a client, and involves 4 DNS servers, as such: **Client -> Recursor -> Root -> TLD -> Authoritative**.

1. **DNS recursor**
Receives initial query from client, and responsible for "recursively" making additional requests until it obtain the response, the correct IP address, which it then returns.  

AKA "recursive resolver", "recursive DNS resolver", etc. 

1. **Root nameserver**

2. **TLD nameserver**

3. **Authoritative nameserver**

{% hint style="info" %}
### What's the difference between an authoritative name server and a recursive DNS resolver? 
https://www.cloudflare.com/learning/dns/what-is-dns/ 
{% endhint %}

## What are some disadvantages?

## How is DNS implemented? 

- The Domain Name System is maintained by a **distributed database system**, which uses the **client–server model**. 
- The nodes of this database are the **name servers**. 
- Each domain has at least one **authoritative DNS server** that publishes information about that domain and name servers of any domains subordinate to it. 
- The top of the hierarchy is served by the **root name servers**, the servers to query when resolving a TLD.

## What are some managed DNS services?


## Sources:
- https://en.wikipedia.org/wiki/Domain_Name_System
- https://www.cloudflare.com/learning/dns/what-is-dns/
- http://www.steves-internet-guide.com/dns-guide-beginners/

{% hint style="info" %}
{% endhint %}

