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
   2. **master-master replication**
      1. Both masters serve reads and writes and coordinate with each other on writes. If either master goes down, the system can continue to operate with both reads and writes.
      2. Disadvantages: 
         * You'll need a load balancer or you'll need to make changes to your application logic to determine where to write.
         * Most master-master systems are either loosely consistent \(violating ACID\) or have increased write latency due to synchronization.
   3. Disadvantages of replication: See Redundancy and Replication. 
2. **Federation \(vertical partitioning\)**
   1. Splits up databases by function. See Data Partitioning. 
3. **Sharding \(horizontal partitioning\)**
   1. See Data Partitioning. 
4. **Denormalization**
   1. Redundant copies of the data are written in multiple tables to avoid expensive joins.
   2. Improve read performance at the expense of some write performance. 
   3.  Some RDBMS help do it automatically, via [materialized views](https://en.wikipedia.org/wiki/Materialized_view) \(which are really just cached tables/query results\). 
   4. _Use to avoid complex/expensive queries across distributed servers, and especially when read-heavy._ 
   5. **Disadvantage\(s\): denormalization**
      1. Data is duplicated.
      2. Constraints can help redundant copies of information stay in sync, but increases complexity of the database design.
5. **SQL tuning**
   1. **Benchmark** and **profile** to simulate and uncover **bottlenecks.**
      1. **Benchmark** - Simulate high-load situations with tools such as [ab](http://httpd.apache.org/docs/2.2/programs/ab.html).
      2. **Profile** - Enable tools such as the [slow query log](http://dev.mysql.com/doc/refman/5.7/en/slow-query-log.html) to help track performance issues. 
   2. Potential optimizations:
      1. **Tighten up the schema**
         * MySQL dumps to disk in contiguous blocks for fast access.
         * Use `CHAR` instead of `VARCHAR` for fixed-length fields.
           * `CHAR` effectively allows for fast, random access, whereas with `VARCHAR`, you must find the end of a string before moving onto the next one.
         * Use `TEXT` for large blocks of text such as blog posts. `TEXT` also allows for boolean searches. Using a `TEXT` field results in storing a pointer on disk that is used to locate the text block.
         * Use `INT` for larger numbers up to 2^32 or 4 billion.
         * Use `DECIMAL` for currency to avoid floating point representation errors.
         * Avoid storing large `BLOBS`, store the location of where to get the object instead.
         * `VARCHAR(255)` is the largest number of characters that can be counted in an 8 bit number, often maximizing the use of a byte in some RDBMS.
         * Set the `NOT NULL` constraint where applicable to [improve search performance](http://stackoverflow.com/questions/1017239/how-do-null-values-affect-performance-in-a-database-search).
      2. **Use good indices**
         * See "Indexing". 
      3. **Avoid expensive joins**
         * [Denormalize](https://github.com/donnemartin/system-design-primer#denormalization) where performance demands it.
      4. **Partition tables**
         * Break up a table by putting hot spots in a separate table to help keep it in memory.
      5. **Tune the query cache**
         * In some cases, the [query cache](https://dev.mysql.com/doc/refman/5.7/en/query-cache.html) could lead to [performance issues](https://www.percona.com/blog/2016/10/12/mysql-5-7-performance-tuning-immediately-after-installation/).

\*\*\*\*

## What is an ORM? 

