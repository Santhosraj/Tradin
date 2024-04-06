import streamlit as st
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from textblob import TextBlob

plt.style.use("fivethirtyeight")


df = pd.read_csv(r"D:\Santhosraj Machine learning\spyder\college_project\trading\articlesData.csv\articlesData.csv")
df.set_index(pd.DatetimeIndex(df['Date'].values))
def getPolarity(text):
    return TextBlob(text).sentiment.polarity

def getSentiment(score):
    if score < 0:
        return 'Negative'
    elif score == 0:
        return 'Neutral'
    else:
        return 'Positive'

def plot_sentiment_over_time(filtered_df):
    plt.figure(figsize=(12, 4))
    plt.title("Sentiment Over Time")
    polarity = filtered_df.groupby(["Date"]).sum()['Polarity']
    plt.plot(polarity.index, polarity)
    st.pyplot(plt)



def main():
    st.title("Sentiment Analysis App")


    user_input = st.text_input("Enter a keyword for sentiment analysis:")

    if user_input:

        df['Title'].fillna("", inplace=True)


        filtered_df = df[df['Title'].str.contains(user_input, case=False, regex=True)]

        if not filtered_df.empty:

            filtered_df['Polarity'] = filtered_df['Title'].apply(getPolarity)
            filtered_df['Sentiment'] = filtered_df['Polarity'].apply(getSentiment)


            st.subheader("Sentiment Distribution:")
            st.bar_chart(filtered_df['Sentiment'].value_counts(), color="#ffaa0088")

            # Plot sentiment over time
            plot_sentiment_over_time(filtered_df)


        else:
            st.warning(f"No data found for '{user_input}'. Please try a different keyword.")

if __name__ == "__main__":
    main()
