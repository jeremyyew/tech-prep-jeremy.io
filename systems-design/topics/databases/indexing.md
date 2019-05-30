# Indexing \(TODO\)

## What is DB indexing?

* It is one way of improving **DB read times without scaling horizontally.**
* Basically, you create an index on **one or more columns** \(usually, the ones you query on\) in a particular table in a database to make it faster to search through the table and find the row or rows that we want. 
* You trade off read speed \(on certain columns\) for write speed \(extra work to update indexes\). 
* Indices are usually represented as **self-balancing** [**B-tree**](https://en.wikipedia.org/wiki/B-tree) **that keeps data sorted and allows searches, sequential access, insertions, and deletions in logarithmic time.**

## How does it work? 

Example: A library catalog. 

* A library catalog is a register that contains the list of books found in a library. The catalog is organized like a database table generally with four columns: book title, writer, subject, and date of publication. There are usually two such catalogs: one sorted by the book title and one sorted by the writer name. That way, you can either think of a writer you want to read and then look through their books or look up a specific book title you know you want to read in case you don’t know the writer’s name. These catalogs are like indexes for the database of books. They provide a sorted list of data that is easily searchable by relevant information.
* Simply saying, an index is a data structure that can be perceived as a table of contents that points us to the location where actual data lives. So when we create an index on a column of a table, we store that column and a pointer to the whole row in the index. Let’s assume a table containing a list of books, the following diagram shows how an index on the ‘Title’ column looks like:![](https://www.educative.io/api/collection/5668639101419520/5649050225344512/page/5681717746597888/image/5684961520648192.png)
* Works well for datasets with large size but small payloads \(i.e. search criteria\). 
  * E.g. data sets that are many terabytes in size, but have very small payloads \(e.g., 1 KB\). Finding a small payload in such a large dataset can be a real challenge, since we can’t possibly iterate over that much data in any reasonable time. Furthermore, it is very likely that such a large data set is spread over several physical devices—this means we need some way to find the correct physical location of the desired data. Indexes are the best way to do this.

## What are the tradeoffs of DB indexing? 



* Placing an index can keep the data in memory, requiring more space.
* Writes could also be slower since the index also needs to be updated.
* When loading large amounts of data, it might be faster to disable indices, load the data, then rebuild the indices.

## How do Indexes decrease write performance?

* Inserting and updating data requires the indexes to be update and inserted as well, so more write operations. 
* Applies to all insert, update, and delete operations for the table. 
* Adding unnecessary indexes on tables should be avoided and indexes that are no longer used should be removed.
* If write is higher than read, may not be worth it. 

## What is compound indexing? 

## How might a database index be implemented?







