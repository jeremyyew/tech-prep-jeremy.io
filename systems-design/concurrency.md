# Concurrency

{% embed url="https://hackernoon.com/concurrent-programming-in-python-is-not-what-you-think-it-is-b6439c3f3e6a" %}

## Concurrency in Python

* Options:
  * multithreading
    * Perfectly fine for IO-bound. 
    * For CPU-bound, there is no true parallelism even with multiple processors. CPython uses GIL \(global interpreter lock\), which is basically a mutex on the interpreter itself - only one thread can control the interpreter. So threads simply have to wait and cannot operate in parallel. 
    * GIL came about since memory management is handled by reference counting, which requires synchronization. Also allowed for non-thread safe C extensions to python. 
  * multiprocessing 
    * Does allow parallelism since each process will only have one thread. As long as the overhead of creating new process is acceptable. 
* Alternatives:
  * Jython. However, most libraries. 
  * Cython \(NOT CPython\), Java, Scala, Go. 

## Synchronization constructs

* Mutex - Mutually exclusive access. 
  * Lock - acquire and release. 
  * Semaphores - restrict access to multiple. Wait and signal. 
  * Monitors - mutex lock but with ability to wait on condition, and signal when condition is \(possibly\) fulfilled. Avoid busy waiting/spinning. Acquire, wait, signal, release. 

