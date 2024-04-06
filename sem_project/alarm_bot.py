# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:40:32 2023

@author: SanthosRaj
"""


import yfinance as yf
from winotify import Notification, audio
import os
import time

tickers = ["BTC-USD", "ETH-USD", "XRP-USD", "BCH-USD"]

upper_limit = [4028408, 32000, 46000, 35200]
lower_limit = [10000, 13000, 1400, 280]

while True:
    try:
        last_prices = [yf.Ticker(ticker).history(period="1d")["Close"].iloc[-1] for ticker in tickers]
        print(last_prices)
        
        for i in range(len(tickers)):
            if last_prices[i] > upper_limit[i]:
                toast = Notification(app_id="Stock alarm", title="Price Alert for " + tickers[i],
                                     msg=f"{tickers[i]} has reached a price of {last_prices[i]}. You might want to sell",
                                     icon=os.path.join(os.getcwd(),
                                                      "D:/Santhosraj Machine learning/spyder/college_project/trading/sell.jpeg"),
                                     duration='long')
                toast.add_actions(label="Go to Stock Broker", launch="https://www.coinbase.com/")
                toast.set_audio(audio.LoopingAlarm6, loop=True)
                toast.show()

            elif last_prices[i] < lower_limit[i]:
                toast = Notification(app_id="Stock alarm", title="Price Alert for " + tickers[i],
                                     msg=f"{tickers[i]} has reached a price of {last_prices[i]}. You might want to buy",
                                     icon=os.path.join(os.getcwd(),
                                                      "D:/Santhosraj Machine learning/spyder/college_project/trading/buy.png"),
                                     duration='long')
                toast.add_actions(label="Go to Stock Broker", launch="https://www.coinbase.com/")
                toast.set_audio(audio.LoopingAlarm8, loop=True)
                toast.show()

        time.sleep(5)

    except Exception as e:
        print(f"Error: {e}")
        time.sleep(5)
