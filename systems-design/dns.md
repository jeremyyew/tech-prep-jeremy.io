# DNS

## What is DNS?

The Domain Name System \(DNS\) is the phonebook of the Internet.

It is a **naming system** that maps a user-friendly **"domain name"** \(or "host name", or web address, or URL\) of a computer/service/resource to a numerical **IP address**, so that a client can locate and interact wih it via underlying network protocols.

For example, the domain name `www.example.com` might translate to the IP address `93.184.216.34` \(under IPv4, or it might be `2606:2800:220:1:248:1893:25c8:1946` under IPv6 - see below\).

The DNS maps names from the **domain name hierarchy** to an address in the **Internet Protocol \(IP\) address space**, and maintains these namespaces to avoid **naming conflicts**. It also allows address spaces to be **quickly updated**, allowing a service's location on the network to change without affecting the end users, who continue to use the same host name.

The functionality of DNS is provided via a distributed database service - thus, the **DNS protocol** specificies technical details such as data structures and communication methods used in the DNS.

Some key characteristics of the DNS are: 
- **Hierarchical**
  - TODO.
- **Distributed**
  - TODO.
  - *This gives it high availability as a service across physical regions, and avoids service bottlenecks that would occur if all requests had to be directed to specific servers.*
- **Decentralized**
  - TODO.
  - This makes it fault-tolerant; there is no central database that will 'break the internet' if it crashes. 

## How might a DNS request \(or 'lookup'\) be processed?

The DNS doesn't always "translate" a hostname to an IP address immediately. Sometimes it has to repeatedly "resolve" intermediate, more general addresses until it obtains the final exact address.

After that, though, results may be **cached** either in the client or some intermediate server \(with some time-to-live expiration setting\), which will make the process much faster.

Thus, process of **DNS resolution** from an empty cache begins from the main request made by a client, and involves 4 DNS servers, as such: **Client -&gt; Recursor -&gt; Root -&gt; TLD -&gt; Authoritative**. These entities communicate via the **client-server model**: clients make **requests** to servers in the form of **DNS queries**, expecting a **response**.

{% hint style="info" %}
### What is a name server?

A DNS name server simply stores DNS records for a specific domain; it responds to queries from clients looking for a specific domain name. A DNS recursor is not a name server, it's just a server, even though "DNS server" and "DNS name server" are sometimes used interchangeably. A DNS recursor also acts as a client on behalf of the user.
{% endhint %}

{% hint style="info" %}
### What is a DNS query?

A DNS query is made **from a DNS client \(the browser\) to a DNS server**, expecting a specific type of response. In a typical DNS lookup two types of queries occur. By using a combination of these queries, the process can be optimized. Ideally records will be cached, which allows DNS name servers to return a non-recursive query.

1. **Recursive query** Recursive DNS queries occur when a DNS client requests information from a DNS server that is set to query subsequent DNS servers until a definitive answer is returned to the client. The queries made to subsequent DNS servers from the recursor are iterative queries.

   Typically made from the browser to a DNS recursor. Requires either the **requested resource record or an error message**.

2. **Iterative query** Iterative DNS queries are ones in which a DNS server is queried and returns an answer **without querying other DNS servers**. Even if it cannot provide a definitive answer i.e. an IP address, it will return a "best answer", i.e. a referral to a server for a lower-level domain namespace, or possibly an error. Also called a **non-recursive** query.

   Either a match, or a referral to a DNS server authoritative for a lower level of the domain namespace. The DNS client will then make a query to the referral address. This process continues with additional DNS servers down the query chain until either an error or timeout occurs.

1. **DNS recursor** AKA "recursive resolver", "recursive DNS resolver", etc.
    > Goes to any one of 13 root name servers, asking: "Who do I go to to get the IP address of `jeremys-blog.blogger.com`"?  
    
    - Receives initial **recursive query** from client. From here on, it acts as a client, making **iterative queries** to other servers on behalf of the user until it tracks down the correct **DNS record** in some authoritative nameserver and can return the correct IP address.
    - It times out or returns an error if no record is found.

