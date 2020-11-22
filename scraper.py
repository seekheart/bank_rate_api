import json
from loguru import logger
import requests
from config import *
from engines import BankRateEngine
import sys

def transform_data(raw_data: dict) -> list:
    return raw_data['data']['cd_rates']


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
    else:
        logger.error(f'Problem occurred with request status code = {r.status_code} with message = {r.text}')
        sys.exit(1)

    data = transform_data(data)
    bank_rate_engine = BankRateEngine()
    logger.info('Exporting data to database')
    bank_rate_engine.drop_and_replace_data(data)

if __name__ == '__main__':
    main()
