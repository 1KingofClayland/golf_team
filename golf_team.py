import streamlit as st
import pandas as pd, numpy as np

st.title("2022 Northwod Varsity Golf Team Averages")

players_df = pd.read_csv("Golf Team Averages 2022 Spring Season - Sheet1.csv")
columns = [column for column in players_df.columns[1:]]
columns.insert(0,"")
players_df.columns = columns
players_df.set_index("", inplace=True)

def get_average(df, col_type):
	col = [col for col in df.columns if col_type in col]
	new_df = df[col]
	new_df[col_type+" Average"] = new_df.T.mean()
	new_df.sort_values(col_type+" Average", inplace=True)
	return new_df

st.subheader("Season Average")
st.dataframe(players_df, 1000, 1000)

st.subheader("Match Average")
st.dataframe(get_average(players_df, "Match"), 1000, 1000)
