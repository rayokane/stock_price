import appdirs as ad 
ad.user_cache_dir = lambda *args: ".cache"
import yfinance as yf
yf.set_tz_cache_location(".cache")
import streamlit as st
import pandas as pd

st.write("""

# Simple Stock Price App

Shown are the stock closing price and volume of Google.
""")

# https://towardsdatascience.comhow-to-get-stock-data-using-python-c0de1df17e75
# define the ticker symbol
tickerSymbol = 'GOOGL'
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end = '2024-6-30')
# Open   High   Low Close   Volume   Dividends   Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
