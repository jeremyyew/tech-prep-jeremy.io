# OS

* Process
  * PCB - process control block
  * Process state: new, ready, running, waiting, terminated
  * program counter: address of next instruction
  * Registers
  * Memory:
    * Stack **- function parameters, local variables, return addresses**
    * Data - **global variables \(static\)**
    * Heap - **dynamic memory \(global too\)**
    * Text - code

![](../.gitbook/assets/screenshot-2020-01-04-at-5.10.41-pm.png)



* Threads 
  * Its own program counter, register set, and stack.
  * Shares heap, data, text with rest of threads belonging to same process.

![](../.gitbook/assets/screenshot-2020-01-04-at-5.24.10-pm.png)



* Scheduling 
  * Long-term: selects processes from job pool \(disk\) to ready queue \(memory\) for execution
* Context switching
  * 
* Mutex
* Semaphore
* Physical vs logical memory
*   ![](https://paper-attachments.dropbox.com/s_FFF6B33FF01B94225D4760701803C6736F40027A549107A905DBE357062E64F1_1535990510875_Screen+Shot+2018-09-04+at+12.01.11+AM.png)

