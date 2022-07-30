# Stacks and Queues
Queues, like the name suggests, follow the First-in-First-Out (FIFO) principle. 
As if waiting in a queue for the movie tickets, the first one to stand in line is
the first one to buy a ticket and enjoy the movie.

Stacks, like the name suggests, follow the Last-in-First-Out (LIFO) principle. 
As if stacking coins one on top of the other, the last coin we put on the top is 
the one that is the first to be removed from the stack later.

## Challenge
Using a Linked List as the underlying data storage mechanism, 
implement both a Stack and a Queue

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
### Time complexity for methods in Stack class:
push : O(1)

pop : O(1)

peek : O(1)

is_empty: O(1)

### Time complexity for methods in Stack class:
enqueue : O(1)

dequeue : O(1)

peek : O(1)

is_empty: O(1)
## API
<!-- Description of each method publicly available to your Stack and Queue-->

Stack :

- push - adds an element to the top of the stack.
- pop - removes the element at the top of the stack

Queue:
- enqueue - adds an element to the end of the queue.
- dequeue - removes the element at the beginning of the queue.

peek for both of them : Returns Value of the node located at the top of the stack

is_empty for both of them : Returns Boolean indicating whether the stack is empty or not.
