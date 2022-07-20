import configparser
import os
import time
import getpass

HOST='localhost'
PORT='3306'
DB_USER='root'
DB_PASS='root'

databases=('web_scrapping')

def get_dump(database):
    filestamp = time.strftime('%Y-%m-%d-%I')
    
    os.popen("mysqldump -h %s -P %s -u %s -p%s %s > %s.sql" % (HOST,PORT,DB_USER,DB_PASS,database,database+"_"+filestamp))
    
    print("\n|| Database dumped to "+database+"_"+filestamp+".sql || ")


if __name__=="__main__":
    for database in databases:
        get_dump(database)
