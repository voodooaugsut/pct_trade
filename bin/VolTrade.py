# Hello World program in Python
    
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import urllib
import tempfile as tp
import os
import requests
from datetime import datetime
matplotlib.style.use('ggplot')
        
def downloadfile2(stock, f = 'sd1t1vml1c1p2k4k5a2'):
  
    baseurl = 'http://finance.yahoo.com/d/quotes.csv?%s'
    stock = ['{:0>4}'.format(x) + '.HK' for x in stock]
    s = '+'.join(stock)
  
    paras = urllib.urlencode({'s': s, 'f': f})
    f = urllib.urlopen(baseurl % paras)
     
    # sd1t1vml1c1p2k4k5a2
    colname = ['symbol', 'date', 'time', 'volume', 
               'daily_rng', 'last_price', 
               'change', 'change_pct', '52wH', '52wH_pct', 'avg_vol']
    data = pd.read_csv(f, names=colname)  
    data = data.set_index(['symbol']) 
    
    f.close()
    return data 
    # construct multiIndex
    
    
        
    # store data
def quote():
    home = os.path.dirname(os.getcwd())
    datahome = os.path.join(home, 'data', 'result.csv')
        
        # timestr = datetime.strftime(datetime.now(), '%D%H%M')
        # data.to_csv(os.path.join(datahome, timestr + '.csv'), index=False)
        
    def getStocklist():
        home = os.path.dirname(os.getcwd())
        ls = os.path.join(home, 'data', 'stock_list.xls')
        ls = pd.read_excel(ls)
        return ls
    def a2():
        ls = getStocklist()
        downloadfile2(ls[0])
        
        
    ls = getStocklist()
    code = ['1398', '939', '1']
    d = pd.DataFrame()
    for x in range(15):
        code = list(ls['STOCK CODE'][x*100:(x+1)*100])
        data = downloadfile2(code)
    #     print data
        d = d.append(data)
    d = d[d['volume'] > 0]
    d.to_csv(datahome)    
    # codeset = list(ls['STOCK CODE'][1500:])
    # downloadfile2(codeset)



def histDownload(code):
    code = 'HKG:' + '{:0>4}'.format(code)
    baseurl = 'https://www.google.com/finance/historical?%s'
    s = urllib.urlencode({'q': code, 'output': 'csv'})
    url = baseurl % s
    print s, url
    try:
        return pd.read_csv(url)
    except:
        print 'error on downloading'

def getStocklist():
    home = os.path.dirname(os.getcwd())
    ls = os.path.join(home, 'data', 'stock_list.xls')
    ls = pd.read_excel(ls)
    return ls

# d = {}
# ls = getStocklist()[0]
# for code in ls['STOCK CODE']:
#     print 'downloading %s \n' % code
#     d['{:0>4}'.format(code)] = histDownload(code)


data = histDownload('1')
print data

