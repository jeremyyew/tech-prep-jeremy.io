# Redundancy and Replication \(TODO\)

## What is redundancy? 

{% hint style="info" %}
Basically, **having multiple copies** for backup and/or performance. Improves reliability but does not necessarily involve consistency. 
{% endhint %}

* [Redundancy](https://en.wikipedia.org/wiki/Redundancy_%28engineering%29) is the **duplication of critical components** or functions of a system with the intention of **increasing the reliability** of the system, usually in the form of a **backup or fail-safe**, or to **improve actual system performance.** 
* For example, if there is only one copy of a file stored on a single server, then losing that server means losing the file. Since losing data is seldom a good thing, we can create duplicate or redundant copies of the file to solve this problem.
* Redundancy plays a key role in **removing the single points of failure** in the system. For example, if we have two instances of a service running in production and one fails, the system can **failover** to the other one.

## What is replication?

{% hint style="info" %}
Basically, **keeping multiple components consistent** via updates. Redundancy is a property, replication is a feature that contributes to redundancy. 
{% endhint %}

* [Replication](https://en.wikipedia.org/wiki/Replication_%28computing%29) means **sharing information to ensure consistency between redundant resources**, such as software or hardware components, to improve **reliability,** [**fault-tolerance**](https://en.wikipedia.org/wiki/Fault_tolerance)**, or accessibility.**
* Replication is widely used in many database management systems \(DBMS\), usually with a master-slave relationship between the original and the copies. The master gets all the updates, which then ripple through to the slaves. Each slave outputs a message stating that it has received the update successfully, thus allowing the sending of subsequent updates.

**Disadvantage\(s\): replication**

* There is a potential for loss of data if the master fails before any newly written data can be replicated to other nodes.
* Writes are replayed to the read replicas. If there are a lot of writes, the read replicas can get bogged down with replaying writes and can't do as many reads.
* The more read slaves, the more you have to replicate, which leads to greater replication lag.
* On some systems, writing to the master can spawn multiple threads to write in parallel, whereas read replicas only support writing sequentially with a single thread.
* Replication adds more hardware and additional complexity.

## What are some examples of services that provide redundancy and/or replication, as well as some that don't? 

## Sources

* Grokking the System Design Overview 

