# Caching

## What is caching?

Saving the result of some computation/query/request, for some amount of time or until we run out of space, to be returned immediately on future requests. 

## What are some examples of caching?

In the context of system design we will usually talk about server-side caching, and most often it will be **CDN's** and **database/application caching.**

In the context of **CDN's,** usually we cache to offload requests from our server. ****

In the context of **database/application** caching, usually we cache to offload reads from database in general - this improves spike tolerance, and also allows easier and cheaper scaling. 

* **Client caching**
  * OS or browser cache. 
* **CDN caching**
  * CDNs are considered a type of cache.
* **Web server caching**
  * Reverse proxies and caches such as Varnish can serve static and dynamic content directly. Web servers can also cache requests, returning responses without having to contact application servers.
* **Database caching**
  * Your database usually includes some level of caching in a **default configuration, optimized for a generic use case**. Tweaking these settings for specific usage patterns can further boost performance.
* **Application caching** \(see below\)
  * There are general strategies for applications reading and writing to caches, outlined below. 
  * In-memory caches such as Memcached and Redis are key-value stores **between your application and your data storage**. 
    * Since the data is held in RAM, it is much faster than typical databases where data is stored on disk. 
    * But RAM is more limited than disk, so we need to keep only the most frequently accessed data in memory. One common example is LRU, which is almost always appropriate. 

## What are some cache update strategies \(for application caching\)?

<table>
  <thead>
    <tr>
      <th style="text-align:left">Strategy</th>
      <th style="text-align:left"><b>1.Cache-aside</b>
      </th>
      <th style="text-align:left"><b>2. Write-through</b>
      </th>
      <th style="text-align:left"><b>3. Write-behind/write-back</b>
      </th>
      <th style="text-align:left"><b>4. Refresh-ahead</b>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left"><b>Description</b>
      </td>
      <td style="text-align:left">
        <p>To read:</p>
        <ol>
          <li><b>Lookup</b> cache.</li>
          <li><b>Query</b> DB if missed.</li>
          <li><b>Cache</b> entry.</li>
          <li><b>Return</b> value.</li>
        </ol>
        <p><em>Also known as &apos;lazy caching&apos;, or &apos;lazy population&apos;.</em>
        </p>
      </td>
      <td style="text-align:left">
        <p>To write:</p>
        <ol>
          <li><b>App</b> write to <b>Cache. </b>
          </li>
          <li><b>Cache</b> write to <b>DB (sync).</b>
          </li>
        </ol>
      </td>
      <td style="text-align:left">
        <p>To write:</p>
        <ol>
          <li><b>App </b>write to <b>Cache.</b>
          </li>
          <li><b>Cache</b> writes to <b>Queue.</b>
          </li>
        </ol>
        <p>Asynchronously,</p>
        <ol>
          <li>Event processor writes from <b>queue to DB. </b>
          </li>
        </ol>
      </td>
      <td style="text-align:left">
        <p>Whenever entry expires:</p>
        <ol>
          <li>Cache<b> automatically reads</b> from DB and<b> updates entry, based on prediction of necessity. </b>
          </li>
        </ol>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Diagram</b>
      </td>
      <td style="text-align:left">
        <p></p>
        <p>
          <img src="../../.gitbook/assets/image (5).png" alt="Cache Aside" />
        </p>
      </td>
      <td style="text-align:left">
        <img src="../../.gitbook/assets/image (11).png" alt="Cache Aside" />
      </td>
      <td style="text-align:left">
        <img src="../../.gitbook/assets/image (9).png" alt="Cache Aside" />
      </td>
      <td style="text-align:left">
        <img src="../../.gitbook/assets/image (18).png" alt="Cache Aside" />
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Advantages</b>
      </td>
      <td style="text-align:left">
        <ul>
          <li><b>Quick reads for frequently-accessed data. </b>
          </li>
          <li>Cache only contains objects that the application actually requests, which
            helps keep the cache size manageable.</li>
          <li>Cache expiration easily handled by simply deleting the cached object.</li>
        </ul>
      </td>
      <td style="text-align:left">
        <p></p>
        <ul>
          <li><b>Cached data never stale. </b>
          </li>
          <li><b>Avoids cache misses for recently updated data. </b>
          </li>
          <li><b>Shifts latency to write (users generally more tolerant of write latency than read) </b>
          </li>
        </ul>
      </td>
      <td style="text-align:left">
        <ul>
          <li><b>Faster writes than write-through. </b>
          </li>
        </ul>
      </td>
      <td style="text-align:left">
        <ul>
          <li><b>Faster reads</b> if predictions are accurate.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Disadvantages</b>
      </td>
      <td style="text-align:left">
        <p></p>
        <ol>
          <li><b>Three trips if cache miss,</b> which can cause noticeable delay.</li>
          <li><b>Cached data might be stale. </b>
            <ul>
              <li>Mitigate by setting<b> time-to-live (TTL)</b>,<b> </b>or using<b> write-through.</b>
              </li>
            </ul>
          </li>
          <li>When a node fails, it is replaced by a new empty node, increasing latency.</li>
        </ol>
      </td>
      <td style="text-align:left">
        <p></p>
        <ol>
          <li><b>Slower</b> than directly writing to DB.
            <ul>
              <li>However, users generally more tolerant of write latency than read.</li>
            </ul>
          </li>
          <li>When a new node is created due to failure or scaling, it <b>will never cache entries until entry is updated</b> in
            the database.
            <ul>
              <li>Mitigate by using cache-aside in conjunction.</li>
            </ul>
          </li>
          <li>If most written data is <b>never/seldom read,</b> the caching is useless
            (useless cache churn).
            <ul>
              <li>Mitigate with appropriate TTL.</li>
            </ul>
          </li>
        </ol>
      </td>
      <td style="text-align:left">
        <ol>
          <li><b>Data loss</b> if cache or queue dies before writes go to DB.
            <ol>
              <li>With synchronous write-through, if cache dies incomplete writes raise
                error at app level.</li>
            </ol>
          </li>
          <li><b>Harder to implement</b> than previous two.</li>
        </ol>
      </td>
      <td style="text-align:left">
        <ol>
          <li><b>Slower</b> reads if predictions are inaccurate.</li>
          <li>Need to <b>maintain consistency </b>via <a href="https://en.wikipedia.org/wiki/Cache_algorithms">cache invalidation</a>,
            which is complex.</li>
        </ol>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Use cases</b>
      </td>
      <td style="text-align:left">Improve read time for frequently requested data (ideally relatively infrequently
        updated)</td>
      <td style="text-align:left">Improve read time for recently-updated data, and eliminate stale data.</td>
      <td
      style="text-align:left">Improve write time while maintaining benefits of write-through.</td>
        <td
        style="text-align:left">Improve read time for data with predictable request frequencies or patterns.</td>
    </tr>
  </tbody>
