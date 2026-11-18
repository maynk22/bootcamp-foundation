import json
import logging

DEFAULT_KEY = 'policies'

logger = logging.getLogger(__name__)

def load_json_file(path):
    try:
        with open(path, encoding='utf-8') as f:
            json_load = json.load(f)
        return json_load[DEFAULT_KEY]
    except FileNotFoundError:
        logger.error("File not found: %s", path)
    except json.JSONDecodeError:
        logger.exception("Json isn't in right format: %s", path)
    except KeyError:
        logger.exception("Policies key not found: %s", path)