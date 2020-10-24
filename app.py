import json
from loguru import logger
import requests
from config import *


def main():
    url = TARGET_URL
    with open(REQ_BODY, 'r') as infile:
        payload = json.load(infile)

    logger.info(f'Issuing request to {url}...')
    logger.debug(f'Request payload = {payload}')
    r = requests.post(url, json=payload)
    logger.info(f'Response status code = {r.status_code}')

    if r.status_code == 200:
        logger.info(f'Successfully retrieved data from {url}!')
        data = r.json()
        logger.info(f'Writing data out to output file = {OUTPUT_FILE_NAME}...')
        with open(OUTPUT_FILE_NAME, 'w') as outfile:
            json.dump(data, outfile, indent=2)
        logger.info(f'Finished writing data!')
    else:
        logger.error(f'Problem occurred with request status code = {r.status_code} with message = {r.text}')

if __name__ == '__main__':
    main()