2. **Root nameserver**
    > Replies to resolver: "Ok, I have the list of all TLD servers. The guy in charge of `.com` is at this address, go ask him". 
    - There are 13 independently maintained DNS root nameservers, and all of them are known to every recursive resolver (installed in system). **Each of them hold an identical list of TLD servers, they are there for redundancy**.
    - A root nameserver responds to a resolver's query by directing the recursive resolver to a TLD nameserver, based on the extension of the domain name requested (.com, .net, .org, etc.). 
    - There are 13 types of root nameservers, but lots of instances all over the world, which use a system called **Anycast routing** to provide speedy responses.
    - The root nameservers are overseen by a nonprofit called the Internet Corporation for Assigned Names and Numbers (ICANN).

3. **TLD nameserver**
    > Replies to resolver: "Yes I am the authority for `.com`. Here is the address of the server of the company who owns `blogger.com`, go ask them.  

4. **Authoritative nameserver** 
    > Replies to resolver: "Yes I am the company that owns blogger.com, this nameserver is where I store the address of my web server that will be able to serve you content from jeremys-blog.blogger.com."
    - Can delegate, IN ANY WAY THEY WANT, ANYTHING to the LEFT of the Domain Name they own (were delegated). That means they can either give you the IP address of the server that can directly serve your request, or refer you to a sub-delegated nameserver. 

Eventually once the resolver has established a IP address via its DNS query and returned that to the browser, the browser can make **HTTP requests** to that IP address. 

## How does DNS caching work?

Both the **browser and OS** will cache DNS records, and both will be checked before the query is sent out to a **recursive resolver**, which also has a cache with special features.

1. **Modern web browsers** are designed by default to cache DNS records for a set amount of time. When a query is made, the browser cache is the **first** location checked for the requested record.
2. **The operating system level DNS resolver** is the **second and last** local stop before a DNS query leaves your machine. The process inside your operating system that is designed to handle this query is commonly called a **“stub resolver” or DNS client**. Only if we get a cache miss does it send a DNS query \(with a recursive flag set\), outside the local network to a DNS recursive resolver inside the Internet service provider \(ISP\).
3. **The DNS recursive resolver** has its own cache. It can skip some levels of querying depending on what kind of records it has: 
   * If the resolver does not have the A records, but does have the **NS records** for the authoritative nameservers, it will query those servers directly.
   * If the resolver does not have the NS records, it will usually have the **TLD records** and will send a query directly to the TLD servers, skipping the root server. 
   * Otherwise it will query the **root servers** - but this typically occurs after a DNS cache has been purged.

## What are some risks of recursive DNS queries?

## What are some disadvantages of DNS in general?
TODO. 

## What are some risks of recursive DNS queries? 
A DNS server that supports recursive resolution is vulnerable to DOS (denial of service) attacks, DNS cache poisoning, unauthorized use of resources, and root name server performance degradation.

**1. DOS attacks**

* Servers supporting recursive DNS queries are vulnerable to phony requests that flood a particular IP address with the results of each server's query. This can overwhelm the IP address with a volume of traffic too large to be processed.

**2. DNS cache poisoning**

* Cache poisoning results from someone tricking a DNS server into believing that a fake DNS query response is authentic. Because responses are normally cached, this false information can be distributed to users of that server.

**3. Unauthorized use of resources**

* With recursive DNS queries enabled, a server is more easily hijacked and its performance compromised.

**4. Root name server performance degradation**

## What are some managed DNS services?
TODO. 

{% hint style="info" %}
### What is IP?  
TODO. 
{% endhint %}

{% hint style="info" %}
### What is IPv4 and IPv6? 
TODO. 
{% endhint %}

{% hint style="info" %}
### What is the difference between URL and URI? 
TODO. 
{% endhint %}

## Sources:

* [https://en.wikipedia.org/wiki/Domain\_Name\_System](https://en.wikipedia.org/wiki/Domain_Name_System)
* [https://www.cloudflare.com/learning/dns/what-is-dns/](https://www.cloudflare.com/learning/dns/what-is-dns/)
* [https://sg.godaddy.com/help/what-risks-are-associated-with-recursive-dns-queries-1184](https://sg.godaddy.com/help/what-risks-are-associated-with-recursive-dns-queries-1184)
* [http://www.zytrax.com/books/dns/ch2/](http://www.zytrax.com/books/dns/ch2/)
* [https://www.home.neustar/blog/recursive-dns-what-it-is-and-why-you-should-care](https://www.home.neustar/blog/recursive-dns-what-it-is-and-why-you-should-care)
* [https://www.cloudflare.com/learning/dns/dns-server-types/](https://www.cloudflare.com/learning/dns/dns-server-types/)


