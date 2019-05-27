# Instagram

## Scoping

1. Use cases
   1. **Post photos or videos \(one only, can edit and delete\)**
   2. **Follow other users \(assume all public\)**
   3. **View posts of followed users**
   4. **Search posts by user/caption**
   5. Some out-of-scope:
      1. Private/public, DM, likes, comments, explore feed, hashtags, mentions, ranking algorithms, stories, tagging 
2. Platform
   1.  Mobile app 
3. Traffic
   * 500 million users total, 1m active daily, 2 posts a day 
   * 2M new photos every day = 2 x 10^6 / 8 \* 10^4 = 2/8 x 10^2  = ~25 photos per second.
   * Average photo file size =&gt; 200KB. 
   * One byte is 8 bits. after that, kb, mb, gb, tb, pt are increasing 2^10 or 10^2. One TB is about **2^40 or 10^8 bytes.** 
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

## **Schema**

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
    type
    timestamp
    caption
} 
```

## Feature Implementation 

## Scalability

