# URL Shortener

* [https://www.interviewcake.com/question/java/url-shortener](https://www.interviewcake.com/question/java/url-shortener)

## Scoping

1. How many links created per month? 
   1. How many users? 
   2. How many links over 5 years? 
   3. How many redirects per link, and size of spikes? 
2. Read/write ratio? About 20-80? 
3. Authentication, accounts, sessions? 
4. Modify and delete? Search? 
5. Persistence of links?
   1. From created
   2. From last used
6. Custom create vs auto-generate?
7. Analytics? 

## **Design Goals**

1. **Lots of links**
2. **Short as possible**
3. **Fast**
4. **Resilient to load spikes**

## **Schema**

```sql
create table ShortLinks (
    slug varchar(20),
    destination varchar(200)
);
```

Why 20? Why 200? 

## Pseudocode

```text
create_shortlink(req):
    dest = req.dest
    slug = req.slug
    
    if slug = None: 
        slug = generateUniqueSlug()
        
    DB.insertLink(slug, dest)
    return Response(OK, slug)

redirect(req):
    dest = DB.getDest(req.slug)
    return Response(302, dest) 
```

## Feature Implementation 

1. **Representing slugs**
   * `c^n` possibilities with charset of size c and slugs of length n. 
   * Choosing charset
     * Case sensitive? Domains are not, but paths can be. 
     * Easy to read/write: Avoid O and 0, I and 1, etc? 
     * URL-legal: 
       * > "only alphanumerics, the special characters "$-\_.+!\*'\(\),", and reserved characters used for their reserved purposes may be used unencoded within a URL" \([RFC 1738](https://www.rfc-editor.org/rfc/rfc1738.txt)\). "Reserved characters" with "reserved purposes" are characters like '?', which marks the beginning of a query string, and '\#', which marks the beginning of a fragment/anchor....No accented characters.
       * So let's use only A-Z, a-z, 0-9 = 62 chars. But for custom, allow `$-_.+!*()`. 

 
   * 100,000 users per minute = 100,000∗60∗24≈145 million new links a da = 52.5 billion a year = 5.2 _trillion_ slugs over 100 years. 
   * 5.2 trillion log 62 = ~7. 
   * Could have more if we have length-1, length-2, etc. But only about 1/62 more. 
2. **Generate random slug**
   * How to generate unique slugs and handle collisions? 
   * We don't want to generate random and re-roll if collision. This will be increasingly slow. We want to do it in an ordered, iterative fashion.
   * Treat a sequence as a base-62 number using base-conversion. Pad shorter numbers to make it 7-char long. 
   * Increment and try again if we hit a custom one thats already been claimed. 
   * ```text
     generateUniqueSlug():
         currentRandomSlugId += 1
         newId = currentRandomSlugId
         return baseConversion(newId, base62Alphabet)
     ```
   * Bonus: Use auto-incrementing id as slug. But what about custom slugs? 
     * > If we used a SQL-type database like MySQL or Postgres, we usually default to having our key field be a standard auto-incrementing integer called "id" or "index." But in this case, because we know that slugs will be unique, there's no need for an integer id—the slug is enough of a unique identifier.
       >
       > BUT here's where it gets clever: what if we _represented the slug_ as an auto-incrementing integer field? We'd just have to use our base conversion method to convert them to slugs! This would also give us tracking of our global currentRandomSlugId for free—MySQL would keep track of the highest current id in the table when it auto increments. Careful though: user-generated slugs throw a pretty huge monkey wrench into things with this strategy! How can you maintain uniqueness across user-generated and randomly-generated slugs without breaking the auto-incrementing ids for randomly-generated slugs?

## Scalability

* **For reads:** 
  * DB - Consider NoSQL, since only key-value reads, no relational queries
  * Cache 
    * Consistency - write-through on modify \(possibly on write too\)
    * LRU 
  * Shard cache by 'hash and mod' of slug in request
  * Shard DB similarly
  * Load balancer + web server workers - how many?? 
* **For writes**
  * Let's say we have multiple web servers for creating links.
  * How to share the incrementing counter across all web servers? 
    * Perhaps everyone has 'jump by N + K' logic, where N is the total number of servers, and K is the id of each server. So everyone gets their own multiples. And everytime we increase servers, we say 'when u reach id Z, start jumping by '
    * But this doesn't seem doable for autoscaling unless we somehow automate it, it might be messy. 
    * Actually a simpler way would be to have the load balancer distributes create requests in a round-robin manner.  
  * Shard cache by 'hash and mod' of slug in request
    * Shard DB similarly

\*\*\*\*

\*\*\*\*

\*\*\*\*

\*\*\*\*

\*\*\*\*

\*\*\*\*

\*\*\*\*

