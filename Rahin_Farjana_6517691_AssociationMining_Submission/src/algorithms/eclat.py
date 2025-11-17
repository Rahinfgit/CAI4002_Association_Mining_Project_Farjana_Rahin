
from collections import defaultdict

def _build_vertical(transactions):
    vertical = defaultdict(set)
    for tid, tx in enumerate(transactions):
        for item in tx:
            vertical[item].add(tid)
    return vertical

def _eclat(prefix, items_tidsets, min_support, num_tx, results):
    while items_tidsets:
        item, tidset = items_tidsets.pop()
        new_itemset = prefix | frozenset([item])
        support = len(tidset) / num_tx
        if support >= min_support:
            results[new_itemset] = support
            new_children = []
            for other_item, other_tidset in items_tidsets:
                inter = tidset & other_tidset
                if inter:
                    new_children.append((other_item, inter))
            _eclat(new_itemset, new_children, min_support, num_tx, results)

def eclat(transactions, min_support):
    num_tx = len(transactions)
    vertical = _build_vertical(transactions)
    items_tidsets = list(vertical.items())
    results = {}
    _eclat(frozenset(), items_tidsets, min_support, num_tx, results)
    return results
