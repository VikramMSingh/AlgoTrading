import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, date
import os

today=date.today()
def analyze_hist(ticker):
    x=pd.read_csv("data_files/6m/%s_%s.csv" %(ticker,today))
    x['MA10']=x["Close"].rolling(10).mean()
    x['MA10_STD']=x["Close"].rolling(10).std()
    x['MA50']=x["Close"].rolling(50).mean()
    x['MA50_STD']=x["Close"].rolling(50).std()
    x['Change']=x['Close'].shift(-1) - x['Close']
    x['MA10_upper']=x['MA10'] + (x['MA10_STD']*2)
    x['MA10_lower']=x['MA10'] - (x['MA10_STD']*2)
    x['MA50_upper']=x["MA50"] + (x["MA50_STD"]*2)
    x['MA50_lower']=x['MA50'] - (x['MA50_STD']*2)
    #x['MA120']=x["Close"].rolling(120).mean()
    #x['MA100']=x["Close"].rolling(100).mean()
    x=x.set_index('Date')
    x=x.dropna()
    x[["Close","MA10","MA50","MA10_upper","MA10_lower","Change"]].plot(figsize=(20,8))
    plt.xlabel("Date",size=20)
    plt.ylabel('Price',size=20)
    plt.title('%s analysis'%ticker)
    plt.grid(True)
    plt.axis('tight')
    #plt.show()
    plt.savefig("results/ma_6m_analysis/%s_%s.png" %(ticker,today))

#analyze_hist("IBN")

with open("portfolio.txt","r") as symbol_file:
    for line in symbol_file:
       analyze_hist(line.strip())
       print("Analysis done and saved for %s" %line.strip())

