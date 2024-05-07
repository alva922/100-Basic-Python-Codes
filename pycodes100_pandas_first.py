#https://newdigitals.org/2024/02/24/100-basic-python-codes/#pandas-first-program
#Pandas First Program
#importing pandas
import pandas as pd
#creating  list 
data=["Harry","Sam","Juliet","Robert","Max"]
#creating pandas Series
df=pd.Series(data)
#printing Series
print(df)
Output:
0     Harry
1       Sam
2    Juliet
3    Robert
4       Max
dtype: object
