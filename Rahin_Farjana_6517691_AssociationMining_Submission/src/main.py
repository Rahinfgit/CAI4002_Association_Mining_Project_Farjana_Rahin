
import time
from preprocessing.loader import load_valid_products, load_transactions_from_csv
from preprocessing.cleaner import preprocess_transactions, print_preprocessing_report
from algorithms.apriori import apriori
from algorithms.eclat import eclat
from algorithms.rules import generate_rules, build_recommendation_index, interactive_query

PRODUCTS_CSV = "data/products.csv"
TRANSACTIONS_CSV = "data/sample_transactions.csv"
DEFAULT_MIN_SUPPORT = 0.2
DEFAULT_MIN_CONFIDENCE = 0.5

def main():
    print("=== Supermarket Association Rule Mining ===")
    valid_products = load_valid_products(PRODUCTS_CSV)
    print(f"Loaded {len(valid_products)} valid products.\n")

    raw_transactions = load_transactions_from_csv(TRANSACTIONS_CSV)
    print(f"Loaded {len(raw_transactions)} raw transactions.\n")

    transactions, report = preprocess_transactions(raw_transactions, valid_products)
    print_preprocessing_report(report)

    if not transactions:
        print("No valid transactions after preprocessing. Exiting.")
        return

    try:
        min_support = float(input(
            f"Enter minimum support (0–1, default {DEFAULT_MIN_SUPPORT}): "
        ) or DEFAULT_MIN_SUPPORT)
        min_conf = float(input(
            f"Enter minimum confidence (0–1, default {DEFAULT_MIN_CONFIDENCE}): "
        ) or DEFAULT_MIN_CONFIDENCE)
    except ValueError:
        print("Invalid input, using defaults.")
        min_support = DEFAULT_MIN_SUPPORT
        min_conf = DEFAULT_MIN_CONFIDENCE

    print(f"Using min_support={min_support:.2f}, min_confidence={min_conf:.2f}\n")

    t0 = time.time()
    freq_ap = apriori(transactions, min_support)
    t1 = time.time()
    rules_ap = generate_rules(freq_ap, min_conf)
    t2 = time.time()
    print(f"Apriori: {len(freq_ap)} frequent itemsets, {len(rules_ap)} rules, "
          f"{(t1-t0)*1000:.2f} ms (itemsets), {(t2-t1)*1000:.2f} ms (rules)")

    t3 = time.time()
    freq_ec = eclat(transactions, min_support)
    t4 = time.time()
    rules_ec = generate_rules(freq_ec, min_conf)
    t5 = time.time()
    print(f"Eclat:   {len(freq_ec)} frequent itemsets, {len(rules_ec)} rules, "
          f"{(t4-t3)*1000:.2f} ms (itemsets), {(t5-t4)*1000:.2f} ms (rules)")

    rec_index = build_recommendation_index(rules_ec)
    interactive_query(rec_index)

if __name__ == "__main__":
    main()
