# Consistency, Availability, Partition Tolerance \(CAP\) \(TODO\)

## What is CAP?

{% hint style="info" %}
It is impossible for a distributed software system to simultaneously provide more than two out of three of the following guarantees: **Consistency, Availability, and Partition tolerance.**
{% endhint %}

**Consistency:** All users see the same data at the same time. Consistency is achieved by updating several nodes before allowing further reads.

**Availability:** Every request gets a response on success/failure. Availability is achieved by replicating the data across different servers.

**Partition tolerance:** The system continues to work despite message loss or partial failure. A system that is partition-tolerant can sustain any amount of network failure that doesn’t result in a failure of the entire network. Data is sufficiently replicated across combinations of nodes and networks to keep the system up through intermittent outages.

![From Grokking the System Design Interview.](../../../.gitbook/assets/image%20%283%29.png)

<table>
  <thead>
    <tr>
      <th style="text-align:left">Consistency</th>
      <th style="text-align:left">Availability</th>
      <th style="text-align:left">Partition tolerance</th>
      <th style="text-align:left">Explanation/example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
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
          communicate with each other (for some indefinite time). Updates in one
          partition might not make it to the other partitions before a client reads
          from the out-of-date partition after having read from the up-to-date one.</p>
        <p><em>Example: User 1 requests to buy ticket 1, and is served by Node A. Usually when User 2 tries to buy a ticket (and is served by Node B), even if they initially see that ticket 1 is available, their purchase request would inform them that it is no longer available. If all of Node A&apos;s messages suddenly fail to send to Node B, User 2 reading from Node B will never know that ticket 1 is no longer available. </em>
        </p>
      </td>
    </tr>
    <tr>
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
      <td style="text-align:left"><b>No </b>
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
</table>## What is consistency? What patterns of consistency are there? When should we use each?

## What is availability? What patterns of availability are there? When should we use each? 

## What is partition tolerance?

## When should we use CP?

## When should we use AP?

## Sources

* Grokking the System Design Interview
* [https://github.com/donnemartin/system-design-primer\#availability-vs-consistency](https://github.com/donnemartin/system-design-primer#availability-vs-consistency)





