
import csv

def load_valid_products(path):
    valid = set()
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for row in reader:
                if not row:
                    continue
                if len(row) >= 2:
                    name = row[1].strip().lower()
                else:
                    name = row[0].strip().lower()
                if name:
                    valid.add(name)
    except FileNotFoundError:
        print(f"ERROR: products file not found at {path}")
    return valid

def parse_items(text):
    if not text:
        return []
    parts = text.split(',')
    return [p.strip().lower() for p in parts if p.strip()]

def load_transactions_from_csv(path):
    transactions = []
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            header = next(reader, None)
            for row in reader:
                if not row:
                    transactions.append([])
                    continue
                if len(row) >= 2:
                    items_text = row[1]
                else:
                    items_text = row[0]
                items = parse_items(items_text)
                transactions.append(items)
    except FileNotFoundError:
        print(f"ERROR: transactions file not found at {path}")
    return transactions
