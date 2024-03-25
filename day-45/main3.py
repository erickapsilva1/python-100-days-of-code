from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
top_movies = response.text

soup = BeautifulSoup(top_movies, "html.parser")
movies = soup.findAll(name="h3", class_="title")

movie_list = []

for movie in movies:
    movie_list.append(movie.getText())

movie_list.reverse()
for movie in movie_list:
    with open("movies.txt", mode="a", encoding="utf-8") as file:
        file.write(movie + "\n")