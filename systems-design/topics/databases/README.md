# Databases \(TODO\)

## What is ACID? 

**ACID** is a set of properties of relational database [transactions](https://en.wikipedia.org/wiki/Database_transaction).

* **Atomicity** - Each transaction is all or nothing
* **Consistency** - Any transaction will bring the database from one valid state to another
* **Isolation** - Executing transactions concurrently has the same results as if the transactions were executed serially
* **Durability** - Once a transaction has been committed, it will remain so

## How can we scale a database?

1. **Replication**
   1. **master-replica replication**
      1. The master serves reads and writes, replicating writes to one or more slaves, which serve only reads. Slaves can also replicate to additional slaves in a tree-like fashion.
      2. If the master goes offline, the system can continue to operate in read-only mode until a slave is promoted to a master or a new master is provisioned.
      3. Disadvantages: 
         * The more read slaves, the more you have to replicate, which leads to greater replication lag.
         * Additional logic is needed to promote a slave to a master.
         * See [Disadvantage\(s\): replication](https://github.com/donnemartin/system-design-primer#disadvantages-replication). 
   2. **master-master replication**
      1. Both masters serve reads and writes and coordinate with each other on writes. If either master goes down, the system can continue to operate with both reads and writes.
      2. Disadvantages: 
         * You'll need a load balancer or you'll need to make changes to your application logic to determine where to write.
         * Most master-master systems are either loosely consistent \(violating ACID\) or have increased write latency due to synchronization.
         * See [Disadvantage\(s\): replication](https://github.com/donnemartin/system-design-primer#disadvantages-replication). 
   3. **Disadvantage\(s\): replication**
      * There is a potential for loss of data if the master fails before any newly written data can be replicated to other nodes.
      * Writes are replayed to the read replicas. If there are a lot of writes, the read replicas can get bogged down with replaying writes and can't do as many reads.
      * On some systems, writing to the master can spawn multiple threads to write in parallel, whereas read replicas only support writing sequentially with a single thread.
      * Replication adds more hardware and additional complexity.
2. **federation \(vertical partitioning\)**
3. **sharding \(horizontal partitioning\)**
4. **denormalization**
5. **SQL tuning**.

\*\*\*\*

## What is an ORM? 

