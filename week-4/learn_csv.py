import csv
with open('data/policies.csv', newline='') as csv_open:
    csv_reader = csv.DictReader(csv_open)
    csv_data = list(csv_reader)
    #print(csv_data)
    for data in csv_data:
        print(data['policy_id'], data['customer_name'], data['product'], data['start_date'], data['sum_insured'], data['annual_premium'], data['status'], data['city'])


with open('data/new_policies.csv', 'w', newline='') as csv_open:
    csv_writer = csv.DictWriter(csv_open, ['policy_id', 'customer_name', 'product', 'start_date', 'sum_insured', 'annual_premium', 'status', 'city'])
    csv_writer.writeheader()
    for data in csv_data:
        csv_writer.writerow(data)