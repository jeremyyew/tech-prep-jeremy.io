# Data Partitioning

## Why do we partition data? 

* Improve database performance. When data is distributed across databases in some manner, there is: 
  * less read and write traffic per server
  * less amount of replication for each server \(less replication lag\)
  * smaller index size, so faster read/writes 
  * more data that can fit in memory, so more cache hits due to improved cache locality

## What data partition schemes are there?

1. **Horizontal Partitioning**
   1. Basically, putting different rows into different tables/DB servers. 
   2. Also called data sharding/range-based partition. 
   3. Key problem: potentially imbalanced servers. 
2. **Vertical Partitioning \(Federation\)**
   1. Basically, putting data related to each distinct feature into different DB servers.
   2. However, with additional growth, it may still be necessary to further partition a feature specific DB across various servers. 
   3. Bonus: _when writing separate pieces of data to multiple DB's, we can write in parallel, increasing throughput._ 
3. **Directory Based Partitioning**
   1. A lookup service which abstracts the current partitioning scheme from DB access code.
   2. So, to find out where a particular data entity resides, we query the directory server that holds the mapping between each tuple key to its DB server. 
   3. We can add servers or change scheme without downtime or re-deployment of every app server. 

## What are some criteria or methods we can use to distribute data across partitions? 

1. **Key or Hash-based partitioning:**
   1. Apply a hash function to some key attributes of the entity we are storing to obtain a partition key. 
   2. For example, if we have 100 DB servers and our ID is a numeric value that gets incremented by one each time a new record is inserted. In this example, the hash function could be ‘ID % 100’. This approach should ensure a uniform allocation of data among servers. \(See **round-robin partitioning**\). 
   3. The fundamental problem is that it effectively fixes the total number of DB servers, since adding new servers means changing the hash function which would require redistribution of data and downtime for the service. 
   4. A workaround for this problem is to use Consistent Hashing.
2. **Round-robin partitioning:** 
   1. With `n` partitions, the `i` tuple is assigned to partition `(i mod n)`.
   2. Ensures uniform data distribution. 
   3. Key/hash-based is a more generic category, and could involve other hash functions, some of which will not ensure uniform distribution. 
3. **List partitioning**
   1. List of values for each partition. Data entries with specific values/attributes go to specific partition \(just a hardcoded mapping\). 
   2. For example, we can decide all users living in Iceland, Norway, Sweden, Finland, or Denmark will be stored in a partition for the Nordic countries.
4. **Composite partitioning**
   1. Combine above. 
   2. Eg. consistent hashing could be considered a composite of hash and list partitioning where the hash reduces the key space to a size that can be listed.

## What are some common challenges associated with data partitioning?

1. **Join operations**
   1.  **Join operations are inefficient when they must compile data from different servers.** Either you make the join in application code or use some built-in SQL feature, such as a server link.
   2. One solution is to denormalize data so that all the required data is still within one table. 
   3. Denormalization has its own issues, such as data inconsistency.
2.  **Data integrity**
   1. **Data integrity is also difficult to enforce across partitions.** 
   2. For example, foreign key constraints - a data value used to refer to another table must exist. 
   3. Most RDBMS do not support foreign keys constraints across databases on different database servers. So applications that require referential integrity often have to enforce it in application code; for example, running regular SQL jobs to clean up dangling references.
3. **Rebalancing partitions**
   1. **Rebalancing partitions often requires downtime.**  
   2. We might have to change our partitioning scheme to rebalance data and/or add servers due to: 
      1. Imbalanced distribution of data
      2. Imbalanced distribution of requests 
      3. Growth
   3. Usually downtime is required, since code to compute partition in every server needs to be changed. 
   4. Directory-based partitioning helps, but it also: 
      1. increases complexity  
      2. introduces new single point of failure

## **Sources:** 

* Grokking the System Design Interview

