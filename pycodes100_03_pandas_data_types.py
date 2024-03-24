#Displaying Pandas Data Types
#https://newdigitals.org/2024/02/24/100-basic-python-codes/#displaying-pandas-data-types
#You can display all columns and their data types with .info():
nba.info()
Output:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 126314 entries, 0 to 126313
Data columns (total 23 columns):
 #   Column         Non-Null Count   Dtype  
---  ------         --------------   ----- 
 0   gameorder      126314 non-null  int64  
 1   game_id        126314 non-null  object
 2   lg_id          126314 non-null  object
 3   _iscopy        126314 non-null  int64  
 4   year_id        126314 non-null  int64  
 5   date_game      126314 non-null  object
 6   seasongame     126314 non-null  int64  
 7   is_playoffs    126314 non-null  int64  
 8   team_id        126314 non-null  object
 9   fran_id        126314 non-null  object
 10  pts            126314 non-null  int64  
 11  elo_i          126314 non-null  float64
 12  elo_n          126314 non-null  float64
 13  win_equiv      126314 non-null  float64
 14  opp_id         126314 non-null  object
 15  opp_fran       126314 non-null  object
 16  opp_pts        126314 non-null  int64  
 17  opp_elo_i      126314 non-null  float64
 18  opp_elo_n      126314 non-null  float64
 19  game_location  126314 non-null  object
 20  game_result    126314 non-null  object
 21  forecast       126314 non-null  float64
 22  notes          5424 non-null    object
dtypes: float64(6), int64(7), object(10)
memory usage: 22.2+ MB
