from collections import Counter, defaultdict
import itertools

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
def total_paid_provider(claims):
    output_dict = {}
    for i in claims:
        if i['provider'] in output_dict.keys():
            output_dict[i['provider']] = output_dict[i['provider']] + i['amount']
        else:
            output_dict[i['provider']] =  i['amount']
    cnt = 0
    for k,v in sorted(output_dict.items(), key=lambda item:item[1], reverse=True):
        if cnt == 3:
            break
        else:
            cnt +=1 
            print(k,v)

total_paid_provider(claims)