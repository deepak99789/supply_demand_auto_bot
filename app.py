import streamlit as st
import pandas as pd
import os

st.title("🔥 Supply Demand Auto Screener")

if os.path.exists("trades.csv"):
    df = pd.read_csv("trades.csv")
    st.dataframe(df)
else:
    st.info("No trades logged yet")
