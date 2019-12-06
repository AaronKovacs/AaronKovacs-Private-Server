import os

# General
PAGE_SIZE = 20

# Database
PROD_DB = 'mysql+pymysql://baja_user:Baja1234@aa194va49vp0z31.cr5a3mpymtml.us-east-1.rds.amazonaws.com:3306/ebdb'

def DB_URL():
    return PROD_DB
