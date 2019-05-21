# Caching

## What is caching?

Save result of a request for some amount of time, to be returned immediately on future requests.

## At what levels of a service can we find caching?

* **Client caching**
  * Caches can be located on the client side \(OS or browser\), server side, or in a distinct cache layer.
* **CDN caching**
  * CDNs are considered a type of cache.
* **Web server caching**
  * Reverse proxies and caches such as Varnish can serve static and dynamic content directly. Web servers can also cache requests, returning responses without having to contact application servers.
* **Database caching**
  * Your database usually includes some level of caching in a **default configuration, optimized for a generic use case**. Tweaking these settings for specific usage patterns can further boost performance.
* **Application caching** 
  * In-memory caches such as Memcached and Redis are key-value stores **between your application and your data storage**. Since the data is held in RAM, it is much faster than typical databases where data is stored on disk. RAM is more limited than disk, so cache invalidation algorithms such as least recently used \(LRU\) can help invalidate 'cold' entries and keep 'hot' data in RAM.
  * **Redis** has the following additional features:
    * Persistence option
    * Built-in data structures such as sorted sets and lists

## What are some cache update strategies?

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
          <img src="../.gitbook/assets/image (2).png" alt="Cache Aside" />
        </p>
      </td>
      <td style="text-align:left">
        <img src="../.gitbook/assets/image (7).png" alt="Cache Aside" />
      </td>
      <td style="text-align:left">
        <img src="../.gitbook/assets/image (5).png" alt="Cache Aside" />
      </td>
      <td style="text-align:left">
        <img src="../.gitbook/assets/image (12).png" alt="Cache Aside" />
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Advantages</b>
      </td>
      <td style="text-align:left">
        <ul>
          <li><b>Quick reads for frequently-accessed data. </b>
          </li>
        </ul>
      </td>
      <td style="text-align:left">
        <p></p>
        <ul>
          <li><b>Cached data never stale. </b>
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
          <li>If most written data is <b>never/seldom read,</b> the caching is useless.
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
      <td style="text-align:left">Improve read time for frequently requested data.</td>
      <td style="text-align:left">Improve read time for recently-updated data, and eliminate stale data.</td>
      <td
      style="text-align:left">Improve write time while maintaining benefits of write-through.</td>
        <td
        style="text-align:left">Improve read time for data with predictable request frequencies or patterns.</td>
    </tr>
  </tbody>
</table>## What is the difference between query-level and object-level caching?

* **Caching at the database query level**
  * Whenever you query the database, hash the query as a key and store the result to the cache. This approach suffers from expiration issues:
    * Hard to delete a cached result with complex queries
    * If one piece of data changes such as a table cell, you need to delete all cached queries that might include the changed cell
  * **Caching at the object level**
    * See your data as an object, similar to what you do with your application code. Have your application assemble the dataset from the database into a class instance or a data structure\(s\):
    * Remove the object from cache if its underlying data has changed
    * Allows for asynchronous processing: workers assemble objects by consuming the latest cached object
    * Suggestions of what to cache:
      * User sessions
      * Fully rendered web pages
      * Activity streams
      * User graph data



## Sources

[https://github.com/donnemartin/system-design-primer\#cache](https://github.com/donnemartin/system-design-primer#cache)

