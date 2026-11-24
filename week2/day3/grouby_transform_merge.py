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
#print(f"Policies where count and size differ: {disagree}")

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

################ PART C ################

claims_copy = claims.copy()

#1. Add policy_total (sum of amount within the policy) to every claim row, then share_of_policy = claim_amount / policy_total. Check: the shares of each policy should add up to 1.
claims_copy['claims_per_policy'] = claims_copy.groupby('policy_id')['claim_amount'].transform('sum')
claims_copy['pct_claims_amt_per_policy'] = claims_copy['claim_amount']/claims_copy['claims_per_policy']
#print(claims_copy.sort_values(by='policy_id'))

#2. Create amount_filled: claim_amount, but where it's missing use the mean of that policy. (fillna + transform("mean").) How many are still missing, and why can that happen at all?
policy_mean = claims_copy.groupby('policy_id')['claim_amount'].transform('mean')
claims_copy['amount_filled'] = claims_copy['claim_amount'].fillna(policy_mean)
#print(claims_copy[['claim_id', 'policy_id', 'claim_amount', 'amount_filled']])

#3. Fill whatever is still missing with the mean of that row's claim_type. Confirm zero missing remain.
claims_type_mean = claims_copy.groupby('claim_type')['claim_amount'].transform('mean')
claims_copy['amount_filled'] = claims_copy['claim_amount'].fillna(claims_type_mean)
#print(claims_copy[['claim_id', 'policy_id', 'claim_amount', 'amount_filled']])

#4. Count claims whose amount is above the average of their own claim_type.
claims_copy['mean_claim_amount_per_claim_type'] = claims_copy.groupby('claim_type')['claim_amount'].transform('mean')
claims_count = claims_copy[claims_copy['claim_amount'] > claims_copy['mean_claim_amount_per_claim_type']]['claim_id'].count()
# print(claims_copy)
# print(claims_count)

#5. Without running it first, predict the row count of groupby(...)["claim_amount"].transform("sum") vs .agg("sum"). Then run both. In one sentence, when do you use each?
claims_transform = claims_copy.groupby('policy_id')['claim_amount'].transform("sum")
claims_agg = claims_copy.groupby('policy_id')['claim_amount'].agg("sum")
# print(claims_transform)
# print(claims_agg)
# We will use transform when we need the same row count and want to modify any column of dataframe or add a new column with mentioned treanformation, I'll use agg when I want to get aggregated amount wrt grouping condition.

################ PART D ################

claims_d = claims.copy()

#1. Sort by policy_id, claim_date, claim_id, then add claim_seq = 1, 2, 3… within each policy using cumcount() (it starts at 0, so add 1). What is the highest claim_seq?
sorted_claims = claims_d.sort_values(by=['policy_id', 'claim_date', 'claim_id'])
sorted_claims['claim_seq'] = sorted_claims.groupby('policy_id').cumcount()+1
#print(sorted_claims['claim_seq'].max())

#2. Add two ranks of claim_date within policy: rank(method="min") and rank(method="first"). They differ on some rows. Why? (Look at the ties.)
claims_d['rank_min'] = claims_d.groupby('policy_id')['claim_date'].rank(method='min')
claims_d['rank_first'] = claims_d.groupby('policy_id')['claim_date'].rank(method='first')
# print(claims_d.sort_values(by='rank_min'))
# print(claims_d.sort_values(by='rank_first'))
#rank method min will give same rank to tied values, but method first will give less rank to first value which comes in tie.

#3. Keep only the latest claim per policy with sort_values then drop_duplicates("policy_id", keep="last"). Shape?
latest_claim_per_policy = claims_d.sort_values(by=['policy_id', 'claim_date', 'claim_id']).drop_duplicates("policy_id", keep="last")
#print(latest_claim_per_policy)

#4. Do the same with groupby("policy_id").tail(1). Prove both give the same set of claim_ids.
last_claims_per_policy = claims_d.sort_values(['policy_id', 'claim_date', 'claim_id']).groupby('policy_id').tail(1)
#print(last_claims_per_policy.sort_values(by='policy_id'))

#5. Repeat Q3 but sort only by claim_date (no claim_id tie-breaker) after shuffling the rows (claims.sample(frac=1, random_state=1)). For how many policies does a different claim get picked? What does this teach you about "latest" when dates tie?
shuffled_claims = claims_d.sample(frac=1, random_state=1)
latest_claim_date_per_policy = shuffled_claims.sort_values(by=['policy_id', 'claim_date']).drop_duplicates("policy_id", keep="last")
#print(latest_claim_date_per_policy)

#6. Take the first claim per policy and add days_to_first_claim = claim date minus policy start_date. Merge start_date in with validate="m:1" first. Describe the result (.describe()).
first = (claims.sort_values(['policy_id', 'claim_date', 'claim_id'])
         .drop_duplicates('policy_id', keep='first')
         .merge(policies[['policy_id', 'start_date']], on='policy_id',
                how='inner', validate='m:1'))
first['days_to_first_claim'] = (first['claim_date'] - first['start_date']).dt.days
#print(first['days_to_first_claim'].describe())   # count 342, median 112.5