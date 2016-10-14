# Stack

+ [API](#api)
  + [push](#pushelement)
  + [pop](#pop)
  + [is_empty](#is_empty)
  + [size](#size)
+ [Implementations](#implementations)
  + `@TODO`
+ [References](#references)

### API

### push(item)
Insert a new item at the head of the Stack
  + `item (any)` The item to insert into the Stack

### pop()
Remove the first item in the Stack and return it
  + `returns (any)` The first item in the Stack
  + `throws (StackEmptyException)` Exception is thrown when this opperation is performed on an empty Stack

### top()
Returns the first item in the Stack without removing it
  + `returns (any)` The first item in the Stack
  + `throws (StackEmptyException)` Exception is thrown when this opperation is performed on an empty Stack

### is_empty()
Query if the Stack has any items
  + `returns (bool)` *True* if there are no items in the Stack and *False* otherwise

### size()
Query how many items are in the Stack
  + `returns (int)` The number of items in the Stack

## Implementations
`@TODO`

## References
+ [Coursera: Introduction to Algorithms Part I](https://www.coursera.org/learn/introduction-to-algorithms)
+ [Textbook: Algorithms 4th Edition](http://algs4.cs.princeton.edu/15uf/)
