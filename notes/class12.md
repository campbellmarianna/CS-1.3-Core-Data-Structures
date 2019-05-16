# Recursion is function calls after it is done.
# When talking about complexity
 - time: O(n)
    - n * visit
    - n * left tree
    - n * right tree
    - 3n * if
    -----------------
    - 6n operations
 - it takes time to call a function
 # The max length of the stack is the height of the tree
 - space: 0(height)
    - height = log n if balanced
    - approches n if not balanced
# Iteratively
- Stack keep track like an undo and/or keep track of things I have to do

# Level Order Recursive
Time:
    - O(n) n * visit
    - n * dequeue
    - 2n * enq
    ------------------
    4n operations
