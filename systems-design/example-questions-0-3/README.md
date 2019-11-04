# Example Questions \(4/6\)

## **Approach**

* **Scoping/Functional requirements**
  * No. of users
  * Possible use cases
  * Final features
    * **Tradeoffs,** justification on decision 
  * Inputs/outputs - sketch API 
  * Read/write ratio 
  * Number of requests per second 
    * Concurrent connections per web server - 500? 
  * Size of requests/responses
    * Change over time, scalability 
  * Persistence
    * Memory requirements
  * MVP vs production
* **Design Goals/Non-functional Requirements**
  * CAP, simplicity, extensibility
  * Clarify
  * Prioritize 
* **Components + Schema**
  * Firm up API if necessary
  * Justify based on design goals
  * SQL or NoSQL
  * Scalability
    * Latency
      * **Horizontal scaling - load balancers**
      * **Caching - client,  web server,  intermediate cache, CDN**
        * **Replicas?**  

        1. **Read-first/Cache-aside**
        2. **Write-through**
        3. **Write-back**
        4. **Refresh-ahead**
      * **Database sharding/data partitioning**
        * **Vertical, horizontal - cons \(joining\)** 
        * **Consistent hashing** 
        * **Directory-based partitioning** 
        * **How to handle non-uniform distribution?** 
    * Fault tolerance 
      * Replicas, redundancy 
* **Others**
  * Pseudocode
  * Feature Implementation 
  * Edge cases/error handling 

## Handy ballpark figures

* [https://github.com/donnemartin/system-design-primer\#latency-numbers-every-programmer-should-know](https://github.com/donnemartin/system-design-primer#latency-numbers-every-programmer-should-know)
* **2.5 million seconds per month**
* **1 request per second = 2.5 million requests per month**
* **40 requests per second = 100 million requests per month**
* **400 requests per second = 1 billion requests per month**
* Reading 1 MB sequentially from memory takes about 250 microseconds, while reading from SSD takes 4x and from disk takes 80x longer.[1](https://github.com/donnemartin/system-design-primer#latency-numbers-every-programmer-should-know)

| char | 1 byte | -128 to 127 or 0 to 255 |
| :--- | :--- | :--- |
| **unsigned char** | **1 byte** | **0 to 255** |
| **unsigned int** | **2 or 4 bytes** | **0 to 65,535 or 0 to 4,294,967,295** |
| signed char | 1 byte | -128 to 127 |
| int | 2 or 4 bytes | -32,768 to 32,767 or -2,147,483,648 to 2,147,483,647 |
| short | 2 bytes | -32,768 to 32,767 |
| unsigned short | 2 bytes | 0 to 65,535 |
| long | 8 bytes | -9223372036854775808 to 9223372036854775807 |
| unsigned long | 8 bytes | 0 to 18446744073709551615 |

| Unit | In Bytes |
| :--- | :--- |
| **Byte** | **1** |
| **KB**  | **10^3** |
| **MB**  | **10^6** |
| **GB** | **10^9** |
| **TB** | **10^12** |
| **PB** | **10^15** |

## Sources:

* Donne Martin's Primer
* * [https://github.com/donnemartin/system-design-primer\#system-design-interview-questions-with-solutions](https://github.com/donnemartin/system-design-primer#system-design-interview-questions-with-solutions)
* Interview Cake 
  * [https://www.interviewcake.com/question/java/url-shortener](https://www.interviewcake.com/question/java/url-shortener)
  * [https://www.interviewcake.com/question/java/tapchat](https://www.interviewcake.com/question/java/tapchat)
  * [https://www.interviewcake.com/question/java/mesh-message](https://www.interviewcake.com/question/java/mesh-message)
* Yangshun's list 
  * [https://github.com/yangshun/tech-interview-handbook/tree/master/design\#specific-topics](https://github.com/yangshun/tech-interview-handbook/tree/master/design#specific-topics)
* Gainlo
  * [http://blog.gainlo.co/index.php/category/system-design-interview-questions/](http://blog.gainlo.co/index.php/category/system-design-interview-questions/)
* Educative
  * [https://www.educative.io/collection/5668639101419520/5649050225344512](https://www.educative.io/collection/5668639101419520/5649050225344512)

## 

