import os

# General
PAGE_SIZE = 20

# Database
PROD_DB = os.environ['db']

def DB_URL():
    return PROD_DB
