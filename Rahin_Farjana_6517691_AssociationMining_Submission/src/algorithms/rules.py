
from collections import defaultdict
from itertools import combinations

def generate_rules(frequent_itemsets, min_confidence):
    rules = []
    support = frequent_itemsets
    for itemset, supp in frequent_itemsets.items():
        if len(itemset) < 2:
            continue
        items = list(itemset)
        for r in range(1, len(items)):
            for antecedent in combinations(items, r):
                antecedent = frozenset(antecedent)
                consequent = itemset - antecedent
                if not consequent:
                    continue
                supp_ante = support.get(antecedent)
                if not supp_ante:
                    continue
                conf = supp / supp_ante
                if conf >= min_confidence:
                    rules.append((antecedent, consequent, supp, conf))
    rules.sort(key=lambda x: x[3], reverse=True)
    return rules

def build_recommendation_index(rules):
    index = defaultdict(list)
    for ante, cons, supp, conf in rules:
        for a in ante:
            for c in cons:
                index[a].append((c, conf))
    best_index = {}
    for item, recs in index.items():
        best = {}
        for c, conf in recs:
            best[c] = max(best.get(c, 0.0), conf)
        best_index[item] = sorted(best.items(), key=lambda x: x[1], reverse=True)
    return best_index

def interactive_query(recommend_index):
    print("\n=== Recommendation Query ===")
    if not recommend_index:
        print("No rules available for recommendations.")
        return
    items = sorted(recommend_index.keys())
    print("Available products with rules:")
    print(", ".join(items))
    print("Type a product name (or 'exit').")
    while True:
        q = input("Query> ").strip().lower()
        if q in ("exit", "quit"):
            break
        if q not in recommend_index:
            print("No recommendations for that product.")
            continue
        recs = recommend_index[q]
        print(f"Customers who bought '{q}' also bought:")
        for item, conf in recs:
            pct = int(round(conf * 100))
            bar = "█" * max(1, pct // 5)
            if pct >= 70:
                label = "Strong"
            elif pct >= 40:
                label = "Moderate"
            else:
                label = "Weak"
            print(f"- {item}: {pct}%  {bar} ({label})")
        print()
