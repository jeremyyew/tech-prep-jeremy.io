# Twitter

* [https://github.com/donnemartin/system-design-primer/blob/master/solutions/system\_design/twitter/README.md](https://github.com/donnemartin/system-design-primer/blob/master/solutions/system_design/twitter/README.md)

## Scoping

1. **Use Cases**
   1. Basic: Post, view followed users' tweets, search  
   2. Others:  
      1. Retweets. Following. Multimedia. Mentions. Hashtags.  Private tweets/DMs. Privacy. 
      2. Lets just ignore all, but later talk about how to incorporate Following + Following Requests    
2. **Platform?** Suppose just web for now. 
3. **Traffic**
   1. How many users? 500 million. 
   2. How many tweets per user?
      * 10 per day per user, so 5 billion a day total, so about 5 million a second total. 
      * We want to divide by hours/mins/secs=24\*60\*60=86,400=8\*10^4. 
      * So 5 x 10^9 / 8 \*10^4 = 6.25 \* 10^4 = ~60,000 per second. 
   3. Read/write requests ratio: 
      * At least 50/50? Assuming every time you tweet, you also read. Probably heavier on read if lots of people are just lurkers - say, up to 20-80. 

## **Design Goals**

1. Fast reads. 
2. Writes could be async, but shouldn't be too slow. 

## **Schema**

```text
Users 
    id (32b)
    handle (20b)
    email - primary key (32b)

Tweets 
    user_id 
    text (140b)
    timestamp (140b)    
    
Follows 
    Follower
    Follower
```

## Feature Implementation 

1. **Post tweet** 
   * The **Client** posts a tweet to the **Web Server**, running as a [reverse proxy](https://github.com/donnemartin/system-design-primer#reverse-proxy-web-server)
   * The **Web Server** forwards the request to the **Write API** server
   * The **Write API** stores the tweet in the user's timeline on a **SQL database**
   * The **Write API** contacts the **Fan Out Service**, which does the following:
     * Queries the **User Graph Service** to find the user's followers stored in the **Memory Cache**
     * Stores the tweet in the _home timeline of the user's followers_ in a **Memory Cache**
       * O\(n\) operation: 1,000 followers = 1,000 lookups and inserts
     * Stores the tweet in the **Search Index Service** to enable fast searching
     * Stores media in the **Object Store**
     * Uses the **Notification Service** to send out push notifications to followers:
       * Uses a **Queue** \(not pictured\) to asynchronously send out notifications
2. **Request recent tweets** 
   * The **Client** posts a home timeline request to the **Web Server**
   * The **Web Server** forwards the request to the **Read API** server
   * The **Read API** server contacts the **Timeline Service**, which does the following:
     * Gets the timeline data stored in the **Memory Cache**, containing tweet ids and user ids - O\(1\)
     * Queries the **Tweet Info Service** with a [multiget](http://redis.io/commands/mget) to obtain additional info about the tweet ids - O\(n\)
     * Queries the **User Info Service** with a multiget to obtain additional info about the user ids - O\(n\)
3. **Search tweets**
   * The **Client** sends a search request to the **Web Server**
   * The **Web Server** forwards the request to the **Search API** server
   * The **Search API** contacts the **Search Service**, which does the following:
     * Parses/tokenizes the input query, determining what needs to be searched
       * Removes markup
       * Breaks up the text into terms
       * Fixes typos
       * Normalizes capitalization
       * Converts the query to use boolean operations
     * Queries the **Search Cluster** \(ie [Lucene](https://lucene.apache.org/)\) for the results:
       * [Scatter gathers](https://github.com/donnemartin/system-design-primer#under-development) each server in the cluster to determine if there are any results for the query
       * Merges, ranks, sorts, and returns the results

## Scalability

1. DB - NoSQL for fast writes, Memory Cache for fast writes and reads. 
   1. Document store that supports indexing and filter. We need this since we will want to request tweets by user, and by timestamp. 
2. Load balancer, multiple web servers.
3. Cache-aside + write-through. Shard by user whose tweets are requested, so that anyone who requests the same user's tweets will be directed to the same cache, and updates are immediately written to that cache. 
   1. Potential issue: by chance we might get quite unequal distribution on certain shards.  
4. Shard DB by users. 
   1. Potential issue: in the future have to request from all DB's if we want to search users or search tweets?
   2. Consider shard by timestamp. So searches can still be done iteratively. Plus normal requests are always going to be done for most recent anyway.  
5. Consistency?
   1. Sometimes there will be a lag before . But that's ok, its not crucial, people don't usually immediately check to see if their friends saw their tweet instantly. 



![](../../.gitbook/assets/image%20%2812%29.png)









