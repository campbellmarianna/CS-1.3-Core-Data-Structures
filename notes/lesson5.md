# By April 24 have a draft 50 to 70 percent done
- Show yourself as a professional software engineer
- technical
- show your effective communicator
- 800 word article
- 5 to 8 minutes
- Pictures and diagrams are required
- Crediting Format Source: (Link to place)
- attribute source

## Tip
- Start a draft

## Homework (This week!)
- 5 to 6 bullet points (headers for article)

### Notes
Concrete Data Structures (backend)
- Array (contiguous memory w/ indexes)
    -static

Abstract Data Types (API)
- List (ordered sequence) (were going to add rules to the list)
    - add, remove, replace
    - Stack (buffee line, plates)
        - stack of plates  
        - can only take a plate off the top
        - push - add an object to top
        - pop - remove and return the object
        - peek - view the object on the top
        - LIFO - last in, first out
    - Queue
        - wait in lines (start in the back move through the middle, come out in the front)
        - enquene - add an object to the back
        - dequeue - remove and return the object at the front
        - front - view the object at the front
        - FIFO - first in, first out
    STACK & QUEUE
    Optional methods
    isEmpty - return
    isFull - return bools

## Homework
- not complicated challenges

Arrays
[x] Inserting and deleting can be really slow.
[x] Searching is fast.
[x] Static + fixed size, not as easy to grow or shrink.
[x] Allocates memory when created, a contiguous chunk of resources, even if all of that space isn't filled.
[x] Finding elements is fast, and since arrays are index and use contiguous memory, binary search is an option
-> helpful if you do know the size of the list, you need random access to elements, or want to iterate quickly.

Linked Lists
[x] Inserting and deleting can be really fast.
[x] Searching is slow.
[x] Dynamic size, can grow or shrink easily.
[x] Only allocates resources as required at runtime, using non-contiguous chunk of memory as needed.
[x] Finding elements requires traversal, and traversal is slow since you can't use binary search.
-> helpful if you don't know the size of the list, and mostly want to add or remove things quickly without random access.

Information Source: Vaidehi Joshi
