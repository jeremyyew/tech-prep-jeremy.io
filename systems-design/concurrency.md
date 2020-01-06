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

## Deadlocks: prevention 

A deadlocked state occurs when two or more processes are waiting indefinitely for an event that can be caused only by one of the waiting processes. There are three principal methods for dealing with deadlocks:

* Usesomeprotocoltopreventoravoiddeadlocks,ensuringthatthesystem will never enter a deadlocked state.
* Allowthesystemtoenteradeadlockedstate,detectit,andthenrecover.
* Ignore the problem altogether and pretend that deadlocks never occur in

  the system.

* The third solution is the one used by most operating systems, including Linux and Windows.
* A deadlock can occur only if four necessary conditions hold simultaneously in the system: mutual exclusion, hold and wait, no preemption, and circular wait. To prevent deadlocks, we can ensure that at least one of the necessary conditions never holds.
* A method for avoiding deadlocks, rather than preventing them, requires that the operating system have a priori information about how each process will utilize system resources. The banker’s algorithm, for example, requires a priori information about the maximum number of each resource class that each process may request. Using this information, we can define a deadlock- avoidance algorithm.
* If a system does not employ a protocol to ensure that deadlocks will never occur, then a detection-and-recovery scheme may be employed. A deadlock- detection algorithm must be invoked to determine whether a deadlock has occurred. If a deadlock is detected, the system must recover either by terminating some of the deadlocked processes or by preempting resources from some of the deadlocked processes.
* Where preemption is used to deal with deadlocks, three issues must be addressed: selecting a victim, rollback, and starvation. In a system that selects victims for rollback primarily on the basis of cost factors, starvation may occur, and the selected process can never complete its designated task.
* Researchers have argued that none of the basic approaches alone is appro- priate for the entire spectrum of resource-allocation problems in operating systems. The basic approaches can be combined, however, allowing us to select an optimal approach for each class of resources in a system.



