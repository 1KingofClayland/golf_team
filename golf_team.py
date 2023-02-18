import streamlit as st
import pandas as pd, numpy as np

st.set_page_config(page_title="NHS Golf Team", page_icon=":golf:", layout="wide", initial_sidebar_state="collapsed")

st.title("2023 Northwood Varsity Golf Team Averages")

#creating original dataframe
players_df = pd.read_csv("Golf Team Averages 2023 Spring Season.csv")
scorecard_df = pd.read_csv("Golf Team Scorecard 2023 Spring Season.csv")
stats_df = pd.read_csv("Golf Team Stats 2023 Spring Season.csv")
stats_df.drop(columns="Unnamed: 0", inplace=True)
stats_df.set_index("Player", inplace=True)
columns = [column for column in players_df.columns[1:]]
columns.insert(0,"")
players_df.columns = columns
players_df.set_index("", inplace=True)

def get_average(df, col_types): #gets average depending on one or more column types
	columns = []
	for col in df.columns:
		if any(col_type in col for col_type in col_types):
			columns.append(col)
	new_df = df[columns]
	new_df["Scoring Average"] = new_df.T.mean()
	new_df.sort_values("Scoring Average", inplace=True)
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

#gets the type of dataframe the user wants
selection = st.sidebar.selectbox("Dataframe", ("Season Average", "User Selected Average", "Match Average Without Worse Score"))

if selection == "Season Average": #gives entire dataframe
	st.subheader("Season Average")
	st.table(players_df)

	st.subheader("Season Stats")
	st.table(stats_df)

if selection == "User Selected Average": #gives selected columns of dataframe
	col_types = st.sidebar.multiselect("Round Type", ("Match", "Practice Round", "Oak Creek", "Strawberry Farms", "Rancho San Joaquin"))
	select_df = get_average(players_df, col_types)

	st.subheader("Selected Average")
	st.table(select_df)

if selection == "Match Average Without Worse Score":
	revised_match_df = pd.DataFrame(get_average(players_df, ["Match"]).iloc[:, :-1].apply(average_without_max, axis=1))
	revised_match_df.rename(columns={0:"Scoring Average"}, inplace=True)
	revised_match_df.sort_values(by="Scoring Average", inplace=True)
	st.table(revised_match_df)