</table>> It's often best to think of lazy caching as a foundation that you can use throughout your app, and write- through caching as a targeted optimization that you apply to specific situations. [https://d0.awsstatic.com/whitepapers/performance-at-scale-with-amazon-elasticache.pdf](https://d0.awsstatic.com/whitepapers/performance-at-scale-with-amazon-elasticache.pdf).

## What is the "thundering herd" effect? 

Also known as dog piling, the thundering herd effect is what happens when many different application processes **simultaneously request a cache key, get a cache miss, and then each hits the same database query in parallel.** The more expensive this query is, the bigger impact it has on the database. If the query involved is a top 10 query that requires ranking a large dataset, the impact can be a significant hit. 

One problem with adding TTLs to all of your cache keys is that it can exacerbate this problem. For example, let's say millions of people are following a popular user on your site. That user hasn't updated his profile or published any new messages, **yet his profile cache still expires due to a TTL**. Your database might suddenly be swamped with a series of identical queries. 

TTLs aside, this effect is also common when **adding a new cache node**, because the new cache node's memory is empty. 

In both cases, the solution is to **prewarm the cache** by following these steps:

1. Write a script that performs the same requests that your application will. If it's a web app, this script can be a shell script that hits a set of URLs.
2. If your app is set up for lazy caching, cache misses will result in cache keys being populated, and the new cache node will fill up.
3. When you add new cache nodes, run your script before you attach the new node to your application. Because your application needs to be

   reconfigured to add a new node to the consistent hashing ring, insert this script as a step before triggering the app reconfiguration.

4. If you anticipate adding and removing cache nodes on a regular basis,

   prewarming can be automated by triggering the script to run whenever

   your app receives a cluster reconfiguration event through Amazon Simple Notification Service \(Amazon SNS\).

Finally, there is one last subtle side effect of using TTLs everywhere. **If you use the same TTL length** \(say 60 minutes\) consistently, then many of your cache keys might **expire within the same time window**, even after prewarming your cache. One strategy that's easy to implement is to **add some randomness** to your TTL: ttl = 3600 + \(rand\(\)  _120\) /_ +/- 2 minutes \*/ The good news is that only sites at large scale typically have to worry about this level of scaling problem. It's good to be aware of, but it's also a good problem to have.

