from bs4 import BeautifulSoup
import requests

year_to_travel_to = input("Which year do you want to travel to?"
                          "Type the date in this format YYYY-MM-DD: ")

billboard_url = "https://www.billboard.com/charts/hot-100/" + year_to_travel_to

response = requests.get(url=billboard_url)
hot_hundred = response.text

soup = BeautifulSoup(hot_hundred, "html.parser")
song_title = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_title]
print(song_names)