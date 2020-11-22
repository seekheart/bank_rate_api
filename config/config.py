import os

# Mongo Settings
MONGO_HOST = os.environ['MONGO_HOST']
MONGO_PORT = int(os.environ['MONGO_PORT'])
MONGO_DB_NAME = os.environ['MONGO_DB']


# Scraper Config
TARGET_URL = os.environ['BANK_URL']
REQ_BODY = os.environ['REQ_BODY']
try:
    OUTPUT_FILE_NAME = os.environ['OUTPUT_FILE_NAME']
except KeyError:
    OUTPUT_FILE_NAME = 'data.json'