Also from [https://d0.awsstatic.com/whitepapers/performance-at-scale-with-amazon-elasticache.pdf](https://d0.awsstatic.com/whitepapers/performance-at-scale-with-amazon-elasticache.pdf)

## What data should we cache?

1. **Consistency**
   * Is it safe to use a cached value? **The same piece of data can have different consistency requirements in different contexts**. For example, during online checkout, you need the authoritative price of an item, so caching might not be appropriate. On other pages, however, the price might be a few minutes out of date without a negative impact on users. 
2. **Update Frequency**
   * Is caching effective for that data? Some applications generate access patterns that are not suitable for caching—for example, sweeping through the key space of a large dataset that is changing frequently. In this case, **keeping the cache up to date could offset any advantage caching could offer.** 
3. **Data structure** 
   * Is the data structured well for caching? Simply caching a database record can often be enough to offer significant performance advantages. However, **sometimes data is best cached in a format that combines multiple records together.** Because caches are simple key-value stores, **you might also need to cache a data record in multiple different formats,** so you can access it by different attributes in the record.

In general, cache \(almost\) everything. 

* It might seem as if you should only cache your heavily hit database queries and expensive calculations, but that other parts of your app might not benefit from caching. 
* In practice, in-memory caching is widely useful, because **it is much faster to retrieve a flat cache key from memory than to perform even the most highly optimized database query or remote API call.**
* Just keep in mind that cached data is stale data by definition, meaning there may be cases where it’s not appropriate, such as accessing an item’s price during online checkout. You can monitor statistics like cache misses to see whether your cache is effective. 

## What is the difference between database/query caching and object caching? TODO. 

* **Caching at the database query level**
  * Whenever you query the database, hash the query as a key and store the result to the cache. This approach suffers from expiration issues:
    * Hard to delete a cached result with complex queries. Why? 
    * If one piece of data changes such as a table cell, you need to delete all cached queries that might include the changed cell
  * **Caching at the object level**
    * See your data as an object, similar to what you do with your application code. Have your application assemble the dataset from the database into a class instance or a data structure\(s\):
    * Remove the object from cache if its underlying data has changed
    * Allows for asynchronous processing: workers assemble objects by consuming the latest cached object.

## When to us Memcached vs Redis? 

| Feature/Metric | Memcached | Redis |
| :--- | :--- | :--- |
| Simplicity | Yes | ? |
| Persistence  | No | Yes |
| Atomic increment/decrement | Yes | Yes |
| Advanced data types | ?  | lists, hashes, and sets  |
| Sort/rank  | ? | Yes |
| Pub/Sub | ? | Yes |
| Horizontal sharding | Yes | No \(at least not with Amazon ElastiCache\) |

**Use Memcached if you need:**

* object caching as primary goal, for example to offload your database
* a simple a caching model as possible
* running large cache nodes, and multithreaded performance with utilization of multiple cores
* ability to scale your cache horizontally as you grow

**Use Redis if you need:**

* persistence of key store
* advanced data types, such as lists, hashes, and sets 
* sorting and ranking datasets in memory 
* publish and subscribe \(pub/sub\) capabilities

Additional differences?: 

* Redis data structures **cannot be horizontally sharded**. As a result, Redis ElastiCache clusters are always a single node, rather than the multiple nodes we saw with Memcached.
* Redis **supports replication**, both for high availability and to separate read workloads from write workloads. A given ElastiCache for Redis primary node can have one or more replica nodes. A Redis primary node can handle both reads and writes from the app. Redis replica nodes can only handle reads, similar to Amazon RDS Read Replicas.
* Because Redis supports replication, you can also fail over from the primary node to a replica in the event of failure. You can configure ElastiCache for Redis to automatically fail over by using the Multi-AZ feature. 
* Redis supports persistence, including backup and recovery. However, because Redis replication is asynchronous, you cannot completely guard against data loss in the event of a failure. We will go into detail on this topic in our discussion of Multi-AZ.

## Sources

* [https://github.com/donnemartin/system-design-primer\#cache](https://github.com/donnemartin/system-design-primer#cache)
* [https://lethain.com/introduction-to-architecting-systems-for-scale/](https://lethain.com/introduction-to-architecting-systems-for-scale/)
* [https://d0.awsstatic.com/whitepapers/performance-at-scale-with-amazon-elasticache.pdf](https://d0.awsstatic.com/whitepapers/performance-at-scale-with-amazon-elasticache.pdf)

## Read More: 

* [https://aws.amazon.com/caching/](https://aws.amazon.com/caching/)



