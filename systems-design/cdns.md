# CDN's

## What is a CDN?
A content delivery network (CDN) is a **globally distributed network of proxy servers**, serving content from locations closer to the user. 

- Generally, **static files** such as HTML/CSS/JS, photos, and videos are served from CDN, although some CDNs such as Amazon's CloudFront support dynamic content. 
- The site's DNS resolution will tell clients which server to contact.

Serving content from CDNs can significantly improve performance in two ways:
- Users receive content at data centers close to them. 
- Your servers do not have to serve requests that the CDN fulfills

## What is the difference between pull and push CDNs? 

### Pull CDN
**CDN pulls from server on user request, then cache until expiry.**

#### Pros: 
- Generally **easier to configure** (your server needs no update logic).
- Can **minimize storage space** on the CDN by only storing recently-requested data. 
- **Distributes high traffic** by serving cached data that is **frequently requested** (with a push CDN, your server is blind to which data is being requested frequently and might be frequently pushing unrequested data).

#### Cons: 
- **Less control** (must wait for cache expiry for updates).
- Might result in **redundant traffic** (and slower response) when unchanged data is frequently repulled. For example, if we have low traffic resulting in frequent cache expiries, or very rare/irregular changes relative to TTL (time-to-live).

#### Use case: 
Sites/services with **heavy traffic** and/or **lots of data** (particularly with a **non-uniform/unpredictable distribution of demand across different data**) can benefit from a pull CDN, since it **distributes traffic by pulling only what is requested, and serving cached copies of what is frequently requested.** 

### Push CDN's: 
**Server pushes updates to CDN only on change/when specified.**

#### Pros: 
- **More control** (consistency exactly when you specify it).
- **Never any redundant traffic** in the form of pulling unchanged data (only as much updates as you need).

#### Cons: 
- Might require **more configuration** (when to update, what data to push).
- **More storage** might be used (if you always push all your data).
- Too frequent changes may result in overloading your server, or high costs.
- High traffic combined with changing data might result in slow performance. Since your server is blind to which data is being requested frequently, it might be frequently pushing unrequested data while trying to ensure data is up to date. 

#### Use case: 
Sites/services with **infrequently updated data**, **predictable/uniform distribution of demand across data** (e.g. users will often want a fixed set of data), **very little data**, or **very low traffic** can benefit from a pull CDN. Or, sites/services with **real-time consistency requirements***. 

## What are some disadvantages of CDNs? 

# Sources:
https://github.com/donnemartin/system-design-primer#content-delivery-network
https://www.creative-artworks.eu/why-use-a-content-delivery-network-cdn/
