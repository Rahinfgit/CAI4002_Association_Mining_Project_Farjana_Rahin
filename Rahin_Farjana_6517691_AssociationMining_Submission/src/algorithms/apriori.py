
from collections import defaultdict
from itertools import combinations

def _get_support_counts(transactions):
    counts = defaultdict(int)
    for tx in transactions:
        for item in tx:
            counts[frozenset([item])] += 1
    return counts

def _filter_by_support(counts, min_support, num_tx):
    min_count = min_support * num_tx
    return {
        itemset: count / num_tx
        for itemset, count in counts.items()
        if count >= min_count
    }

def apriori(transactions, min_support):
    num_tx = len(transactions)
    counts = _get_support_counts(transactions)
    Lk = _filter_by_support(counts, min_support, num_tx)
    all_freq = dict(Lk)
    k = 2
    while Lk:
        Lk_itemsets = list(Lk.keys())
        candidates = set()
        for i in range(len(Lk_itemsets)):
            for j in range(i + 1, len(Lk_itemsets)):
                a = Lk_itemsets[i]
                b = Lk_itemsets[j]
                union = a | b
                if len(union) == k:
                    valid = True
                    for subset in combinations(union, k - 1):
                        if frozenset(subset) not in Lk:
                            valid = False
                            break
                    if valid:
                        candidates.add(union)

        counts = defaultdict(int)
        for tx in transactions:
            for cand in candidates:
                if cand.issubset(tx):
                    counts[cand] += 1

        Lk = _filter_by_support(counts, min_support, num_tx)
        all_freq.update(Lk)
        k += 1
    return all_freq
