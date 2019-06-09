# Indexing

## What is DB indexing?

{% hint style="info" %}
In a **relational database**, an **index** is a **data structure** that increases retrieval speed at the expense of decreasing write speed as well as using more storage space.
{% endhint %}

* Indices are usually represented as **self-balancing** [**B-tree**](https://en.wikipedia.org/wiki/B-tree) ****that keeps data sorted and allows **searches, sequential access, insertions, and deletions** in **logarithmic time.**
* It is one way of improving **DB read times without scaling horizontally.**
* Note: A b-tree is NOT a binary tree. [**https://en.wikipedia.org/wiki/B-tree**](https://en.wikipedia.org/wiki/B-tree)\*\*\*\*
  * The B-tree is a generalization of a [binary search tree](https://en.wikipedia.org/wiki/Binary_search_tree) - a node can have more than two children.
  * Each node's keys act as separation values which define the range of values contained by each of its [subtrees](https://en.wikipedia.org/wiki/Subtree). 

## How does it work? 

Example: A library catalog. 

* A library catalog is a register that contains the list of books found in a library. The catalog is organized like a database table generally with four columns: book title, writer, subject, and date of publication. There are usually two such catalogs: one sorted by the book title and one sorted by the writer name. That way, you can either think of a writer you want to read and then look through their books or look up a specific book title you know you want to read in case you don’t know the writer’s name. These catalogs are like indexes for the database of books. They provide a sorted list of data that is easily searchable by relevant information.
* Simply saying, an index is a data structure that can be perceived as a table of contents that points us to the location where actual data lives. So when we create an index on a column of a table, we store that column and a pointer to the whole row in the index. Let’s assume a table containing a list of books, the following diagram shows how an index on the ‘Title’ column looks like:![](https://www.educative.io/api/collection/5668639101419520/5649050225344512/page/5681717746597888/image/5684961520648192.png)
* Works well for datasets with large size but small payloads \(i.e. search criteria\). 
  * E.g. data sets that are many terabytes in size, but have very small payloads \(e.g., 1 KB\). Finding a small payload in such a large dataset can be a real challenge, since we can’t possibly iterate over that much data in any reasonable time. Furthermore, it is very likely that such a large data set is spread over several physical devices—this means we need some way to find the correct physical location of the desired data. Indexes are the best way to do this.

## What are the tradeoffs of DB indexing? 

* More memory. 
* Slower writes due to updating index.
  * Inserting and updating data requires the indexes to be update and inserted as well, so more write operations. 
  * Applies to all insert, update, and delete operations for the table. 

## When to use single indexes? 

* High read, low write. 
  * If write is higher than read, may not be worth it. 
* **High cardinality.** 
  * If you create an index in a column that has low cardinality, that’s not going to be beneficial since the index should reduce search space. Low cardinality does not significantly reduce search space.  Example: if you create an index on a boolean \( `int` `1` or `0` only \) type column, the index will be very skewed since cardinality is less \(cardinality is 2 here\). But if this boolean field can be combined with other columns to produce high cardinality, go for that index when necessary.
* Other tips: 
  * Indexes that are no longer used should be removed.
  * When loading large amounts of data, it might be faster to disable indices, load the data, then rebuild the indices.
  * By the way, you can enforce uniqueness by creating a unique index. 

## What is compound indexing? 

* Index on multiple columns in specific order, used when queries have conditions on columns in the same order. 
* The columns used in composite indices are concatenated together, and those concatenated keys are stored in sorted order using a B+ Tree. 
* **Only left prefixes, in correct order.** 
  * Composite on `col1`, `col2`, `col3`, `col4`. 
  * Valid: `col1`, `(col1, col2)` , `(col1, col2, col3)` , `(col1, col2, col3, col4)`. 
  * Invalid: `(col1, col3)` or `(col1, col2, col4)` or `col3` , `col4`, `(col2, col1)`
  * When you perform a search, concatenation of your search keys is matched against those of the composite index. Then if there is any mismatch between the ordering of your search keys & ordering of the composite index columns, the index can’t be used.

## **When to use composite indexing?** 

* Certain fields are **appearing together in many queries.**
* If you are creating a composite index in \(`col1`, `col2`\)**, you don't need to create an index on col1.**  `col1` alone can be served by the composite index itself since it’s a left side prefix of the index.
* If columns used in the composite index end up **having high cardinality together,** they are good candidate for the composite index.

## Sources

* [https://www.freecodecamp.org/news/database-indexing-at-a-glance-bb50809d48bd/](https://www.freecodecamp.org/news/database-indexing-at-a-glance-bb50809d48bd/)
* [https://medium.com/@User3141592/single-vs-composite-indexes-in-relational-databases-58d0eb045cbe](https://medium.com/@User3141592/single-vs-composite-indexes-in-relational-databases-58d0eb045cbe)

