from collections import Counter, defaultdict
from itertools import groupby
from operator import itemgetter
from datetime import date

# Problems 1, 2, 3, 4, 6, 9
claims = [
    {"claim_id": "C001", "provider": "Apex Clinic",      "date": "2026-01-05", "amount": 250.00},
    {"claim_id": "C002", "provider": "Bayview Hospital", "date": "2026-01-05", "amount": 1200.50},
    {"claim_id": "C003", "provider": "Apex Clinic",      "date": "2026-01-06", "amount": 180.00},
    {"claim_id": "C004", "provider": "Cedar Pharmacy",   "date": "2026-01-06", "amount": 45.75},
    {"claim_id": "C005", "provider": "Bayview Hospital", "date": "2026-01-07", "amount": 980.00},
    {"claim_id": "C006", "provider": "Orchid Dental",    "date": "2026-01-07", "amount": 320.00},
    {"claim_id": "C007", "provider": "Apex Clinic",      "date": "2026-01-06", "amount": 180.00},
    {"claim_id": "C008", "provider": "Cedar Pharmacy",   "date": "2026-02-02", "amount": 60.25},
    {"claim_id": "C009", "provider": "Bayview Hospital", "date": "2026-02-03", "amount": 1500.00},
    {"claim_id": "C010", "provider": "Apex Clinic",      "date": "2026-02-03", "amount": 275.00},
    {"claim_id": "C011", "provider": "Bayview Hospital", "date": "2026-02-03", "amount": 1500.00},
    {"claim_id": "C012", "provider": "Zenith Lab",       "date": "2026-03-01", "amount": 410.00},
    {"claim_id": "C013", "provider": "Apex Clinic",      "date": "2026-03-02", "amount": 190.00},
    {"claim_id": "C014", "provider": "Cedar Pharmacy",   "date": "2026-03-02", "amount": 38.40},
]

# Problem 5: unsorted, with a repeated date and a gap
dates = ["2026-01-05", "2026-01-07", "2026-01-06", "2026-01-06",
         "2026-01-09", "2026-01-10", "2026-01-11", "2026-01-12", "2026-01-20"]

# Problem 6: a list of lists (batches of claims)
batches = [claims[:5], claims[5:9], claims[9:]]

# Problem 7: two months of provider totals
april = {"Apex Clinic": 300.0, "Bayview Hospital": 900.0, "Mercy Care": 150.0}
may   = {"Apex Clinic": 120.0, "Mercy Care": 80.0, "Zenith Lab": 60.0}

# Problems 8 and 10
raw_amounts = ["USD 1,234.50 Dr", "USD 980.00 Cr", "USD 45.75 Dr",
               "USD 10,000.00 Cr", "USD 0.99 Dr"]
opening_balance = 1000.00


#prob1: Given a list of claim payment dictionaries, return total paid per provider.
def claim_payment_per_provider(claims:list):
    claims_counter = Counter()
    for claim in claims:
        claims_counter[claim['provider']] += claim['amount']
    return claims_counter

#prob2: Same data: return the top 3 providers by amount paid.
def top_three_providers(providers:dict):
    top_three = Counter(providers).most_common(3)
    return top_three

#prob3: Group claim payments by month. Return a dictionary of month to list of amounts.
def amount_by_month(claims:list):
    month_amt_dict = defaultdict(list)
    for claim in claims:
        month = date.fromisoformat(claim['date']).strftime("%Y-%m")
        month_amt_dict[month].append(claim['amount'])
    return month_amt_dict

def duplicate_claim_payments(claims: list):
    claims_list = defaultdict(list)
    for claim in claims:
        key = (claim['provider'], claim['date'], claim['amount'])
        claims_list[key].append(claim['claim_id'])
    return [ids for ids in claims_list.values() if len(ids) > 1]
        

claims_per_provider = claim_payment_per_provider(claims)
top_three_providers_list = top_three_providers(claims_per_provider)
monthly_amount = amount_by_month(claims)
dup_claims = duplicate_claim_payments(claims)
print(dict(claims_per_provider))
print(top_three_providers_list)
print(dict(monthly_amount))
print(dup_claims)