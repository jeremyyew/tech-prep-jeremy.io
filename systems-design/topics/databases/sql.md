# SQL and NoSQL

## What are the main differences? 

<table>
  <thead>
    <tr>
      <th style="text-align:left"></th>
      <th style="text-align:left">SQL</th>
      <th style="text-align:left">NoSQL</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left"><b>Storage</b>
      </td>
      <td style="text-align:left">
        <p>Each row represents an entity and each column represents a data point
          about that entity.</p>
        <p>&lt;b&gt;&lt;/b&gt;</p>
        <p></p>
      </td>
      <td style="text-align:left">
        <p></p>
        <p>Depends on data storage models.</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Schema</b>
      </td>
      <td style="text-align:left">
        <p></p>
        <p>Fixed schema, meaning the columns must be <b>decided and chosen before data entry</b> and
          each row must have data for each column. The schema can be altered later,
          but it involves modifying the whole database and going offline.</p>
      </td>
      <td style="text-align:left">
        <p></p>
        <p>In NoSQL, schemas are dynamic. Columns can be added on the fly and each
          &#x2018;row&#x2019; (or equivalent) doesn&#x2019;t have to contain data
          for each &#x2018;column.&#x2019;</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Querying</b>
      </td>
      <td style="text-align:left">SQL databases use SQL (structured query language) for defining and manipulating
        the data, which is very powerful.</td>
      <td style="text-align:left">
        <p>In a NoSQL database, queries are focused on a collection of documents.</p>
        <p>&lt;b&gt;&lt;/b&gt;</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Scalability</b>
      </td>
      <td style="text-align:left">In most common situations, SQL databases are vertically scalable, i.e.,
        by increasing the horsepower (higher Memory, CPU, etc.) of the hardware,
        which can get very expensive. It is<b> possible to scale a relational database across multiple servers,</b> but
        this is <b>challenging and time-consuming. </b>
      </td>
      <td style="text-align:left">
        <p></p>
        <p>On the other hand, NoSQL databases are <b>horizontally scalable</b>, meaning
          we can add more servers easily in our NoSQL database infrastructure to
          handle a lot of traffic. Any cheap commodity hardware or cloud instances
          can host NoSQL databases, thus making it a lot more cost-effective than
          vertical scaling. A lot of NoSQL technologies also <b>distribute data across servers automatically.</b>
        </p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Reliability or ACID Compliancy (Atomicity, Consistency, Isolation, Durability)</b>
      </td>
      <td style="text-align:left">The vast majority of relational databases are <b>ACID compliant.</b> So,
        when it comes to data reliability and safe guarantee of performing transactions,
        SQL databases are still the better bet.</td>
      <td style="text-align:left">
        <p></p>
        <p>Most NoSQL solutions <b>sacrifice ACID compliance for performance and scalability.</b>
        </p>
      </td>
    </tr>
  </tbody>
</table>## How do we decide which to use? 

### Reasons for SQL: 

1. We need to ensure **ACID compliance**. ACID compliance reduces anomalies and protects the integrity of your database by prescribing exactly how transactions interact with the database. 
   1. For many e-commerce and financial applications, an ACID-compliant database remains the preferred option.
2. Your **data is structured and unchanging.** 
   1. If your business is **not experiencing massive growth** that would require more servers and if you’re only working with **data that is consistent**, then there may be no reason to use a system designed to support a variety of data types and high traffic volume.

### Reasons for NoSQL: 

1. **Large data, little structure.** 
   1.  No constraints on types. 
2. **Scalability.** 
   1. Write performance is better than NoSQL, critical for write-heavy applications. 
   2. Easier to horizontally scale with commodity hardware, which also makes it cheaper. 
   3. Auto-scaling and replication across distributed servers provided sometimes, such as with Cassandra. 
3. **Rapid development.** 
   1. No need to even define schema. 
   2. Easy to iterate versions without breaking changes or migrations. 

## What types of NoSQL DB's are there? \(TODO\)

| Type  | Description | Use case | Popular examples |
| :--- | :--- | :--- | :--- |
| **1.Key-Value Stores** | Array of key-value pairs. | ? | Redis, Voldemort, and Dynamo. |
| **2. Document Databases** | Data is stored in 'documents' \(instead of rows and columns in a table\) and these documents are grouped together in collections. Each document can have an entirely different structure. | ? | CouchDB and MongoDB. |
| **3. Wide-Column Databases** | Instead of ‘tables,’ in columnar databases we have **column families, which are containers for rows**. Unlike relational databases, we don’t need to know all the columns up front and each row doesn’t have to have the same number of columns.  | Analyzing large datasets.  |  Cassandra and HBase. |
| **4. Graph Databases** |  Nodes \(entities\), properties \(information about the entities\), and edges/lines \(connections between the entities\).  | Representing relationships between entities.  | Neo4J and InfiniteGraph. |

\*\*\*\*





