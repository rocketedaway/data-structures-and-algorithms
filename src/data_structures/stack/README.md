# Stack

+ [API](#api)
  + [push](#pushitem)
  + [pop](#pop)
  + [top](#top)
  + [is_empty](#is_empty)
  + [size](#size)
+ [Implementations](#implementations)
  + [Stack With Linked List](#stackwithlinkedlist)
  + [Stack With Resizing List](#stackwithresizinglist)
+ [References](#references)

### API

### push(item)
Insert a new item at the top of the Stack

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

### size
The number of items that are in the Stack
  + `returns (int)` The number of items in the Stack

## Implementations

### Stack With Linked List

[Source File](stack_linked_list.py)

For this implementation, a [Singly Linked List](../linked_list/linked_list.py) is used as the underlying data structure. Items are pushed and popped from the head of the Linked List.

### Underlying data structure example
```
  HEAD
|------|
| None |
|------|

push('Bar')

  HEAD
|-------|
| 'Bar' |
|-------|   |------|
|   ------> | None |
|-------|   |------|

push('Foo')

  HEAD
|-------|   |-------|
| 'Foo' |   | 'Bar' |
|-------|   |-------|   |------|
|   ------> |   ------> | None |
|-------|   |-------|   |------|

pop()

  HEAD
|-------|
| 'Bar' |
|-------|   |------|
|   ------> | None |
|-------|   |------|

```

#### Cost Model
```
|------|------|------|
| push | pop  | find |
|------|------|------|
| O(1) | O(1) | O(N) |
|------|------|------|
```

### Stack With Resizing List

[Source File](stack_list.py)

For this implementation, a pre-initilized List is used to illustrate the resizing functionality as Lists in Python already resize them selves. Items are inserted at the end of the List and removed from the end of the List.

The following rules govern when the underlying List is resized:
1. The List grows in size by 2x when the list is full
2. The List shrinks in size by 1/2 when the List is 1/4 full

#### Underlying data structure example
Resize (Increase Capacity):
```
Initial      [ - ]
          ^
          H

push('A')    [ A ]  (Resize)> [ A | - ]
               ^                ^
               H                H
```

Resize (Reduce Capacity):
```
Initial      [ A | B | - | - ]
                   ^
                   H

pop()        [ A | - | - | - ]  (Resize)> [ A | - ]
               ^                            ^
               H                            H
```

#### Cost Model
```
|------|------|------|
| push | pop  | find |
|------|------|------|
| O(1) | O(1) | O(N) |
|------|------|------|
```

## References
+ [Coursera: Introduction to Algorithms Part I](https://www.coursera.org/learn/introduction-to-algorithms)
+ [Textbook: Algorithms 4th Edition](http://algs4.cs.princeton.edu/15uf/)
