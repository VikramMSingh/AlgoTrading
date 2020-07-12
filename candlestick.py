import pandas as pd
import matplotlib.pyplot as plt 
from mpl_finance import candlestick2_ohlc
from datetime import datetime, date
today = date.today()

def stock_analyze(ticker):
	x=pd.read_csv("data_files/6m/%s_%s.csv" %(ticker,today))
	x['MA50'] = x['Close'].rolling(50).mean()
	x['MA10'] = x['Close'].rolling(10).mean()
#	x['Change']=x['Close'].shift(-1) - x['Close']
	
	fig, ax = plt.subplots()
	plt.xticks(rotation=30)
#	plt.yticks(ticks=50)
	plt.xlabel("Date")
	plt.ylabel("Price")
	plt.title("%s analysis" %ticker)
	#plt.figure(figsize=(4,4))
	candlestick2_ohlc(ax, x['Open'], x['High'], x['Low'], x['Close'], width=0.5, colorup='g')
	x['MA10'].plot(ax=ax,color='b')
	x['MA50'].plot(ax=ax,color='y')
#	x['Change'].plot()
	plt.show()
	
stock_analyze("AAPL")
