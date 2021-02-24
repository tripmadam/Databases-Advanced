#libraries
from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd
import time
import pymongo as mongo


#methods
def scraper():
    URL = requests.get('https://www.blockchain.com/btc/unconfirmed-transactions')
    URL.raise_for_status()

    soup = BeautifulSoup(URL.content, 'lxml')
        
    transactions = soup.find_all('div', attrs={'class': 'sc-6nt7oh-0 PtIAf'})
    hashes = []
    times = []
    BTC = []
    Dollars = []
  
    for x in range(transactions.__len__()):
        if (x%4 == 0):
            hashes.append(transactions[x].text)
        if(x%4 == 1): 
            times.append(transactions[x].text)
        if(x%4 == 2):
            BTC.append(transactions[x].text.replace(' BTC',''))
        if(x%4 == 3):
            Dollars.append(transactions[x].text.replace('$','').replace(',',''))

    data = {'Hashes' : hashes, 'Time': times, 'Amount_BTC': BTC, 'Amount_Dollars': Dollars}
    df = pd.DataFrame(data)
    df['Amount_Dollars'] = df['Amount_Dollars'].astype(float)
    df['Amount_BTC'] = df['Amount_BTC'].astype(float)
    sort = df.sort_values('Amount_Dollars', ascending=False).head(1)
    test = sort['Hashes'].values[0] +" " + sort['Time'].values[0] + " " + str(sort['Amount_BTC'].values[0]) +" "+ str(sort['Amount_Dollars'].values[0]) + "\n"
    results = open("results.txt","a")
    results.writelines(test)
    results.close()

#constants
CLIENT = mongo.MongoClient ("mongodb://127.0.0.1:27017")    
transactions = CLIENT["transactions"]
col_amount_BTC = local_database["Amount_BTC"]


try:
    while True:
                
        scraper()

        time.sleep(60)
except KeyboardInterrupt:
    print('interrupted!')

