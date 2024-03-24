#Initial Pandas Data QC
#Now you can use pandas to take a look at your data
import pandas as pd
nba = pd.read_csv("nba_all_elo.csv")
type(nba)
pandas.core.frame.DataFrame
 
len(nba)
#126314
 
nba.shape
#(126314, 23)
 
nba.head()
gameorder   game_id lg_id   _iscopy year_id date_game   seasongame  is_playoffs team_id fran_id ... win_equiv   opp_id  opp_fran    opp_pts opp_elo_i   opp_elo_n   game_location   game_result forecast    notes
0   1   194611010TRH    NBA 0   1947    11/1/1946   1   0   TRH Huskies ... 40.294830   NYK Knicks  68  1300.0000   1306.7233   H   L   0.640065    NaN
1   1   194611010TRH    NBA 1   1947    11/1/1946   1   0   NYK Knicks  ... 41.705170   TRH Huskies 66  1300.0000   1293.2767   A   W   0.359935    NaN
2   2   194611020CHS    NBA 0   1947    11/2/1946   1   0   CHS Stags   ... 42.012257   NYK Knicks  47  1306.7233   1297.0712   H   W   0.631101    NaN
3   2   194611020CHS    NBA 1   1947    11/2/1946   2   0   NYK Knicks  ... 40.692783   CHS Stags   63  1300.0000   1309.6521   A   L   0.368899    NaN
4   3   194611020DTF    NBA 0   1947    11/2/1946   1   0   DTF Falcons ... 38.864048   WSC Capitols    50  1300.0000   1320.3811   H   L   0.640065    NaN

#Let’s customize configuration settings

pd.set_option("display.max.columns", None)
pd.set_option("display.precision", 2)

nba.tail()
gameorder   game_id lg_id   _iscopy year_id date_game   seasongame  is_playoffs team_id fran_id pts elo_i   elo_n   win_equiv   opp_id  opp_fran    opp_pts opp_elo_i   opp_elo_n   game_location   game_result forecast    notes
126309  63155   201506110CLE    NBA 0   2015    6/11/2015   100 1   CLE Cavaliers   82  1723.41 1704.39 60.31   GSW Warriors    103 1790.96 1809.98 H   L   0.55    NaN
126310  63156   201506140GSW    NBA 0   2015    6/14/2015   102 1   GSW Warriors    104 1809.98 1813.63 68.01   CLE Cavaliers   91  1704.39 1700.74 H   W   0.77    NaN
126311  63156   201506140GSW    NBA 1   2015    6/14/2015   101 1   CLE Cavaliers   91  1704.39 1700.74 60.01   GSW Warriors    104 1809.98 1813.63 A   L   0.23    NaN
126312  63157   201506170CLE    NBA 0   2015    6/16/2015   102 1   CLE Cavaliers   97  1700.74 1692.09 59.29   GSW Warriors    105 1813.63 1822.29 H   L   0.48    NaN
126313  63157   201506170CLE    NBA 1   2015    6/16/2015   103 1   GSW Warriors    105 1813.63 1822.29 68.52   CLE Cavaliers   97  1700.74 1692.09 A   W   0.52    NaN

