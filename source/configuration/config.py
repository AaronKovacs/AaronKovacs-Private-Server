import os

# General
PAGE_SIZE = 20

# Database
PROD_DB = 'mysql+pymysql://server_user:Server1234@aa6t7orqp8ohxz.cr5a3mpymtml.us-east-1.rds.amazonaws.com:3306/ebdb'

def DB_URL():
    return PROD_DB
