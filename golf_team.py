import streamlit as st
import pandas as pd, numpy as np

st.title("2022 Northwod Varsity Golf Team Averages")

#creating original dataframe
players_df = pd.read_csv("Golf Team Averages 2022 Spring Season - Sheet1.csv")
columns = [column for column in players_df.columns[1:]]
columns.insert(0,"")
players_df.columns = columns
players_df.set_index("", inplace=True)

def get_average(df, col_type): #gets average depending on a certain column type
	col = [col for col in df.columns if col_type in col]
	new_df = df[col]
	new_df[col_type+" Average"] = new_df.T.mean()
	new_df.sort_values(col_type+" Average", inplace=True)
	return new_df

def average_without_max(pd_series): #gets average without the max value in a pandas series
	series_max = pd_series.max()
	sum = pd_series.sum()
	if sum != series_max:
		null_sum = pd_series.isnull().sum()
		average = (sum-series_max)/(len(pd_series)-1-null_sum)
	else:
		average = series_max
	return average

st.subheader("Season Average")
st.dataframe(players_df, 1000, 1000)

match_df = get_average(players_df, "Match")

st.subheader("Match Average")
st.dataframe(match_df, 1000, 1000)

if st.checkbox("Match Average Without Worse Score"):
	revised_match_df = pd.DataFrame(match_df.iloc[:, :-1].apply(average_without_max, axis=1))
	revised_match_df.rename(columns={0:"Scoring Average"}, inplace=True)
	revised_match_df.sort_values(by="Scoring Average", inplace=True)
	st.dataframe(revised_match_df)
