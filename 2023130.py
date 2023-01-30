# http://hk.finance.yahoo.com/
import yfinance as yf
import mplfinance as mpf


stock = {'彼特幣':'BTC-USD',
         'Tesla, Inc.':'TSLA',
         '元大台灣50':'0050.TW',
         '元大高股息':'0056.TW'}


# data 使用 pandas 製作
# data = yf.download(tickers=stock['元大台灣50'],start='2022-01-01',end='2023-01-30')
#
# data = data.drop(columns='Adj Close')
#
#
# mpf.plot(data,type='candle',mav=(20,60),volume=True)
print(dir(yf))