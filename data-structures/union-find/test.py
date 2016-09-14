from quick_find import QuickFind
from quick_union import QuickUnion
from quick_union_weighted import WeightedQuickUnion

def run_test(union_find):
    union_find.union(2, 1)
    union_find.union(3, 1)

    union_find.union(5, 4)
    union_find.union(6, 5)
    union_find.union(7, 5)

    assert union_find.connected(0, 0)
    for n in range(1, N):
        assert not union_find.connected(0, n)

    for n in range(1, 4):
        for m in range(1, 4):
            assert union_find.connected(n, m)

    for n in range(4, N):
        for m in range(4, N):
            assert union_find.connected(n, m)

    for n in range(1, 4):
        for m in range(4, N):
            assert not union_find.connected(n, m)

    assert union_find.count() == 3

N = 8

print 'Quick-Find Test Started'
run_test(QuickFind(N))
print 'Quick-Find Test Finished'

print 'Quick-Union Test Started'
run_test(QuickUnion(N))
print 'Quick-Union Test Finished'

print 'Weighted-Quick-Union Test Started'
run_test(WeightedQuickUnion(N))
print 'Weighted-Quick-Union Test Finished'
