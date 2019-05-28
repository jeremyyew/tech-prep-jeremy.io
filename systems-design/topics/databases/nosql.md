# NoSQL

## What is NoSQL? What types of NoSQL are there?

There are four main types of NoSQL databases:

* **Key/Value Stores** are like hash maps. Look up a key, and get back the value associated with it.
* **Document Databases** also use keys and values, so they're quite similar to key/value stores. Usually document databases are a bit more flexible though—they might structure the values as JSON to support indexing or filtering by value.
* **Graph Databases** are like graphs, storing nodes and edges connecting them.
* **Column Databases** are sort of like SQL databases, where each entry \(row\) is associated with different fields \(columns\). But in a column database, rows don't always have the same columns, and not every column has to be filled.

## When would you use NoSQL over SQL? 

Broadly, NoSQL databases take away three "nice" features that SQL databases have:

* **Transactions**: We usually can't lock records or prevent two users from accessing the same data at the same time.
* **Flexible Queries**: Most NoSQL databases provide key-based lookups. They usually don't have fancier SQL queries, especially across multiple tables \(e.g.: joins\).
* **Consistency**: We usually can't guarantee that everybody sees the same data in the database. Our queries might return data that are slightly out of date / stale.

