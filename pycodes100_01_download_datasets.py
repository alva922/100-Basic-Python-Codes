#Download the datasets: NBA results provided by FiveThirtyEight in a 17MB CSV file.
import requests
 
download_url = "https://raw.githubusercontent.com/fivethirtyeight/data/master/nba-elo/nbaallelo.csv"
target_csv_path = "nba_all_elo.csv"
 
response = requests.get(download_url)
response.raise_for_status()    # Check that the request was successful
with open(target_csv_path, "wb") as f:
    f.write(response.content)
print("Download ready.")
 
#Output:
#Download ready.
#When you execute the script, it will save the file nba_all_elo.csv in your current working directory YOURPATH.
