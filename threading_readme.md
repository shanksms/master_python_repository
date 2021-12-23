# Important python threading concepts
### resources
[python concurrency] (https://learning.oreilly.com/library/view/mastering-concurrency-in)

### what is a thread
In the field of computer science, a thread of execution is the smallest unit of programming commands 
(code) that a scheduler (usually as part of an operating system) can process and manage. 
Depending on the operating system, the implementation of threads and processes 
(which we will cover in future chapters) varies, but a thread is typically an element (a component) of a process.

### The threading module in Python 3
The old thread module has been considered deprecated by Python developers for a long time, mainly because of its rather
low-level functions and limited usage. The threading module, on the other hand, is built on top of the thread module, 
providing easier ways to work with threads through powerful, higher-level APIs. Python users have actually been 
encouraged to utilize the new threading module over the thread module in their programs.
In addition to all of the functionality for working with threads that the thread module provides, the threading module supports a number of extra methods, as follows:

threading.activeCount(): This function returns the number of currently active thread objects in the program
threading.currentThread(): This function returns the number of thread objects in the current thread control from the caller
threading.enumerate(): This function returns a list of all of the currently active thread objects in the program
Following the object-oriented software development paradigm, the threading module also provides a Thread class that supports the object-oriented implementation of threads. The following methods are supported in this class:

run(): This method is executed when a new thread is initialized and started
start(): This method starts the initialized calling thread object by calling the run() method
join(): This method waits for the calling thread object to terminate before continuing to execute the rest of the program
isAlive(): This method returns a Boolean value, indicating whether the calling thread object is currently executing
getName(): This method returns the name of the calling thread object
setName(): This method sets the name of the calling thread object
