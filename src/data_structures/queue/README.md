# Queue

+ [API](#api)
  + [enqueue](#enqueueitem)
  + [dequeue](#dequeue)
  + [front](#front)
  + [is_empty](#is_empty)
  + [size](#size)
+ [Implementations](#implementations)
  + `@TODO`
+ [References](#references)

### API

### enqueue(item)
Insert a new item at the back of the Queue

### dequeue()
Remove the item at the front of the Queue and return it
  + `returns (any)` The item at the front of the Queue
  + `throws (QueueEmptyException)` Exception is thrown when this opperation is performed on an empty Queue

### front()
Remove the item at the front of the Queue without removing it
  + `returns (any)` The item at the front of the Queue
  + `throws (QueueEmptyException)` Exception is thrown when this opperation is performed on an empty Queue

### is_empty()
Query if the Queue has any items
  + `returns (bool)` *True* if there are no items in the Queue and *False* otherwise

### size
The number of items that are in the Queue
  + `returns (int)` The number of items in the Queue

## Implementations
`@TODO`

## References
+ [Coursera: Introduction to Algorithms Part I](https://www.coursera.org/learn/introduction-to-algorithms)
+ [Textbook: Algorithms 4th Edition](http://algs4.cs.princeton.edu/15uf/)
