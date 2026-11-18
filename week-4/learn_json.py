import json
import logging

json_file_path='data/policies.json'
log_file_path='../log.txt'


logging.basicConfig(level=logging.INFO, filename=log_file_path, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
logger = logging.getLogger(__name__)

try:
    with open(json_file_path, encoding='utf-8') as f:
        json_load = json.load(f)
    policies = json_load['policies']
except FileNotFoundError:
    logger.error("File not found: %s", json_file_path)
except json.JSONDecodeError:
    logger.exception("Json isn't in right format: %s", json_file_path)
except KeyError:
    logger.exception("Policies key not found: %s", json_file_path)
else:
    logger.info("%s policies loaded", len(policies))
    for policy in policies:
        logger.debug(policy)


with open('data/active_policies.json', 'w', encoding='utf-8') as f:
    active_policies = [policy for policy in policies if policy['status']=='active']
    load_active_policies = json.dump(active_policies, f, indent=2)