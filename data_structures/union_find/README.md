# Union-Find (Disjoint-Set)

+ [API](#api)
  + [union] (#unionnode_a-node_b)
  + [find] (#findnode)
  + [connected] (#connectednode_a-node_b)
  + [count] (#count)
+ [Implementations](#implementations)
  + [Quick-Find](#quick-find)
  + [Quick-Union](#quick-union)
  + [Weighted-Quick-Union](#weighted-quick-union)

### API

### union(node_a, node_b)
Add connection between node_a and all other nodes in the same component to the component of node_b
  + `node_a (int)` A node in the data strucutre
  + `node_b (int)` Another node in the data strucutre

### find(node)
Find the component identifier which contains the specified node
  + `node (int)` A node in the data strucutre
  + `returns (int)` A component identifier

### connected(node_a, node_b)
Check if a connection between node_a and and node_b exists
  + `node_a (int)` A node in the data strucutre
  + `node_b (int)` Another node in the data strucutre
  + `returns (bool)` *True* if a connection exists and *False* otherwise

### count()
Query how many distinct components there are in the data structure
  + `returns (int)` The number of distinct components

## Implementations

### Quick-Find

[Source File](https://github.com/rocketedaway/data-structures-and-algorithms/blob/master/data_structures/union_find/quick_find.py)

A naive implementation of the Union-Find data structure that optimizes just the `find(node)` and `connected(node_a, node_b)` methods.

The data is stored in a array (list) where the array (list) indicies are the ids of the nodes and the values at those indicies are the ids of the components that the nodes belong too.

The `find(node)` and `connected(node_a, node_b)` methods are very performant as they only require at most 2 look-ups, giving them a constant running time(O(1)). The `union(node_a, node_b)` command on the other hand needs to iterate over every node which is connected to `node_a` (the whole component) and update them to be in the component of `node_b`. As the amount of nodes grows this method has a maximum running time of O(N), where N is the number of nodes in the data structure. When you take into account that this data structure's initilization has a running time of O(N), it will take upwords of N^2 array (list) accesses to preform N `union(node_a, node_b)` commands.

#### Example:
```
Indicies      0   1   2   3   4   5   6   7
Values      [ 0 | 1 | 1 | 1 | 4 | 5 | 5 | 5 ]

The above has 4 distinct components with members:
0 => { 0 }, 1 => { 1,2,3 }, 4 => { 4 }, 5 => { 5,6,7 }
```

### Quick-Union

[Source File](https://github.com/rocketedaway/data-structures-and-algorithms/blob/master/data_structures/union_find/quick_union.py)

A simple implementation of the Union-Find data structure that optimizes the union operation

@TODO
+ Add in depth explanation of how this version of the data structure works
+ Add explanation as to why this is optimized for the Union command
+ Add explanation of the problems with this implementation

#### The underlying data structure:
```
(List Indicies)     0   1   2   3   4   5   6   7 ... N
(List Values)       0 | 1 | 1 | 1 | 4 | 4 | 5 | 5 ... N

The above has 3 distinct components {0, 1, 4} with members:

[0]      [1]       [4]
        /   \       |
      [2]   [3]    [5]
                  /   \
                [6]   [7]
```

### Weighted-Quick-Union

[Source File](https://github.com/rocketedaway/data-structures-and-algorithms/blob/master/data_structures/union_find/quick_union_weighted.py)

A simple implementation of the Union-Find data structure that further optimizes the union operation

@TODO
+ Add in depth explanation of how this version of the data structure works
+ Add explanation as to why this is optimized for the Union command and why its different from the Quick-Union implementation

#### The underlying data structure:
@TODO
+ Add explanation of the underlying data sructure and how it works
