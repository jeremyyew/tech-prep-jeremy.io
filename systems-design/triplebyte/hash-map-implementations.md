---
description: >-
  https://www.codingeek.com/data-structure/a-complete-guide-to-hashing-and-collision-resolution-strategy/
---

# Hash Map Implementations

## Python 

* Resize by factor of two
* Sparse table of pointers to dense table of \(hash value, key\_value, pointer\_value\)/ 

## Collision resolution strategy

It's okay to have collisions. It's all about the distribution of that collision. 

* Chaining 
  * with linked lists
  * with tree \(java\) 
* Open addressing
  * Probing 
    * Probe sequences: What is the interval to the next possible location? 
    * Linear - go to next. 
    * Quadratic - jump quadratically. 
    * **Double Hashing** - interval computed by another hash. 
    * **Cuckoo -** a set of hash functions, we rotate amongst them to insert/lookup. If still cannot, we relocate recursively. 
    * **Robin hood** - displace based on probe distance. 
    * 2-choice. 
  * Resizing - all at once, incremental \(insert only into new table\)
  * You cant have more values than the number of keys. 
  * We have to worry not just about collision but clustering. 
* MinHash. 

## Resizing



## Terminology

* Load factor = n/k, average number of entries per key. 
  * n is the number of entries occupied in the hash table.
  * k is the number of buckets.

