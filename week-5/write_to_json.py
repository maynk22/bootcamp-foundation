import json
import logging

logger = logging.getLogger(__name__)

def write_json_file(path, policies):
    try:
        active_policies = [policy for policy in policies if policy['status']=='active']
    except KeyError:
        logger.exception("A policy is missing 'status' key")
        return None

    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(active_policies, f, indent=2)
    except (OSError, TypeError):
        logger.exception("Could not write %s", path)
        return None

    return active_policies