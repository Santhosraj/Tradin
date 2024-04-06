 # -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:53:57 2023

@author: SanthosRaj
"""

from tkinter import *
from tkcalendar import DateEntry
import datetime as dt
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc


def visualize():
   
    from_date = cal_from.get_date()
    to_date = cal_to.get_date()

    start = dt.datetime(from_date.year, from_date.month, from_date.day)
    end = dt.datetime(to_date.year, to_date.month, to_date.day)

    ticker = text_ticker.get()
    data = yf.download(ticker, start=start, end=end)

   
    data = data[['Open', 'High', 'Low', 'Close']]

   
    data.reset_index(inplace=True)
    data.loc[:, 'Date'] = data['Date'].map(mdates.date2num)


    ax = plt.subplot()
    ax.grid(True)
    ax.set_axisbelow(True)
    ax.set_title('{} Share Price'.format(ticker), color='white')
    root.title('Visualizer') 
    ax.set_facecolor('black')
    ax.figure.set_facecolor('#121212')
    ax.tick_params(axis='x', colors='white')
    ax.tick_params(axis='y', colors='white')
    ax.xaxis_date()

  
    candlestick_ohlc(ax, data.values, width=0.5, colorup='#00ff00')
    plt.show()


root = Tk()
root.title("Stock Visualizer")


label_from = Label(root, text="From:")
label_from.pack()
cal_from = DateEntry(root, width=50, year=2010, month=1, day=1)
cal_from.pack(padx=10, pady=10)

label_to = Label(root, text="To:")
label_to.pack()
cal_to = DateEntry(root, width=50)
cal_to.pack(padx=10, pady=10)

label_ticker = Label(root, text="Ticker Symbol:")
label_ticker.pack()
text_ticker = Entry(root)
text_ticker.pack()

btn_visualize = Button(root, text="Visualize", command=visualize)
btn_visualize.pack()

root.mainloop()
