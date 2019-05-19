# DNS

## What is DNS? 
The Domain Name System (DNS) is the phonebook of the Internet. 

It is a **naming system** that maps a user-friendly **"domain name"** (or "host name", or web address, or URL) of a computer/service/resource to a numerical **IP address**, so that a client can locate and interact wih it via underlying network protocols. 

For example, the domain name `www.example.com` might translate to the IP address `93.184.216.34` (under IPv4, or it might be `2606:2800:220:1:248:1893:25c8:1946` under IPv6 - see below). 

The DNS maps names from the **domain name hierarchy** to an address in the **Internet Protocol (IP) address space**, and maintains these namespaces to avoid **naming conflicts**. It also allows address spaces to be **quickly updated**, allowing a service's location on the network to change without affecting the end users, who continue to use the same host name. 

The functionality of DNS is provided via a distributed database service - thus, the **DNS protocol** specificies technical details such as data structures and communication methods used in the DNS.

Some key characteristics of the DNS are: 
- **Hierarchical**
  - For each domain, an authoritative name server is assigned. 
- **Distributed**
  - *This gives it high availability as a service across physical regions, and avoids service bottlenecks that would occur if all requests had to be directed to specific servers.*
- **Decentralized**
  - This makes it fault-tolerant; there is no central database that will 'break the internet' if it crashes. 

## How might a DNS request (or 'lookup') be processed?
The DNS doesn't always "translate" a hostname to an IP address immediately. Sometimes it has to repeatedly "resolve" intermediate, more general addresses until it obtains the final exact address. 

After that, though, results may be **cached** either in the client or some intermediate server (with some time-to-live expiration setting), which will make the process much faster. 

Thus, process of **DNS resolution** begins from the main request made by a client, and involves 4 DNS servers, as such: **Client -> Recursor -> Root -> TLD -> Authoritative**.  These entities communicate via the **client-server model**: clients make **requests** to servers in the form of **DNS queries**, expecting a **response**. 

{% hint style="info" %}
### What is a name server?   
A DNS name server simply stores DNS records for a specific domain; it responds to queries from clients looking for a specific domain name. A DNS recursor is not a name server, it's just a server, even though "DNS server" and "DNS name server" are sometimes used interchangeably. A DNS recursor also acts as a client on behalf of the user.  
{% endhint %}

{% hint style="info" %}
### What is a DNS query? 
A DNS query is made **from a DNS client (the browser) to a DNS server**, expecting a specific type of response. In a typical DNS lookup three types of queries occur. By using a combination of these queries, the process can be optimized. Ideally records will be cached, which allows DNS name servers to return a non-recursive query.

1. **Recursive query**
    Recursive DNS queries occur when a DNS client requests information from a DNS server that is set to query subsequent DNS servers until a definitive answer is returned to the client. The queries made to subsequent DNS servers from the recursor are iterative queries.
    
    Typically made from the browser to a DNS recursor. Requires either the **requested resource record or an error message**. 

2. **Iterative query**
   Iterative DNS queries are ones in which a DNS server is queried and returns an answer **without querying other DNS servers**. Even if it cannot provide a definitive answer i.e. an IP address, it will return a "best answer", i.e. a referral to a server for a lower-level domain namespace, or possibly an error. Also called a **non-recursive** query.

   Either a match, or a referral to a DNS server authoritative for a lower level of the domain namespace. The DNS client will then make a query to the referral address. This process continues with additional DNS servers down the query chain until either an error or timeout occurs.

   Typically made by a recursor to a name server. 

    
{% endhint %}

1. **DNS recursor**
    AKA "recursive resolver", "recursive DNS resolver", etc.
    Receives initial **recursive query** from client (browser), `wwww.example.com`. From here on, it acts as a client, making **iterative queries** to other servers on behalf of the user. 
    
    Goes to some root nameserver asking: where can I get help resolving queries for addresses in the top-level domain `com`?  

    - Receives initial **recursive query** from client, and is capable of making additional requests until it tracks down the correct **DNS record** in some authoritative nameserver and can return the correct IP address. 
    - It times out or returns an error if no record is found.


2. **Root nameserver**
    Replies "Ask this guy, he is in charge of `com`". Responds to recursor with address of the appropriate TLD server, since he knows all the TLD guys. 

3. **TLD nameserver**
    Receives query from recursor asking for the authoritative nameserver for the domain name `example`. Replies since he knows everything under `com`. 

4. **Authoritative nameserver** 
    Receives query from recurser asking for IP address for the domain name `example`. Returns IP address to recursor. 

Now that the browser has established a IP address via its DNS query, it can make **HTTP requests** to the IP address. 

## What are some disadvantages?

## What are some risks of recursive DNS queries? 
A DNS server that supports recursive resolution is vulnerable to DOS (denial of service) attacks, DNS cache poisoning, unauthorized use of resources, and root name server performance degradation.

**1. DOS attacks**
  - Servers supporting recursive DNS queries are vulnerable to phony requests that flood a particular IP address with the results of each server's query. This can overwhelm the IP address with a volume of traffic too large to be processed.
**2. DNS cache poisoning**
   - Cache poisoning results from someone tricking a DNS server into believing that a fake DNS query response is authentic. Because responses are normally cached, this false information can be distributed to users of that server.
**3. Unauthorized use of resources**
   - With recursive DNS queries enabled, a server is more easily hijacked and its performance compromised.
**4. Root name server performance degradation**
   - When DNS servers are not configured correctly, queries using RFC1918 addressing (also known as "private" addressing) may be leaked to the root name servers, causing a degradation in service for legitimate queries to those servers.

## What are some managed DNS services?


{% hint style="info" %}
### What is IP?  
{% endhint %}

{% hint style="info" %}
### What is IPv4 and IPv6? 
{% endhint %}

{% hint style="info" %}
### What's the difference between a recursive DNS query and a recursive DNS resolver? 
A recursive query is sent as a **request** to a **resolver**. A DNS recursive resolver resolves the query by making additional requests to other servers.
{% endhint %}

{% hint style="info" %}
### What is the difference between URL and URI? 
{% endhint %}

## Sources:
- https://en.wikipedia.org/wiki/Domain_Name_System
- https://www.cloudflare.com/learning/dns/what-is-dns/
- https://sg.godaddy.com/help/what-risks-are-associated-with-recursive-dns-queries-1184

{% hint style="info" %}
{% endhint %}

