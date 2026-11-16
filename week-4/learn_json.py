import json

with open('data/policies.json', encoding='utf-8') as f:
    json_load = json.load(f)
    policies = json_load['policies']
    for policy in policies:
        print(policy)

with open('data/active_policies.json', 'w', encoding='utf-8') as f:
    active_policies = [policy for policy in policies if policy['status']=='active']
    load_active_policies = json.dump(active_policies, f, indent=2)