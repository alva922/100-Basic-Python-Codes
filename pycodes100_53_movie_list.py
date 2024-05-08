#https://newdigitals.org/2024/02/24/100-basic-python-codes/#must-watch-movie-list
#Must Watch Movie List
import requests
from bs4 import BeautifulSoup
 
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
 
response = requests.get(URL)
response_text = response.text
soup = BeautifulSoup(response_text, 'html.parser')
 
movies = []
titles = soup.find_all(name='h3', class_='title')
 
for i in titles:
    with open('movies.txt', 'a',encoding="utf-8" ) as file:
        file.write(i.getText()+"\n")
#Example I/O: the file movies.txt containing the list of 100 must watch movies, viz.
100) Stand By Me
99) Raging Bull
98) Amelie
97) Titanic
96) Good Will Hunting
95) Arrival
94) Lost In Translation
93) The Princess Bride
92) The Terminator
91) The Prestige
90) No Country For Old Men
89) Shaun Of The Dead
88) The Exorcist
87) Predator
86) Indiana Jones And The Last Crusade
etc.
  
