# Triplebyte

* **Tic tac toe**
* **Database short answer**
  * Foreign keys
  * Compound indexes, benefits/drawbacks, implementation
* **HTTP/Web short answer** 
  * Web
    * Characteristics of different REST verbs  
    * Headers
    * CDN's 
    * Browser caching - controlled by headers
  * Hashing - might be slow, bcrypt 
  * Salting 
* **Data structures short answer** 
  * Hashmap
    * insert, probing, chaining, collision resolution 
    * Key stored as well 
    * Resizing still gives hashmaps amortized constant time 
  * BST 
    * ordering invariant, performance 
    * Definition of balanced tree
    * Self-balancing tree - rotations done to maintain balance 
    * Performance of finding k-th smallest with in-order traversal 
      * augment the tree? add height? 
* **Low level short answer**
  * malloc allocates memory on the heap - they seemed rather lost - thinking that ptr/stack would just print 10. They knew the basics around concurrency, like what deadlock and mutexes are - but didn't seem to know much beyond that.
* **Debug section**
  * Use debugger!
* **Used car API problem**

  1. Can the candidate get an app off the ground? 

  - Almost certainly. They could talk about tech to use - JS + SQL - as well as a plausible schema. They understood that 20million cars isn’t a lot and wouldn’t require a overengineered design.

  2. What size app can they actually build and did they intelligently discuss scaling? 

  - I think MVP would be just fine, and they could even do some modest scaling as they understood the concept of multiple EC2 instances of their app and load balancing traffic. However, they described a rather manual approach to scaling rather than a fancier dynamic auto-scaling.

  * Dynamic autoscaling: 
    * Amazon EC2 Auto Scaling or Amazon Auto Scaling for multiple services. 
    * Autoscaling fleet: Docker Swarm, Kubernetes.

* 3. What would distinguish this candidate's approach from another candidate who got the same objective score? 

  - They did a great job of scoping out the key specs up front, like data size and request load. I also liked that they knew about result pagination for large returns of data. I liked that they knew about RDS for the database, but they seemed to be throwing in “Docker” more like a buzzword rather than actual experience since they didn’t mention ECS or Fargate.

\* Scopes out the problem, checking how often the data updates, how many cars, and how many requests. 

\* Gets 20 million cars is not a lot. 

\* SQL Database. One table for all the cars, with each attribute in a column. Add indexes. 

\* NodeJS, use SQLize to talk to the DB. 

\* POST with POST and JSON. Ranges with upper/lower limit. 

\* Paginate large results. 

\* AWS, EC2. RDS for the database. 

\* Scale, put on my servers. Use Nginx reverse proxy to load balance - but not clear on deployment. 

\* Alternatively use Docker on EC2 for the App.

Personal Story: 

Daniel is a multi-disciplinary developer with knowledge of multiple programming languages and a great grasp of Emacs to boot!

