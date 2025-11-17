
def preprocess_transactions(raw_transactions, valid_products):
    before_count = len(raw_transactions)
    empty_count = 0
    single_count = 0
    duplicate_instances = 0
    invalid_items_count = 0
    standardized_items = 0

    cleaned = []
    for tx in raw_transactions:
        if not tx:
            empty_count += 1
            continue

        standardized_items += len(tx)
        duplicate_instances += len(tx) - len(set(tx))
        tx_set = set(tx)

        valid_items = {i for i in tx_set if i in valid_products}
        invalid_items_count += len(tx_set) - len(valid_items)

        if len(valid_items) == 0:
            empty_count += 1
            continue
        if len(valid_items) == 1:
            single_count += 1
            continue

        cleaned.append(frozenset(valid_items))

    after_count = len(cleaned)
    total_items_after = sum(len(tx) for tx in cleaned)
    unique_products_after = len(set().union(*cleaned)) if cleaned else 0

    report = {
        "before_transactions": before_count,
        "after_transactions": after_count,
        "empty_transactions": empty_count,
        "single_item_transactions": single_count,
        "duplicate_instances": duplicate_instances,
        "invalid_items": invalid_items_count,
        "standardized_items": standardized_items,
        "total_items_after": total_items_after,
        "unique_products_after": unique_products_after,
    }
    return cleaned, report

def print_preprocessing_report(report):
    print("Preprocessing Report")
    print("--------------------")
    print("Before Cleaning:")
    print(f"  Total transactions: {report['before_transactions']}")
    print(f"  Empty transactions: {report['empty_transactions']}")
    print(f"  Single-item transactions: {report['single_item_transactions']}")
    print(f"  Duplicate items found: {report['duplicate_instances']}")
    print(f"  Invalid items found: {report['invalid_items']}")
    print()
    print("After Cleaning:")
    print(f"  Valid transactions: {report['after_transactions']}")
    print(f"  Total items: {report['total_items_after']}")
    print(f"  Unique products: {report['unique_products_after']}")
    print()
