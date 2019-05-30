# Consistency, Availability, Partition Tolerance \(CAP\) \(TODO\)

## What is CAP?

{% hint style="info" %}
Only 2/3: **Consistency, Availability, and Partition tolerance.** But networks aren't reliable, so you'll need to support partition tolerance. You'll need to make a software tradeoff between **consistency and availability.**
{% endhint %}

1. **Consistency:** 
   * **"**All users see the same data at the same time". 
   * "Every read receives the most recent write or an error." / No user sees 'wrong' i.e. out-of-sync data. 
   * Consistency is achieved by updating several nodes before allowing further reads. 
2. **Availability:** 
   * "Every request gets a response on success/failure."
   * "Every request receives a response, without guarantee that it contains the most recent version of the information."
   * Availability is achieved by replicating the data across different servers.
   * Requests include writes: accept writes that can be processed later when the partition is resolved.
   * You can't return an error or timeout - you have to let the user do what they want to do \(ie read something, or write something\). 
   * Formally,  requests must be responded to eventually - there is no upper bound but it has to be finite. Notice how this is both a strong and a weak requirement. It's strong because 100% of the requests must return a response \(there's no 'degree of availability' here\), but weak because the response can take an unbounded \(but finite\) amount of time.
   * There seems to be two contexts of ensuring availability: 
     * "does your policy determine that in the case of network failure we always complete the request, even if it results in potentially inconsistent state?"
     * "does your architecture support failovers in the case of node failure?" 
3. **Partition tolerance:** 
   * "The system continues to work despite message loss or partial failure"
   * "The system continues to operate despite arbitrary partitioning due to network failures"
   * Data is sufficiently replicated across combinations of nodes and networks to keep the system up through intermittent outages.

![From Grokking the System Design Interview. The definition of availability seems off though. ](../../../.gitbook/assets/image%20%283%29.png)



<table>
  <thead>
    <tr>
      <th style="text-align:left">Use case</th>
      <th style="text-align:left">Consistency</th>
      <th style="text-align:left">Availability</th>
      <th style="text-align:left">Partition tolerance</th>
      <th style="text-align:left">Explanation/example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">In practice, never. Conceptually, in the case of network failure, behaviour
        is undefined. We either perpetually wait (no response, so neither consistent
        nor available) or we return something that might be wrong (available, inconsistent)
        or we return an error (consistent, unavailable).</td>
      <td style="text-align:left"><b>Yes</b>
      </td>
      <td style="text-align:left"><b>Yes</b>
      </td>
      <td style="text-align:left"><b>No </b>
      </td>
      <td style="text-align:left">
        <p>Generally everything works, as long as there are no network failures -
          it takes time for nodes to update each other, but this is deterministic.
          If the network fails, the system becomes partitioned into nodes that cannot
          communicate with each other (for some indefinite time).</p>
        <p><em>Example: User 1 requests to buy ticket 1, and is served by Node A. Usually when User 2 tries to buy a ticket (and is served by Node B), even if they initially see that ticket 1 is available, their purchase request would inform them that it is no longer available. If all of Node A&apos;s messages suddenly fail to send to Node B, what do we do? </em>
        </p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Atomic reads and writes, strong consistency.</td>
      <td style="text-align:left"><b>Yes</b>
      </td>
      <td style="text-align:left"><b>No</b>
      </td>
      <td style="text-align:left"><b>Yes</b>
      </td>
      <td style="text-align:left">To cope with possible network failure, we can stop serving requests from
        the out-of-date partition, but then the service is no longer 100% available.
        <br
        /><em>Example: On detection of network failure, we shut down Node B. User 2, who only has access to Node B, cannot have their service requests fulfilled, at least temporarily - they just get an error. </em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">When we are okay with eventual consistency, for the sake of high availability.</td>
      <td
      style="text-align:left"><b>No </b>
        </td>
        <td style="text-align:left"><b>Yes </b>
        </td>
        <td style="text-align:left"><b>Yes</b>
        </td>
        <td style="text-align:left">
          <p>We could just continue serving out-of-date data, but then it wouldn&apos;t
            be consistent.
            <br /><em>Example: Both Users 1 and 2 are allowed to buy ticket 1, and we will deal with the consequences, lol. </em>
          </p>
          <p></p>
        </td>
    </tr>
  </tbody>
</table>## What consistency patterns are there?

1. **Weak consistency \(not really consistent\)**
   1. After a write, reads may or may not see it. A best effort approach is taken.
   2. Memcached is weakly consistent, since it will sometimes have stale data \(without any write-through update strategy\). 
   3. Use cases: real time applications such as voice/video chats, streaming, realtime multiplayer games. 
2. **Eventual consistency \(async replication\)**
   1. After a write, reads will eventually see it \(typically within milliseconds\). Data is replicated asynchronously.
   2. Use cases: temporary inconsistencies are okay, availability is critical. 
3. **Strong consistency \(sync replication\)** 
   1. After a write, reads will see it. The write only completes after the replication. 
   2. Use cases: atomic transactions, e.g. file systems and RDBMSes.

## What availability patterns are there?

1. **Fail-over**
   1. **Active-passive**
      1. With active-passive fail-over, "heartbeats" are sent between the active and the passive server on standby. If the heartbeat is interrupted, the passive server takes over the active's IP address and resumes service.
      2. The length of downtime is determined by whether the passive server is already running in 'hot' standby or whether it needs to start up from 'cold' standby. Only the active server handles traffic.
      3. Active-passive failover can also be referred to as master-slave failover.
   2. **Active-active** 
      1. In active-active, both servers are managing traffic, spreading the load between them.
   3. **Disadvantages:** 
      1. Fail-over adds more hardware and additional complexity.
      2. There is a potential for loss of data if the active system fails before any newly written data can be replicated to the passive.
2. **Replication \(see replication and redundancy\)**

## Sources

* Grokking the System Design Interview
* [https://github.com/donnemartin/system-design-primer\#availability-vs-consistency](https://github.com/donnemartin/system-design-primer#availability-vs-consistency)





