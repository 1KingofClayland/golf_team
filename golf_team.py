import streamlit as st
import pandas as pd, numpy as np

st.title("2022 Northwod Varsity Golf Team Averages")

players_df = pd.read_csv("Golf Team Averages 2022 Spring Season - Sheet1.csv")
columns = [column for column in players_df.columns[1:]]
columns.insert(0,"")
players_df.columns = columns
players_df.set_index("", inplace=True)

def sort_players(df, col):
  return df.iloc[:-1,:].sort_values(by=col)

st.dataframe(players_df, 1000, 1000)