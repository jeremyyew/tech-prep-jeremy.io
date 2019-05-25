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
Users 
    phoneNumber

Chats 
    sender
    receiver
    contents
    datetime

```

## Pseudocode

## Feature Implementation 

## Scalability

