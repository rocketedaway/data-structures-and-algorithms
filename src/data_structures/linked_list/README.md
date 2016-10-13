# Linked List

+ [API](#api)
  + [push](#pushpayload)
  + [pop](#pop)
  + [is_empty](#is_empty)
  + [head](#head)
+ [Implementations](#implementations)
  + [Singly Linked List](#singly-linked-list)

### API

### push(payload)
Insert a new node at the front of the Linked List
  + `payload (any)` The payload of the node to be inserted into the Linked List
  + `returns (node)` The node that was just inserted

### pop()
Remove the first node of Linked List and return it's payload
  + `returns (any)` The payload of the removed node in the Linked List
  + `throws (LinkedListEmptyException)` Exception is thrown when this opperation is performed on an empty list

### is_empty()
Query if the Linked List has any nodes in it
  + `returns (bool)` *True* if the head of the Linked List is equal to *None* and *False* otherwise

### head()
Return the payload of the head node
  + `returns (any)` The payload of the head node in the Linked List if it exists or *None*
  + `throws (LinkedListEmptyException)` Exception is thrown when this opperation is performed on an empty list

## Implementations

### Singly Linked List

[Source File](linked_list.py)

This implementation's nodes only hold a link to the next node in the list. Nodes are inserted and removed from head of the list. This implementation is a FIFO data structure and provides constant time `push` and `pop` methods.

The problem with this implementations is that there is no random access and to find a node you need to iterate over at most `N` nodes were `N` is the number of nodes in the list.

#### Node class definition
```
|--------------|
| Node         |
|--------------|
| Node next    |
| Any  payload |
|--------------|
```

#### Underlying data structure example
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
```

#### Cost Model
```
|-------|-------|-------|
| Push  | Pop   | Find  |
|-------|-------|-------|
| O(1)  | O(1)  | O(N)  |
|-------|-------|-------|
```

