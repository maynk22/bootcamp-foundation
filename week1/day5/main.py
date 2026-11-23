import logging
from week1.day5.load_json_file import load_json_file
from week1.day5.write_to_json import write_json_file

json_file_path='../week-4/data/policies.json'
write_file_path = '../week-4/data/active_policies.json'
log_file_path='../log.txt'

logger = logging.getLogger(__name__)

def main():
    policies = load_json_file(json_file_path)
    if policies is None:
        return
    logger.info("Loaded %d policies", len(policies))

    active_policies = write_json_file(write_file_path, policies)
    if active_policies is None:
        return
    logger.info("Added %d active policies to %s", len(active_policies), write_file_path)

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO, 
        filename=log_file_path, 
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
        )
    main()
