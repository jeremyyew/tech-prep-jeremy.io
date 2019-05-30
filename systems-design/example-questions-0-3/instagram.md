# Instagram

## Scoping

1. Use cases
   1. **Post photos or videos \(single only, can edit and delete\)**
   2. **Follow other users \(assume all public\)**
   3. **View posts of followed users**
   4. **Search posts by user/caption**
   5. Some out-of-scope:
      1. Private/public, DM, likes, comments, explore feed, hashtags, mentions, ranking algorithms, stories, tagging 
2. Platform
   1.  Mobile app 
      1. Considerations - if you use local cache, remember you have to update if you're logging in on multiple devices. Besides on log in,  you could perhaps request updates app startup. 
3. Traffic
   * 500 million users total, 1m active daily, 2 posts a day 
   * 2M new photos every day = 2 x 10^6 / 8 \* 10^4 = 2/8 x 10^2  = ~25 photos per second.
   * Average photo file size =&gt; 200KB. 
   * One byte is 8 bits. after that, kb, mb, gb, tb, pt are increasing 2^10 or 10^3. 
   * One TB is about **2^40 or 10^12 bytes.** 
   * Total space for 1 day:  
     * **2M \* 200KB =&gt;  200KB \* 2 \* 10^6 = 400GB.**
   * Total space for 10 years:  
     * **400GB  \* 365 \* 10 = 1.4 X 10^6 GB  = 1.4 x 10^4 TB ~=** 1425TB
   * Read-write ratio: At least 10 views per 1 post. 

## **Design Goals**

1. Highly available, low latency 
2. Eventual consistency is fine 
3. Reliability - never lose posts
4. Unlimited storage 

## **DB/Schema**

```text
Users {
    id 
    username
    email 
}

Follows {
    followed_id
    following_id
}

Posts {
    id 
    path
    type
    timestamp
    caption
} 
```

## Request flow 

1. **Post photo or video \(single only, can edit and delete\)**
   1. Add entry in posts DB \(write-through\). 
   2. Upload photo to object storage \(write-through, but can also consider async i.e. write-behind\), with key as media\_id. 
2. **Follow other users \(assume all public\)**
   1. Add entry in Follows \(maybe write-through, but doesnt seem important since the device local cache wont. But perhaps cache-aside will be useful so that highly-followed users' list will be updated for everyone to see? Not that important either it seems\). 
   2. Check for changes on app startup. 
   3. Load all on login. 
3. **View posts of followed users**
   1. Request for new \(non-loaded\) posts, most recent only 
   2. Server gets followed users. 
   3. Server gets all posts. 
   4. Server returns posts synchronously. 
   5. App displays posts.
      1. Async loads images/videos by requesting from object storage CDNs using media\_ids. 
      2. For posts with images already has loaded, check if version number has changed. If so, re-load from object storage. 
   6. Local cache stores images with some sort of version number. 
4. **Search posts by user/caption**
   1. Search Index service
   2. Cache-aside

## Scalability

* **Distributed file storage** 
* **NoSQL, since fast writes are necessary, and relational queries arent critical** 
  * Wide-column data store like Cassandra. 
    * Reliability and availability due to replicas, fast writes. 
    * Why specifically wide-column? 
  * Photos: key=id, value = path, etc
  * UserPhotos: key=id, value=list of photos 
  * UserFollows: key=id, value=list of photos 
  * You need to explicitly store relationships. 
* **Storage for 10 years:**
  * **Photo files**: 
    * 400GB  \* 365 \* 10 = 1.4 X 10^6 GB  = 1.4 x 10^4 TB ~= ****1425TB
  * **Users:** 
    * UserID \(4 bytes\) + Username \(20 bytes\) + Email \(32 bytes\) = at least 56 bytes \* 500 million = 5 \* 10^8 \* 56 = 25 \* 10^9 = 25GB
  * **Photos:** PhotoID \(4 bytes\) + UserID \(4 bytes\) + PhotoPath \(200 bytes\) + Timestamp \(4 bytes\) + Caption \(500 bytes\) =  ~700 bytes
    * 2M per day = ~700M a year = 7B in 10 years
    * 7B \* 700 bytes =  50 \* 10^11 bytes  = 5TB  
  * **UserFollow: assume 500 users on average.** 
    * UserID \(4 bytes\) + 500 \* FollowerID \(4 bytes\) = 2000 bytes 
    * 500 million \* 2000 bytes = 10 \* 10^11 bytes =  1TB
  * Total db storage = 6TB 
* **Web Servers:** 
  * Separate services for reads and writes, since writes will be much slower. 
* **Shard DB by UserID**
  * Easy to retrieve all related user data
  * Generating photoIDs: Since each DB will autoincrement photoIds, we can append shard number to make it unique. 
  * Issues: 
    * non-uniform distribution of followers, and of photos
    * Will it take longer to always request users across shards
    * Availability: if that shard is down with no replicas then that user is completely unavailable
* **Shard DB by PhotoID** 
  * If we can generate unique PhotoIDs first and then find a shard number through “PhotoID % 10”, the above problems will have been solved. We would not need to append ShardID with PhotoID in this case as PhotoID will itself be unique throughout the system.
  * Generate via DB instance just for autoincrement ids, or double DB instance with even and odd ids for each. 
  * Or, Key Generation Service \(KGS\). 
* **KGS** 
  * Generate beforehand, store in DB, hand out on request \(mark as used\). 
  * No worries about duplications or collisions.
  * Performance
    * Mark a set of keys as used, keep them in memory, and give them out instantly \(no query, no write lag\). 
    * It's okay if the service dies and we lose them. 
    * Or give each server a bunch of keys at once, even. 
    * To improve key lookup, we can also move used keys to a separate DB to decrease index size. But perhaps key to url mapping should be stored in the generateURL service/application server itself. 
  * Concurrency
    * Make the `withdrawKey` operation atomic. 
    * If we are using memory, then definitely need a lock on the list of keys. 
  * SPOF: Yes, so replicate and standby. 

