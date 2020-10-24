import os

TARGET_URL = os.environ['BANK_URL']
REQ_BODY = os.environ['REQ_BODY']
try:
    OUTPUT_FILE_NAME = os.environ['OUTPUT_FILE_NAME']
except KeyError:
    OUTPUT_FILE_NAME = 'data.json'
