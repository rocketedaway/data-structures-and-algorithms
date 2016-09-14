# Union-Find (Disjoint-Set)

+ [API](#api)
  + [union] (#unionnodea-nodeb)
  + [find] (#findnode)
  + [connected] (#connectednode_a-nodeb)
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

A simple implementation of the Union-Find data structure that optimizes just the find/connected operations

#### The underlying data structure:
```
(List Indicies)     0   1   2   3   4   5   6   7 ... N
(List Values)       0 | 1 | 1 | 1 | 4 | 5 | 5 | 5 ... N

The above has 4 distinct components with members:
0 => { 0 }, 1 => { 1,2,3 }, 4 => { 4 }, 5 => { 5,6,7 }
```

#### Cost Model:
```
-------------------------------------------
| Construction | Union | Find | Connected |
-------------------------------------------
|      N       |   N   |   1  |     1     |
-------------------------------------------

@TODO: Add explanation as to why this is optimized for the Find command
```

### Quick-Union

A simple implementation of the Union-Find data structure that optimizes the union operation

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

#### Cost Model:
```
-------------------------------------------
| Construction | Union | Find | Connected |
-------------------------------------------
|      N       |   N   |   N  |   N^2     |
-------------------------------------------

@TODO: Add explanation as to why this is optimized for the Union command
@TODO: Add explanation of the problems with this implementation
```

### Weighted-Quick-Union

A simple implementation of the Union-Find data structure that further optimizes the union operation

#### The underlying data structure:
@TODO: Add explanation of the unnderlying data sructure and how it works

#### Cost Model:
```
-------------------------------------------
| Construction | Union | Find | Connected |
-------------------------------------------
|      N       | ln(N) |   *  |   ln(N)   |
-------------------------------------------
* The Find command is proportional to the height of the two components


@TODO: Add explanation as to why this is optimized for the Union command and why its different from the Quick-Union implementation
@TODO: Add explanation of the problems with this implementation
```
