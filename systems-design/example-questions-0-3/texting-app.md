# Texting App

* [https://www.interviewcake.com/question/java/tapchat](https://www.interviewcake.com/question/java/tapchat)
* Like Snapchat, not Whatsapp. 

## Scoping

1. Scale: 
   1. Users total? Say 500 million. 
      1. Messages per day? Say 100. 
      2. So 50 billion per day. 
      3. So 500, 000 per second. 
   2. Storage? 
      1. Store messages until delivered.
      2. 280 char messages = 280 bytes if ASCII, more if UTF-8 \(for emojis, other languages\). 
      3. 300 bytes \* 50 billion = 15 terabytes 
         1. One byte is 8 bits. after that, kb, mb, gb, tb, pt are increasing 2^10.
         2. One TB is about **2^40 or 10^12 bytes, and one billion is 10^9**
         3.  **5 \* 10^10 \*3 \* 10^2 = 15 \* 10^12. So 15 terabytes.**
2. Features:
   1. Basics? Send and receive. 
   2. Platform? Mobile. 
   3. Messaging only between app users? Yes. 
   4. Images, audio, etc? Not yet. 
   5. Length limit? 
   6. How to add other users? 
   7. Privacy?
   8. Replies? 

## **Design Goals**

1. Send and receive instantaneous. 
2. Don't lose messages. 
3. Resilient to spikes.

## **Schema**

```text
//SQL
Users 
    phoneNumber

Messages 
    sender
    receiver
    contents
    datetime

// OR No-SQL document store
{   key: recipient's phone,
    value: [
        { contents: [ message ],
          sender: [ sender phone ] },
        { contents: [ message ],
          sender: [ sender phone ] },
        ...
    ] 
}
```

## Feature Implementation 

1. DB? NoSQL
   1. **Transactions:** We don't need database transactions, so that's not a problem.
   2. **Relational Queries:** We're not doing any fancy lookups—in fact, our data model is really quite simple. So that's OK too.
   3. **Consistency**: We do make updates to our databases though, so we need to figure out how we should handle concurrent updates and if we're OK working with data that might not be completely up to date.
2. Save message to DB, then send to user once available 
   1. Polling vs Long Polling \(Push, Server Sent Events\)

## Scalability

1. **What happens if a user receives two messages at the same time?** **\(concurrency\)** We need to make sure they both get delivered; we don't want to drop any messages.
   1. When we write a pending message to be delivered to a recipient, if it already exists, combine/append it and send all together. 
2. Once a user's messages are delivered, they can be deleted from the database. What happens if a user **asks for new messages before an earlier delete clearing out old messages propagates through the database? \(Consistency\) We might get duplicate messages.** 
   1. **We always have the risk of stale data since we using NoSQL, and stateless servers.** 
   2.  Load balancers with **sticky sessions**. but giving up some flexibility with load balancing.
   3. Better: have the app itself recognize when it receives, by having some sort of unique ID or hash of sender/timestamp. That way even if it retrieves the same message, it will know not to display it. 
   4. OR some sort of data revision number, so we know when data is outdated.  

## 

