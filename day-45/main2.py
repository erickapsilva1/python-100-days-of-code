from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.findAll(name="span", class_="titleline")

article_texts = []
article_links = []

for article in articles:
    article_text = article.find("a")
    article_texts.append(article_text.getText())
    article_link = article_text.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.findAll(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)+1

print(article_texts[largest_index])
print(article_links[largest_index])