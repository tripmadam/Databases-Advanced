#libraries
from bs4 import BeautifulSoup
import requests
# import numpy as np
# import pandas as pd
import time
import pymongo as mongo
import redis 
r = redis.Redis(host='redis',port='6379')


#methods
def scraper():
    URL = requests.get('https://www.blockchain.com/btc/unconfirmed-transactions')
    URL.raise_for_status()

    soup = BeautifulSoup(URL.content, 'html.parser')
        
    transactions = soup.find_all('div', attrs={'class': 'sc-6nt7oh-0 PtIAf'})
   
        
    for x in range(transactions.__len__()):
        if(x%4 ==0):
            r.rpush(transactions[x].text ,transactions[x].text)
            r.rpush(transactions[x].text ,transactions[x+1].text)
            r.rpush(transactions[x].text, float(transactions[x+2].text.replace(' BTC','')))
            r.rpush(transactions[x].text, float(transactions[x+3].text.replace('$','').replace(',','')))
            #r.expire(transactions[x].text, 60)
            keylist.append(transactions[x].text )
            #print(r.lrange(transactions[x].text,0,-1))
        
        

def push():

    valuelist = []

    for x in keylist:
       value = r.lrange(x,2,2)
       valuelist.append(value)

    maximumindex = valuelist.index(max(valuelist))

    hashhighest = keylist[maximumindex]

    topush = r.lrange(hashhighest,0,-1)

    
    highest = {"Hash": topush[0].decode('utf-8'), "Time": topush[1].decode('utf-8') , "Amount_BTC" : topush[2].decode('utf-8') , "Amount_USD" : topush[3].decode('utf-8') }
    x = col_transactions.insert_one(highest)

    xID = x.inserted_id
    print(col_transactions.find_one(xID))

    keylist.clear()
    r.flushdb()



#constants
CLIENT = mongo.MongoClient ("mongodb://mongo:27017")    
transactions_db = CLIENT["Transactions"]
col_transactions = transactions_db["transactions"]
keylist = []

try:
    while True:
                
        scraper()
        time.sleep(10)
        scraper()
        time.sleep(10)
        scraper()
        time.sleep(10)
        scraper()
        time.sleep(10)
        scraper()
        time.sleep(10)
        scraper()
        push()
        time.sleep(10)
        

except KeyboardInterrupt:
    print(' interrupted!')

