#Exploring the Dataset
#Exploratory Data Analysis (EDA) can help you answer questions about your dataset
#Examine how often specific values occur in a column
nba["team_id"].value_counts()
Output:
BOS    5997
NYK    5769
LAL    5078
DET    4985
PHI    4533
       ... 
INJ      60
PIT      60
DTF      60
TRH      60
SDS      11
Name: team_id, Length: 104, dtype: int64
#It seems that a team named "Lakers" played 6024 games, but only 5078 of those were played by the Los Angeles Lakers. Find out who the other "Lakers" team is:
nba.loc[nba["fran_id"] == "Lakers", "team_id"].value_counts()
Output:
LAL    5078
MNL     946
Name: team_id, dtype: int64

#Then you can use the min and max aggregate functions, to find the first and last games of Minneapolis Lakers:
nba["date_played"] = pd.to_datetime(nba["date_game"])
nba.loc[nba["team_id"] == "MNL", "date_played"].min()
nba.loc[nba['team_id'] == 'MNL', 'date_played'].max()
nba.loc[nba["team_id"] == "MNL", "date_played"].agg(("min", "max"))
 
Output:
min   1948-11-04
max   1960-03-26
Name: date_played, dtype: datetime64[ns]
