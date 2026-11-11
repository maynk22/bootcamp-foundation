claims = [
       {"id": 1, "amount": 500},
       {"id": 2, "amount": 120},
       {"id": 3, "amount": 900},
   ]

print(sorted(claims, key=lambda c: c["amount"]))