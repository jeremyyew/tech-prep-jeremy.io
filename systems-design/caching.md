# Caching

## What is caching? 
Save result of a request for some amount of time, to be returned immediately on future requests. 

## At what levels of a service can we find caching?
- **Client caching**
  - Caches can be located on the client side (OS or browser), server side, or in a distinct cache layer.
- **CDN caching**
  - CDNs are considered a type of cache.
- **Web server caching**
  - Reverse proxies and caches such as Varnish can serve static and dynamic content directly. Web servers can also cache requests, returning responses without having to contact application servers.
- **Database caching**
  - Your database usually includes some level of caching in a **default configuration, optimized for a generic use case**. Tweaking these settings for specific usage patterns can further boost performance.
- **Application caching** 
  - In-memory caches such as Memcached and Redis are key-value stores **between your application and your data storage**. Since the data is held in RAM, it is much faster than typical databases where data is stored on disk. RAM is more limited than disk, so cache invalidation algorithms such as least recently used (LRU) can help invalidate 'cold' entries and keep 'hot' data in RAM.
  - Redis has the following additional features:
    - Persistence option
    - Built-in data structures such as sorted sets and lists
- **Caching at the database query level**
  - Whenever you query the database, hash the query as a key and store the result to the cache. This approach suffers from expiration issues:
    - Hard to delete a cached result with complex queries
    - If one piece of data changes such as a table cell, you need to delete all cached queries that might include the changed cell
- **Caching at the object level**
  - See your data as an object, similar to what you do with your application code. Have your application assemble the dataset from the database into a class instance or a data structure(s):
  - Remove the object from cache if its underlying data has changed
  - Allows for asynchronous processing: workers assemble objects by consuming the latest cached object
  - Suggestions of what to cache:
    - User sessions
    - Fully rendered web pages
    - Activity streams
    - User graph data

## What are some cache update strategies? 

### Cache-aside
### Write-through
### Write-behind
### Refresh-ahead

## Sources
https://github.com/donnemartin/system-design-primer#cache 