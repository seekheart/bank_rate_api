import os

# Scraper Config
try:
    TARGET_URL = os.environ['BANK_URL']
except Exception as e:
    TARGET_URL = ""
try:
    REQ_BODY = os.environ['REQ_BODY']
except:
    REQ_BODY = ""

