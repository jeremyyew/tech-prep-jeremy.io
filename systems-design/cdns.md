# CDN's

## CDN's

### What is a CDN?

**Motivation: physical distance has a big impact on how quickly the user receives a web page, and static content shouldn't have to be always requested from a single location.** 

A content delivery network \(CDN\) is a **globally distributed network of proxy servers**, serving content from locations closer to the user.

* Generally, **static files** such as HTML/CSS/JS, photos, and videos are served from CDN, although some CDNs such as Amazon's CloudFront support dynamic content. 
* The site's DNS resolution will tell clients which server to contact.

Serving content from CDNs can significantly improve performance in two ways:

* **Performance across regions:** Users in multiple locations receive content at data centers close to them. 
* **Scalability**: Reduces load on servers by serving static files, which are often a large proportion of the website's data. Helps improve performance particularly during spikes. 

![](../.gitbook/assets/image%20%283%29.png)

### What is the difference between pull and push CDNs?

### Pull CDN

**CDN pulls from server on user request, then cache until expiry.**

**Pros:**

* Generally **easier to configure** \(your server needs no update logic\).
* Can **minimize storage space** on the CDN by only storing recently-requested data. 
* **Distributes high traffic** by serving cached data that is **frequently requested** \(with a push CDN, your server is blind to which data is being requested frequently and might be frequently pushing unrequested data\).

**Cons:**

* **Less control** \(must wait for cache expiry for updates\). Less flexible too. 
* Might result in **redundant traffic** \(and slower response\) when unchanged data is frequently repulled. For example, if we have low traffic resulting in frequent cache expiries, or very rare/irregular changes relative to TTL \(time-to-live\).

**Use case:**

Sites/services with **heavy traffic**, **lots of data** \(particularly with **non-uniform/unpredictable distribution of demand across different data**\), and/or **unpredictable demand for data over time**, can benefit from a pull CDN, since it **distributes traffic by pulling only what is requested, and serving cached copies of what is frequently requested.**

Examples: image/video hosting site, social network.

### Push CDN's:

**Server pushes updates to CDN only on change/when specified.**

**Pros:**

* **More control** \(consistency exactly when you specify it\).
* **Never any redundant traffic** in the form of pulling unchanged data \(only as much updates as you need\).

**Cons:**

* Might require **more configuration** \(when to update, what data to push\).
* **More storage** might be used \(if you always push all your data\).
* Too frequent changes may result in overloading your server, or high costs.
* High traffic combined with changing data might result in slow performance. Since your server is blind to which data is being requested frequently, it might be frequently pushing unrequested data while trying to ensure data is up to date. 

**Use case:**

Sites/services with **infrequently updated data**, **very big files**, **predictable/uniform distribution of demand across data** \(e.g. users will often want a fixed set of data\), **consistent demand for data over time**, or **low traffic** can benefit from a pull CDN. Or, sites/services with **real-time consistency requirements\***.

Examples: blogs, archives, podcasts.

### What are some disadvantages of CDNs?

* Might get expensive. 
* Require configuration and changing URLs.
* In particular, TTL/push frequency must be configured appropriately or users get stale data.

{% hint style="info" %}
#### Additional terminology: Origin and Edge servers

Origin servers are the origin of data. Edge servers get data from the origin server. A POP \(point of presence\) is a single physical location that consists of one or multiple edge servers.
{% endhint %}

## Sources:

[https://github.com/donnemartin/system-design-primer\#content-delivery-network](https://github.com/donnemartin/system-design-primer#content-delivery-network) [https://www.keycdn.com/support/how-does-a-cdn-work](https://www.keycdn.com/support/how-does-a-cdn-work)

