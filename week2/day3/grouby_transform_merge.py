import pandas as pd

claims = pd.read_csv('../../data/claims.csv', parse_dates=['claim_date'])
policies = pd.read_csv('../../data/policy.csv', parse_dates=['start_date'])
customers = pd.read_csv('../../data/customers.csv', parse_dates=['signup_date'])
cust_dupes = pd.read_csv('../../data/customers_with_dupes.csv', parse_dates=['signup_date'])


################ PART A ################

#1. Print the shape of all four tables.
# print(claims.shape)
# print(policies.shape)
# print(customers.shape)
# print(cust_dupes.shape)

#2. How many claim_amount values are missing, and what percent of claims is that?
claims_count = claims['claim_id'].count()
claims_amount_empty = claims['claim_amount'].isna().sum()
percent_empty_claim_amount = (claims_amount_empty/claims_count)*100
# print(claims_amount_empty)
# print(percent_empty_claim_amount)

#3. For each table, is the key column unique? (.is_unique) Which one is not?
claims_unique = claims['claim_id'].is_unique
policies_unique = policies['policy_id'].is_unique
customers_unique = customers['customer_id'].is_unique
customer_dup_unique = cust_dupes['customer_id'].is_unique
# print(claims_unique)
# print(policies_unique)
# print(customers_unique)
# print(customer_dup_unique)

#4. How many claims have a policy_id that does not exist in policies? How many policies have a customer_id that does not exist in customers? (Hint: .isin() and ~ to flip True/False.
non_existent_policies = (~claims['policy_id'].isin(policies['policy_id'])).sum()
non_existent_customers = (~policies['customer_id'].isin(customers['customer_id'])).sum()   
# print(non_existent_policies)
# print(non_existent_customers)

################ PART B ################

#1. Total claim_amount per policy_id. How many policies (envelopes) come out?
total_claims_per_policy = claims.groupby('policy_id')[['claim_amount']].sum().reset_index()
# print(total_claims_per_policy)
# print(len(total_claims_per_policy))

#2. Redo it with named outputs in one call: total (sum of amount), count (number of claims), mean (average amount). Use .agg(total=("claim_amount","sum"), ...) and .reset_index() so policy_id becomes a normal column.
claims_details = claims.groupby('policy_id').agg(total=("claim_amount", "sum"), No_of_claims=("claim_id", "count"), average_amount=("claim_amount", "mean")).reset_index()
#print(claims_details)

#3. count on claim_amount skips missing values; size() counts every row. For how many policies do they disagree?
g = claims.groupby('policy_id')
disagree = (g['claim_amount'].count() != g.size()).sum()
print(f"Policies where count and size differ: {disagree}")
#4. Question 1 gave more groups than there are real policies with claims. Find out why and list the extra IDs. (This is the orphan trap from A4 showing up.)
real_policies = set(policies['policy_id'])
extra_policies = sorted(set(claims['policy_id']) - real_policies)
# print(extra_policies)
# print(claims['policy_id'].nunique(), "groups", claims['policy_id'].nunique() - len(extra_policies), "real")

#5. Group by two columns, policy_id and claim_type, and sum the amount. How many rows?
claims_policy_claims_type = claims.groupby(['policy_id', 'claim_type'])['claim_amount'].sum()
# print(claims_policy_claims_type)
# print(len(claims_policy_claims_type))

#6. Show the 5 policies with the biggest total. (nlargest)
largest_5_claims_amount_policies = total_claims_per_policy.nlargest(5, "claim_amount").reset_index()
# print(largest_5_claims_amount_policies)