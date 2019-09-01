---
description: 'https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/'
---

# Salting and Hashing

{% hint style="info" %}
A salt is added to the hashing process to force their uniqueness, increase their complexity without increasing user requirements, and to mitigate password attacks like rainbow tables**.** 
{% endhint %}

* Adding random data to the input of a hash function to guarantee a unique hash even when the inputs are the same.
* **Salting** is a security measure that makes it exponentially harder for hackers to carry out brute force attacks, especially with rainbow tables. 
  * Must be generated for every password. 
  * They can be transparent. \(See below\)
* **Brute force attack:** 
  * Try many passwords on one account/one password on many accounts. 
  * Given a stolen database of hashed passwords and knowledge/intelligent guesses of which hashes were used, compare a list of common/stolen passwords \(hashed\) to figure out the original password. 
  * A **rainbow table** is simply precomputed list of hashed words- requires lots of memory. 
* **How salting protects against brute force attacks:** 
  * Unfeasible for rainbow tables to account for the salts. Even if the salt for a specific account \(or all individual salts for many accounts\) is known, the rainbow table can only be precomputed using a specific hash and that single. 
  * Repeated passwords: 
    * People who use obvious passwords are safer. 
    * People who use the same passwords across accounts are safer. 
    * It makes any duplicate values in the table of hashed passwords very unlikely, making it hard to spot the existence of common passwords. 
    * People who happen to share passwords are not compromised together. 
* Common hashes: 
  * MD4, MD5 - vulnerable 
  * SHA \(Security hashing algorithm\): SHA-1 deperecated. SHA-2 used in SSL/TLS connections. 

