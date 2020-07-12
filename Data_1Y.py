from pandas_datareader import *
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
today=date.today()
start_day=today+relativedelta(years=-1)
#print(start_day)
def data_collector(ticker):
    data_collected= DataReader('%s' %ticker,  'yahoo', start_day , today)
    data_collected.to_csv('data_files/annual/%s.csv' %(ticker))
    #print(data_collected)
    return 0

with open("portfolio.txt","r") as symbol_file:
    for line in symbol_file:
        data_collector(line.strip())
        print("Data gathered %s" %line.strip())
