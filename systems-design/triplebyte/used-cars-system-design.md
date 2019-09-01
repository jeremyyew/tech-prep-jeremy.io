# Used Cars App - System Design

* Requirement questions:
  * How many cars? 
  * Do users get to add cars to the app? 
    * If so, do they need user accounts? 
  * What categories? 
    * Name, Plate, Year,  
  * How many requests? 
    * Per month: divide by 30 \*  24 \* 60 \* 60 = 2.6 x 10^6. 
    * Per day: divide by 30 \*  24 \* 60 \* 60 = 86,400 = 9 x 10^4. 
  * Search functionality? Ranges? 
* To research: when to index? 
* DB Schema
* API 
* Components 
  * DB \(MySQL, Postgres\). 
    * Space requirements: 
  * Object Storage 
  * Web server \(backend\). **Why Django?** 
  * Web server \(frontend\) NodeJS. 
* MVP Deployment
  * Amazon RDS. On cloud host: Heroku? Amazon EC2/EB. GCP, CF.  
* Improve scalability i.e. availability
  * Caching. Redis. 
  * CDN to serve frontend + static assets
  * Sharding \(i.e. horizontal partitioning\) 
  * NoSQL 
  * Amazon ECS. Docker, Kubernetes. 
  * Fargate?
* Improve reliability 
  * DB replicas 

