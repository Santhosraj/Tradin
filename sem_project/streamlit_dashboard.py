import yfinance as yf
import streamlit as st
from PIL import Image
from urllib.request import urlopen

# Titles and subtitles
st.title("Cryptocurrency Daily Prices | ₿")
st.header("Main Dashboard")


# Defining ticker variables
Bitcoin = 'BTC-USD'
Ethereum = 'ETH-USD'

BitcoinCash = 'BCH-USD'

# Access data from Yahoo Finance
BTC_Data = yf.Ticker(Bitcoin)
ETH_Data = yf.Ticker(Ethereum)

BCH_Data = yf.Ticker(BitcoinCash)

# Fetch crypto data for the dataframe
start_date = "2023-12-01"  # Adjust the start date as needed
end_date = "2023-12-31"
BTC = yf.download(Bitcoin, start=start_date, end=end_date)
ETH = yf.download(Ethereum, start=start_date, end=end_date)

BCH = yf.download(BitcoinCash, start=start_date, end=end_date)

# Display cryptocurrency information
def display_crypto_info(coin_name, image_url, dataframe, history_data):
    st.write(f"{coin_name} ($)")
    coin_image = Image.open(urlopen(image_url))
    st.image(coin_image)
    st.table(dataframe)
    st.bar_chart(history_data.Close)

# Display information for each cryptocurrency
display_crypto_info("BITCOIN", 'https://s2.coinmarketcap.com/static/img/coins/64x64/1.png', BTC, BTC_Data.history(period="max"))
display_crypto_info("ETHERUM", 'https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png', ETH, ETH_Data.history(period="max"))

display_crypto_info("BITCOIN CASH", 'https://s2.coinmarketcap.com/static/img/coins/64x64/1831.png', BCH, BCH_Data.history(period="max"))
