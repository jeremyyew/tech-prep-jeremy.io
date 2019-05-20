# CDN's

## What is a CDN?

**Motivation: physical distance has a big impact on how quickly the user receives a web page, and static content shouldn't have to be always requested from a single location.**

A content delivery network \(CDN\) is a **globally distributed network of proxy servers**, serving content from locations closer to the user. 

Generally, **static files** such as HTML/CSS/JS, photos, and videos are served from CDN, although some CDNs such as Amazon's CloudFront support dynamic content.

## What are some key benefits?

* **Performance across regions:** Users in multiple locations receive content at data centers close to them. 
* **Scalability**: Reduces load on servers by serving static files, which are often a large proportion of the website's data. Helps improve performance particularly during spikes. 
* **Improved SEO rankings**: Based on faster load speeds.
* **Added security**: Some CDNs can mitigate DDOS attacks. 

![](../.gitbook/assets/image%20%283%29.png)

## What is the difference between pull and push CDNs?

**Pull CDN: CDN pulls from server on user request, then cache until expiry.**

**Push CDN's: Server pushes updates to CDN only on change/when specified.**

\*\*\*\*

<table>
  <thead>
    <tr>
      <th style="text-align:left"></th>
      <th style="text-align:left"><b>Pull</b>
      </th>
      <th style="text-align:left"><b>Push</b>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left"><b>Ease of config</b>
      </td>
      <td style="text-align:left">Generally <b>easier to configure </b>(your server needs no update logic).
        In some cases, all you have to do is provide your FQDN (fully qualified
        domain name) and the CDN will automatically pull. (Of course you also need
        to rewrite URLs to point to the CDN servers).</td>
      <td style="text-align:left">Might require <b>more configuration</b> (when to update, what data to push).</td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Storage</b>
      </td>
      <td style="text-align:left">
        <p></p>
        <p>Can <b>minimize storage space</b> on the CDN by only storing recently-requested
          data.</p>
      </td>
      <td style="text-align:left">
        <p></p>
        <p><b>More storage</b> might be used (if you always push all your data).</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Traffic</b>
      </td>
      <td style="text-align:left">
        <p><b>Distributes high traffic</b> by serving cached data that is <b>frequently requested. </b>
        </p>
        <p></p>
        <p>However, might result in <b>redundant traffic</b> (and slower response)
          when unchanged data is frequently re-pulled. For example, if we have <b>low traffic resulting in frequent cache expiries</b>,
          or <b>very rare/irregular changes</b> relative to TTL (time-to-live).</p>
      </td>
      <td style="text-align:left">
        <p><b>Never any redundant traffic</b> caused by pulling unchanged data (only
          as much updates as you need).</p>
        <p></p>
        <p>However, too frequent changes may result in overloading your server, or
          high costs.</p>
        <p></p>
        <p><b>High traffic combined with changing data </b>might result in slow performance.
          Since your server is <b>blind to which data is being requested frequently</b>,
          it might be frequently pushing unrequested data while trying to ensure
          data is up to date.</p>
        <p>&lt;b&gt;&lt;/b&gt;</p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><b>Control</b> 
      </td>
      <td style="text-align:left"><b>Less control</b> (must wait for cache expiry for updates). Less flexible
        too.</td>
      <td style="text-align:left">
        <p></p>
        <p><b>More control</b> (consistency exactly when you specify it).</p>
      </td>
    </tr>
  </tbody>
</table>{% hint style="info" %}
## Pull CDN Use-Case: 

Sites/services with **heavy traffic**, **lots of data** \(particularly with **non-uniform/unpredictable distribution of demand across different data**\), and/or **unpredictable demand for data over time**, can benefit from a pull CDN, since it distributes traffic by **pulling only what is requested**, and **serving frequent requests from its cache.**

Examples: image/video hosting site, social network.
{% endhint %}

{% hint style="info" %}
## Push CDN Use-Case:

Sites/services with **infrequently updated data**, **big files \(e.g. 10mb or more\)**, **predictable/uniform distribution of demand across data** \(e.g. users will often want a fixed set of data\), **consistent demand for data over time**, or **low traffic** can benefit from a pull CDN. Or, sites/services with **real-time consistency requirements**.

Examples: blogs, archives, podcasts.
{% endhint %}

## What are some disadvantages of CDNs?

* Might get expensive. 
* Require configuration and changing URLs.
* In particular, TTL/push frequency must be configured appropriately or users get stale data.

{% hint style="info" %}
### Additional terminology: Origin and Edge servers

Origin servers are the origin of data. Edge servers get data from the origin server. A POP \(point of presence\) is a single physical location that consists of one or multiple edge servers.
{% endhint %}

## What are some CDN services?

### KeyCDN

Recommends Pull Zone for most cases. Recommends Push Zone for &gt; 10mb files.

## How to choose a CDN?

* Locations
* Performance
  * Certain CDN networks aim to employ concentrated amounts of low-performing POPs in particular locations while others aim to utilize a lesser amount of strategically placed, high-performing POPs. 
* Customizability/flexibility
* Price 
* HTTP/2 protocol support, SSL support?

## Sources:

[https://github.com/donnemartin/system-design-primer\#content-delivery-network](https://github.com/donnemartin/system-design-primer#content-delivery-network) [https://www.keycdn.com/support/how-does-a-cdn-work](https://www.keycdn.com/support/how-does-a-cdn-work)

## Read more:

[https://www.keycdn.com/blog/cdn-cache](https://www.keycdn.com/blog/cdn-cache)

